from pathlib import Path
import sys


def collect():
    print("Collecting data...")


def categorizing():
    print("Categorizing...")


def organize():
    extension_map = {
        "Development": [".py", ".cs", ".js", ".html", ".css", ".sql", ".json", ".xml", ".cpp"],
        "Data": [".csv", ".xlsx", ".xls", ".json", ".db", ".sqlite", ".tsv"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".odt", ".rtf"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".ico"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Media": [".mp3", ".mp4", ".wav", ".mkv", ".mov"],
        "System": [".exe", ".msi", ".bin", ".bat", ".sh", ".ini", ".log"]
    }

    if getattr(sys, 'frozen', False):
        parent = Path(sys.executable).resolve().parent
    else:
        parent = Path(__file__).resolve().parent

    print(f"Organizing folder: {parent}")

    for file in parent.iterdir():
        if file.is_dir() or file.name == Path(sys.executable).name:
            continue

        for category, extension in extension_map.items():
            if file.suffix.lower() in extension:
                create = parent / category
                create.mkdir(exist_ok=True)
                target = create / file.name

                try:
                    file.rename(target)
                    print(f"Moved: {file.name} -> {category}")
                except OSError:
                    print(
                        f"Skipping {file.name}: File is currently open or access is denied.")


if __name__ == "__main__":
    collect()
    categorizing()
    organize()
