#!/usr/bin/env python3
"""
富丽 FULI 工作空间扫描器 v0.2

生成工作空间的轻量快照，不修改用户文件。
无需外部依赖包。
"""

from pathlib import Path
import argparse, os, hashlib, json, time
from collections import Counter, defaultdict
from datetime import datetime

IGNORE_DIRS = {
    ".git", ".fuli", ".advisor", "node_modules", ".venv", "venv",
    "__pycache__", ".DS_Store"
}

def file_hash(path, limit=50 * 1024 * 1024):
    try:
        if path.stat().st_size > limit:
            return None
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None

def scan(root: Path):
    files = []
    hashes = defaultdict(list)
    ext_counts = Counter()
    now = time.time()

    for p in root.rglob("*"):
        try:
            rel = p.relative_to(root)
            if any(part in IGNORE_DIRS for part in rel.parts):
                continue
            if not p.is_file():
                continue
            st = p.stat()
            ext = p.suffix.lower() or "[no_ext]"
            ext_counts[ext] += 1
            h = file_hash(p)
            if h:
                hashes[h].append(str(rel))
            files.append({
                "path": str(rel),
                "name": p.name,
                "ext": ext,
                "size": st.st_size,
                "modified": datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds"),
                "age_days": round((now - st.st_mtime) / 86400, 1),
            })
        except Exception:
            continue

    duplicates = [paths for paths in hashes.values() if len(paths) > 1]

    final_like = []
    tokens = ("final", "最终", "最新版", "latest", "new", "新版", "定稿")
    for f in files:
        low = f["name"].lower()
        if any(t in low for t in tokens):
            final_like.append(f["path"])

    git = (root / ".git").exists()

    return {
        "workspace": str(root.resolve()),
        "scanned_at": datetime.now().isoformat(timespec="seconds"),
        "file_count": len(files),
        "git_repository": git,
        "extension_counts": dict(ext_counts.most_common()),
        "duplicates": duplicates[:50],
        "final_like_files": final_like[:100],
        "recent_files": sorted(files, key=lambda x: x["modified"], reverse=True)[:100],
        "files": files[:5000],
    }

def to_markdown(snapshot):
    lines = []
    lines.append("# Workspace Snapshot")
    lines.append("")
    lines.append(f"- Workspace: `{snapshot['workspace']}`")
    lines.append(f"- Scanned at: {snapshot['scanned_at']}")
    lines.append(f"- File count: {snapshot['file_count']}")
    lines.append(f"- Git repository: {snapshot['git_repository']}")
    lines.append("")
    lines.append("## File types")
    for ext, count in snapshot["extension_counts"].items():
        lines.append(f"- `{ext}`: {count}")
    lines.append("")
    lines.append("## Duplicate file groups")
    if snapshot["duplicates"]:
        for i, group in enumerate(snapshot["duplicates"], 1):
            lines.append(f"{i}. " + " | ".join(f"`{x}`" for x in group))
    else:
        lines.append("- None detected by identical file hash.")
    lines.append("")
    lines.append("## Final/latest-like names")
    if snapshot["final_like_files"]:
        for x in snapshot["final_like_files"]:
            lines.append(f"- `{x}`")
    else:
        lines.append("- None detected.")
    lines.append("")
    lines.append("## Recently modified files")
    for f in snapshot["recent_files"][:50]:
        lines.append(f"- `{f['path']}` — {f['modified']} — {f['size']} bytes")
    return "\n".join(lines) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workspace", nargs="?", default=".", help="workspace path")
    ap.add_argument("--out", default=None, help="output directory")
    args = ap.parse_args()

    root = Path(args.workspace).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Workspace not found or not a directory: {root}")

    out = Path(args.out).expanduser().resolve() if args.out else root / ".fuli" / "snapshots"
    if not out.exists():
        out.mkdir(parents=True)

    snap = scan(root)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    json_path = out / f"{stamp}.json"
    md_path = out / f"{stamp}.md"

    json_path.write_text(json.dumps(snap, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(to_markdown(snap), encoding="utf-8")

    print(md_path)
    print(json_path)

if __name__ == "__main__":
    main()
