# General info
It is a simple console app that merges PDF files in given directory.

# Technologies
* Python 3.10
* PyPDF2 1.26.0

# Install
1. Clone repository
2. Install requirements
   > pip install -r requirements.txt

# Usage
1. Pass only path to merge ALL pdf files in there
   > python merge.py /path/to/pdf/files
2. Pass path and file names to merge only them
   > python merge.py /path/to/pdf/files -f file1 file2
3. You can also pass output path
   > python merge.py /path/to/pdf/files -f file1 file2 -o /path/to/output

# TODO
* tests - check if content of merged file is correct

# Status
Project is: _in progress_

# Contact
Created by [@Gasper3](https://github.com/Gasper3) - feel free to contact me!
