#!/usr/bin/env python3
"""Organizador de arquivos via linha de comando."""

import argparse
import sys
from pathlib import Path
import shutil

CATEGORIES = {
    "Imagens": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"},
    "Documentos": {".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf"},
    "Planilhas": {".xls", ".xlsx", ".csv", ".ods"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".wmv"},
    "Audios": {".mp3", ".wav", ".flac", ".aac", ".ogg"},
    "Compactados": {".zip", ".rar", ".7z", ".tar", ".gz"},
}


def get_unique_path(target_path: Path) -> Path:
    """Retorna um caminho único adicionando sufixo numérico (_1, _2...) caso o arquivo já exista."""
    if not target_path.exists():
        return target_path

    counter = 1
    stem = target_path.stem
    suffix = target_path.suffix
    parent = target_path.parent

    while True:
        candidate = parent / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def resolve_category(extension: str) -> str:
    """Mapeia a extensão para a categoria correspondente."""
    ext = extension.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Outros"


def organize_directory(directory: Path, dry_run: bool = False) -> None:
    """Varre o diretório e move os arquivos para suas respectivas pastas de categoria."""
    stats = {cat: 0 for cat in CATEGORIES}
    stats["Outros"] = 0

    files = [f for f in directory.iterdir() if f.is_file()]

    if not files:
        print("Nenhum arquivo encontrado para organizar.")
        return

    prefix = "[DRY-RUN] " if dry_run else ""

    for file_path in files:
        category = resolve_category(file_path.suffix)
        dest_dir = directory / category
        dest_file = get_unique_path(dest_dir / file_path.name)

        stats[category] += 1

        if dry_run:
            if dest_file.name != file_path.name:
                print(f"{prefix}{file_path.name} -> {category}/{dest_file.name} (conflito de nome)")
            else:
                print(f"{prefix}{file_path.name} -> {category}/")
            continue

        dest_dir.mkdir(exist_ok=True)
        shutil.move(str(file_path), str(dest_file))

        if dest_file.name != file_path.name:
            print(f"[MOVIDO] {file_path.name} -> {category}/{dest_file.name} (renomeado)")
        else:
            print(f"[MOVIDO] {file_path.name} -> {category}/")

    print("\n--- Resumo ---")
    for category, count in stats.items():
        if count > 0:
            print(f"{category}: {count}")


def parse_args() -> argparse.Namespace:
    """Configura e valida os argumentos de CLI."""
    parser = argparse.ArgumentParser(
        description="Organiza arquivos de um diretório em subpastas por extensão."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Caminho do diretório a ser organizado (Padrão: diretório atual)",
    )
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Simula a execução sem mover nenhum arquivo",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target_dir = Path(args.path).resolve()

    if not target_dir.exists():
        print(f"Erro: O caminho '{target_dir}' não existe.", file=sys.stderr)
        sys.exit(1)

    if not target_dir.is_dir():
        print(f"Erro: O caminho '{target_dir}' não é um diretório.", file=sys.stderr)
        sys.exit(1)

    print(f"Diretório alvo: {target_dir}")
    if args.dry_run:
        print("Modo de simulação ativo. Nenhum arquivo será alterado.\n")

    organize_directory(target_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()