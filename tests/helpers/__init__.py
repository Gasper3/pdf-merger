from pathlib import Path

from PyPDF2 import PdfFileReader

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


def check_merged_file(pdf_file):
    expected_pages_content = ["Strona 1", "Strona 2", "Strona 3", "Page1", "Page2", "Page3"]

    reader = PdfFileReader(pdf_file)

    for i, page in enumerate(reader.pages):
        content = page.extractText()
        assert content.find(expected_pages_content[i]) != -1
