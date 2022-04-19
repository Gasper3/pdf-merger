from app.PDFMerger import Merger
from .helpers import create_args, remove_created_files, get_contents_names


def test_merge_from_path(resources_path):
    args = create_args()
    merger = Merger(**args)

    merger.merge_files()

    assert merger.merged_file_name in get_contents_names(resources_path)
    remove_created_files(resources_path)


def test_merge_to_output_not_exist(resources_path):
    output_path = resources_path.joinpath("new_output")
    args = create_args(output=output_path)
    merger = Merger(**args)

    merger.merge_files()

    assert merger.merged_file_name in get_contents_names(output_path)
    remove_created_files(resources_path)
