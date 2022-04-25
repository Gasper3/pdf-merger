from pathlib import Path


def remove_directory_contents(path: Path):
    for item in path.iterdir():
        if item.is_dir():
            remove_directory_contents(item)
        elif item.is_file():
            item.unlink()


def remove_item(item_to_remove: Path):
    if item_to_remove.is_dir():
        remove_directory_contents(item_to_remove)
        item_to_remove.rmdir()
    elif item_to_remove.is_file():
        item_to_remove.unlink()


def remove_created_files(resources_path: Path):
    for item in resources_path.joinpath("output").iterdir():
        remove_item(item)

    for item in resources_path.iterdir():
        if item.name in ["output", "pdf1.pdf", "pdf2.pdf", "pdf3.pdf"]:
            continue
        remove_item(item)
