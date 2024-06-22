# Directory To Tar

A Python-based tool designed to efficiently create backups of directories into tar.gz archives.

### Overview
This project contains a Python script that creates a .tar.gz archive of a specified directory.

It provides a progress bar to visually track the archiving process.

The script uses the os, tarfile, and datetime modules from the Python standard library and the progress module for displaying the progress bar.

### Features

Directory Archiving: Compresses a specified directory into a .tar.gz file.

Progress Bar: Displays a progress bar to show the archiving progress.

Error Handling: Handles errors gracefully during the archiving process.

Timestamp Generation: Generates a timestamp string for naming the archive file.


#### Requirements

Python 3.x

progress module (can be installed via pip install progress)



#### Installation

Clone the repository:

```bash
git clone https://github.com/MoeinTavakoli/dir_to_tar
cd dir_to_tar
```

Install the required module:

```bash
pip install progress
```

Run the script from the command line with the directory you want to archive as an argument:

```
python3 main.py -d /path/to/directory
```