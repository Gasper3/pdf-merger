from pathlib import Path

import pytest
from PyPDF2 import PdfFileReader

from pdfmerge2.exceptions import PathNotExistsError, FilesNotFoundInDirectoryError
from pdfmerge2.merger import Merger
from .helpers import create_args, get_contents_names


def test_merge_from_path(resources_path):
    args = create_args()
    merger = Merger(**args)

    merger.merge_files()

    assert merger.merged_file_path.name in get_contents_names(resources_path)
    with merger.merged_file_path.open(mode='rb') as merged_file:
        reader = PdfFileReader(merged_file)
        assert 12 == len(reader.pages)


def test_merge_to_output_not_exist(resources_path):
    output_path = resources_path.joinpath("new_output")
    args = create_args(output=output_path)
    merger = Merger(**args)

    merger.merge_files()

    assert merger.merged_file_path.name in get_contents_names(output_path)
    with merger.merged_file_path.open(mode='rb') as merged_file:
        reader = PdfFileReader(merged_file)
        assert 12 == len(reader.pages)


def test_merge_specified_files(resources_path):
    args = create_args(pdf_files=['pdf1', 'pdf2'])
    merger = Merger(**args)

    merger.merge_files()

    assert merger.merged_file_path.name in get_contents_names(resources_path)
    with merger.merged_file_path.open(mode='rb') as merged_file:
        reader = PdfFileReader(merged_file)
        assert 6 == reader.numPages


def test_bad_path():
    args = create_args(path=Path("asd/qwe"))
    merger = Merger(**args)

    with pytest.raises(PathNotExistsError):
        merger.merge_files()


def test_file_not_found():
    args = create_args(pdf_files=['bad_file1', 'bad_file2'])
    merger = Merger(**args)

    with pytest.raises(FileNotFoundError):
        merger.merge_files()


def test_files_in_path_not_found(resources_path):
    args = create_args(path=resources_path.joinpath("output"))
    merger = Merger(**args)

    with pytest.raises(FilesNotFoundInDirectoryError):
        merger.merge_files()
