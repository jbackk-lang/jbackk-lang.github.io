#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path

def build_repo_index(root: Path) -> str:
    lines = []
    lines.append(f"# Indeks repozytorium\n")
    lines.append(f"Root: `{root}`\n")

    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = Path(dirpath).relative_to(root)
        indent_level = len(rel_dir.parts)
        indent = "  " * indent_level

        # katalog
        if rel_dir == Path("."):
            lines.append(f"\n## .\n")
        else:
            lines.append(f"\n## {rel_dir}\n")

        # pliki
        for fname in sorted(filenames):
            fpath = Path(dirpath) / fname
            rel_path = fpath.relative_to(root)
            size = fpath.stat().st_size
            lines.append(f"{indent}- **Plik:** `{rel_path}`  (rozmiar: {size} B)")

    return "\n".join(lines)


def main():
    # katalog repo – możesz zmienić na ścieżkę bezwzględną
    root = Path(".").resolve()
    index_md = build_repo_index(root)

    out_file = root / "repo_index.md"
    with out_file.open("w", encoding="utf-8") as f:
        f.write(index_md)

    print(f"[OK] Zapisano indeks repo do: {out_file}")


if __name__ == "__main__":
    main()
