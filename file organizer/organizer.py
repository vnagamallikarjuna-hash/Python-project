import os
import shutil
import logging
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# File categories and extensions
FILE_TYPES = {
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx",
        ".xls", ".xlsx", ".csv"
    ],
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".webp", ".svg", ".tiff"
    ],
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv"
    ],
    "Audio": [
        ".mp3", ".wav", ".aac", ".flac", ".ogg"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],
    "Code": [
        ".py", ".java", ".c", ".cpp", ".html",
        ".css", ".js", ".php", ".sql"
    ],
    "Installers": [
        ".exe", ".msi", ".apk", ".deb"
    ]
}


def get_category(extension):
    """Return the category for a file extension."""
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def get_unique_path(destination):
    """Avoid overwriting files with the same name."""
    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix
    parent = destination.parent
    count = 1

    while True:
        new_path = parent / f"{stem}_{count}{suffix}"
        if not new_path.exists():
            return new_path
        count += 1


def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.is_dir():
        print("Error: Invalid folder path.")
        return

    moved = 0
    failed = 0
    skipped = 0

    print("\nStarting file organization...\n")

    try:
        # Snapshot entries before moving files
        entries = list(os.scandir(folder))
    except OSError as error:
        print(f"Cannot access folder: {error}")
        logging.error("Folder scan failed: %s", error)
        return

    for entry in entries:
        if not entry.is_file(follow_symlinks=False):
            skipped += 1
            continue

        source = Path(entry.path)
        category = get_category(source.suffix)
        destination_folder = folder / category

        try:
            destination_folder.mkdir(
                parents=True, exist_ok=True
            )

            destination = get_unique_path(
                destination_folder / source.name
            )

            shutil.move(str(source), str(destination))

            print(f"[MOVED] {source.name} -> {category}")
            logging.info(
                "Moved %s to %s", source.name, destination
            )
            moved += 1

        except (OSError, shutil.Error) as error:
            print(f"[ERROR] {source.name}: {error}")
            logging.error(
                "Failed to move %s: %s", source.name, error
            )
            failed += 1

    # Final report
    print("\n" + "=" * 40)
    print("       FILE ORGANIZATION REPORT")
    print("=" * 40)
    print(f"Files moved successfully : {moved}")
    print(f"Files failed             : {failed}")
    print(f"Items skipped            : {skipped}")
    print(f"Completed at             : {datetime.now()}")
    print("Log file                 : organizer.log")
    print("=" * 40)

    logging.info(
        "Finished: moved=%d, failed=%d, skipped=%d",
        moved, failed, skipped
    )


if __name__ == "__main__":
    path = input("Enter the folder path to organize: ").strip()
    organize_folder(path)