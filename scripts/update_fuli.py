#!/usr/bin/env python3
"""
富丽自更新脚本 v0.4

安全地从官方仓库更新富丽系统文件。
仅支持 Git 安装方式，不做强制覆盖。
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Optional

OFFICIAL_REPO = "https://github.com/ydj9931/fuli.git"


def run(cmd: list[str], cwd: Path) -> tuple[int, str, str]:
    """运行命令，返回 (返回码, stdout, stderr)"""
    try:
        r = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=30)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except subprocess.TimeoutExpired:
        return -1, "", "命令超时"
    except FileNotFoundError:
        return -1, "", f"未找到命令: {cmd[0]}"


def check_git_available() -> bool:
    """检查 git 是否可用"""
    code, _, _ = run(["git", "--version"], Path.cwd())
    return code == 0


def find_fuli_dir() -> Path | None:
    """查找富丽安装目录（当前脚本所在目录的父目录）"""
    return Path(__file__).resolve().parent.parent


def is_git_repo(fuli_dir: Path) -> bool:
    """确认是 Git 仓库"""
    code, _, _ = run(["git", "rev-parse", "--git-dir"], fuli_dir)
    return code == 0


def check_origin(fuli_dir: Path) -> bool:
    """确认 origin 指向官方仓库"""
    code, stdout, _ = run(["git", "remote", "get-url", "origin"], fuli_dir)
    if code != 0:
        return False
    return "ydj9931/fuli" in stdout


def has_local_changes(fuli_dir: Path) -> bool:
    """检查是否有未提交的本地修改"""
    code, stdout, _ = run(["git", "status", "--porcelain"], fuli_dir)
    return code == 0 and bool(stdout)


def get_current_version(fuli_dir: Path) -> str | None:
    """读取当前 VERSION 文件"""
    vf = fuli_dir / "VERSION"
    if vf.exists():
        return vf.read_text().strip()
    return None


def get_latest_version(fuli_dir: Path) -> str | None:
    """获取远程最新 VERSION"""
    code, _, _ = run(["git", "fetch", "origin"], fuli_dir)
    if code != 0:
        return None
    code, stdout, _ = run(
        ["git", "show", "origin/main:VERSION"], fuli_dir
    )
    if code == 0:
        return stdout.strip()
    return None


def can_fast_forward(fuli_dir: Path) -> bool:
    """检查是否可以 fast-forward 合并"""
    code, stdout, _ = run(
        ["git", "rev-list", "--left-right", "main...origin/main"],
        fuli_dir,
    )
    if code != 0:
        return False
    lines = [l for l in stdout.split("\n") if l]
    # 以 '>' 开头的行表示 origin 领先，以 '<' 开头的行表示本地领先
    has_local = any(l.startswith("<") for l in lines)
    return not has_local


def show_changelog_summary(fuli_dir: Path) -> str:
    """获取 CHANGELOG 中最新版本的摘要"""
    code, stdout, _ = run(
        ["git", "show", "origin/main:CHANGELOG.md"], fuli_dir
    )
    if code != 0:
        return "无法获取 CHANGELOG"
    lines = stdout.split("\n")
    # 提取第一个版本块的前 15 行
    in_block = False
    summary = []
    count = 0
    for line in lines:
        if line.startswith("## v"):
            if in_block:
                break
            in_block = True
        if in_block:
            summary.append(line)
            count += 1
            if count > 15:
                break
    return "\n".join(summary) if summary else "无变更摘要"


def do_update(fuli_dir: Path) -> bool:
    """执行 fast-forward 更新"""
    code, stdout, stderr = run(
        ["git", "merge", "--ff-only", "origin/main"], fuli_dir
    )
    return code == 0


def main():
    fuli_dir = find_fuli_dir()
    print(f"富丽安装目录: {fuli_dir}")

    if not check_git_available():
        print("❌ 未检测到 git，自动更新仅支持 Git 安装方式。")
        print("   请手动重新下载最新版本: git clone https://github.com/ydj9931/fuli.git")
        sys.exit(1)

    if not is_git_repo(fuli_dir):
        print("❌ 当前安装不是 Git 仓库。")
        print("   如果通过 ZIP 安装，请重新下载最新版本。")
        sys.exit(1)

    if not check_origin(fuli_dir):
        print("❌ origin 未指向官方仓库 (ydj9931/fuli)。")
        print("   请确认 remote 配置正确。")
        sys.exit(1)

    if has_local_changes(fuli_dir):
        print("⚠️  检测到本地修改，未自动覆盖。")
        print("   如需重置: git -C", fuli_dir, "stash && git merge --ff-only origin/main")
        print("   或手动备份修改后再更新。")
        sys.exit(1)

    current = get_current_version(fuli_dir) or "未知"
    print(f"当前版本: {current}")

    latest = get_latest_version(fuli_dir)
    if latest is None:
        print("❌ 无法获取远程版本信息，请检查网络连接。")
        sys.exit(1)
    print(f"最新版本: {latest}")

    if current == latest:
        print("✅ 已是最新版本。")
        sys.exit(0)

    if not can_fast_forward(fuli_dir):
        print("❌ 无法自动 fast-forward 更新，本地与远程存在分歧。")
        print("   请手动处理: cd", fuli_dir, "&& git fetch && git status")
        sys.exit(1)

    print("\n更新内容:")
    print(show_changelog_summary(fuli_dir))
    print()

    if do_update(fuli_dir):
        new_ver = get_current_version(fuli_dir) or latest
        print(f"✅ 更新成功: {current} → {new_ver}")
    else:
        print("❌ 更新失败，请手动执行: cd", fuli_dir, "&& git pull")
        sys.exit(1)


if __name__ == "__main__":
    main()
