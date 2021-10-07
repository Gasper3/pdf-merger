import argparse
from app.PDFMerger import Merger

def main():
    parser = argparse.ArgumentParser(description="Merge .pdf files")
    parser.add_argument("-o", "--output", help="Path where merged file will be saved", type=str)
    parser.add_argument("-f", "--files", help="Merge only these files", type=str, metavar="name", nargs="+")
    parser.add_argument('path', help="Path to pdf files", type=str)

    args = parser.parse_args()

    Merger(args).merge_files()

if __name__ == "__main__":
    main()
