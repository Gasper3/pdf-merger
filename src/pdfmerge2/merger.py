from datetime import datetime
from pathlib import Path

import PyPDF2

from .exceptions import FilesNotFoundInDirectoryError, PathNotExistsError


class Merger:
    def __init__(self, path: Path | str, pdf_files: list[str], output: Path | str):
        self.pdf_merger = PyPDF2.PdfFileMerger()

        self.path: Path = Path(path) if isinstance(path, str) else path
        self.pdf_files: list[str] = pdf_files
        self.output_path: Path = self._parse_output(output)

        self.merged_file_path: Path | None = None

    def merge_files(self):
        self._validate()

        for file in self._get_files():
            with file.open(mode='rb') as pdf_file:
                self.pdf_merger.append(fileobj=pdf_file)

        self._write_merged_files()

    def _get_files(self) -> list[Path]:
        if self.pdf_files:
            return [self.path.joinpath(file if file.endswith(".pdf") else f"{file}.pdf") for file in self.pdf_files]

        pdf_files = [filename for filename in self.path.iterdir() if filename.suffix == ".pdf"]
        pdf_files.sort(key=lambda item: item.name.lower())

        if not pdf_files:
            raise FilesNotFoundInDirectoryError(self.path.name)

        return pdf_files

    def _write_merged_files(self):
        filename = datetime.now().strftime('%Y-%m-%d_%H%M%S_merged')
        output_path = self.output_path.joinpath(f"{filename}.pdf")
        self.merged_file_path = output_path.resolve()

        with open(output_path, 'wb') as pdf_output:
            self.pdf_merger.write(fileobj=pdf_output)

    def _validate(self):
        if not self.path.exists():
            raise PathNotExistsError(self.path)
        if not self.output_path.exists():
            self.output_path.mkdir()

    def _parse_output(self, output_path) -> Path:
        if output_path is None:
            return self.path
        return Path(output_path) if isinstance(output_path, str) else output_path
