# General info
It is a simple CLI app that merges PDF files in given directory

# Technologies
* Python 3.10
* PyPDF2 1.26.0

# Install
## Using pip
```
pip install pdfmerge2
```

## Cloning repository for development
1. Clone repository
2. Install requirements
   ```
   pip install -r requirements.txt
   ```
   or
   ```
   poetry install
   ```

# Usage
1. Pass only path to merge ALL pdf files in there
   ```
   pdfmerge2 /path/to/pdf/files
   ```
2. Pass path and file names to merge only them 
   ```
   pdfmerge2 /path/to/pdf/files -f file1 file2
   ```
3. You can also pass output path
   ```
   pdfmerge2 /path/to/pdf/files -f file1 file2 -o /path/to/output
   ```

# Contact
Created by [@Gasper3](https://github.com/Gasper3) - feel free to contact me!
