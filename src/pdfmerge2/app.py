import argparse
import os

from .exceptions import FilesNotFoundInDirectoryError, PathNotExistsError
from .merger import Merger

is_debug = os.getenv("PDFMERGER2_DEBUG")


def run():
    parser = argparse.ArgumentParser(description="Merge .pdf files")
    parser.add_argument("-o", "--output", help="Path where merged file will be saved", type=str)
    parser.add_argument("-f", "--files", help="Merge only these files", type=str, metavar="name", nargs="+")
    parser.add_argument('path', help="Path to pdf files", type=str)

    args = parser.parse_args()

    merger = Merger(args.path, args.files, args.output)

    try:
        merger.merge_files()
    except PathNotExistsError as e:
        print("Provided path does not exist" if not is_debug else e)
    except FilesNotFoundInDirectoryError as e:
        print("Files not found" if not is_debug else e)
    except FileNotFoundError as e:
        print("File not found" if not is_debug else e)
    except Exception as e:
        print("Error occurred" if not is_debug else e)
    else:
        print(f"Files merged into: {merger.merged_file_name}")
