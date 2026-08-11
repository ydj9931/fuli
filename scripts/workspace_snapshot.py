#!/usr/bin/env python3
"""富丽 v0.3 确定性工作空间快照辅助脚本。

默认不创建 .fuli/。输出目录必须由调用方显式提供并提前存在。
"""
from pathlib import Path
import argparse, hashlib, json
from collections import Counter, defaultdict
from datetime import datetime

IGNORE_DIRS={'.git','.fuli','.advisor','node_modules','.venv','venv','__pycache__'}

def file_hash(path, limit=50*1024*1024):
    try:
        if path.stat().st_size > limit: return None
        h=hashlib.sha256()
        with path.open('rb') as f:
            for chunk in iter(lambda:f.read(1024*1024), b''): h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None

def scan(root):
    files=[]; hashes=defaultdict(list); exts=Counter()
    for p in root.rglob('*'):
        try:
            rel=p.relative_to(root)
            if any(part in IGNORE_DIRS for part in rel.parts) or not p.is_file(): continue
            st=p.stat(); ext=p.suffix.lower() or '[no_ext]'; exts[ext]+=1
            h=file_hash(p)
            if h: hashes[h].append(str(rel))
            files.append({'path':str(rel),'size':st.st_size,'modified':datetime.fromtimestamp(st.st_mtime).isoformat(timespec='seconds')})
        except Exception: pass
    return {'workspace':str(root.resolve()),'scanned_at':datetime.now().isoformat(timespec='seconds'),'file_count':len(files),'git_repository':(root/'.git').exists(),'extension_counts':dict(exts.most_common()),'duplicate_groups':[v for v in hashes.values() if len(v)>1][:50],'recent_files':sorted(files,key=lambda x:x['modified'], reverse=True)[:100]}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('workspace',nargs='?',default='.'); ap.add_argument('--out',required=True)
    args=ap.parse_args(); root=Path(args.workspace).expanduser().resolve(); out=Path(args.out).expanduser().resolve()
    if not root.is_dir(): raise SystemExit(f'Workspace not found: {root}')
    if not out.is_dir(): raise SystemExit(f'Output directory does not exist: {out}. Create it only after user-authorized initialization.')
    stamp=datetime.now().strftime('%Y%m%d-%H%M%S'); path=out/f'{stamp}.json'; path.write_text(json.dumps(scan(root),ensure_ascii=False,indent=2),encoding='utf-8'); print(path)

if __name__=='__main__': main()
