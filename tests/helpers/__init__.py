from pathlib import Path

from .remove_created_items import remove_created_files


def create_args(path: Path = None, pdf_files=None, output: Path = None):
    if path is None:
        path = Path("tests/resources")
    return {
        "path": path,
        "pdf_files": pdf_files,
        "output": Path(output) if output is not None else None
    }


def get_contents_names(path: Path):
    result = []
    for item in path.iterdir():
        result.append(item.name)

    return result
