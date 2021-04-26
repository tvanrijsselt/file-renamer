# Rename multiple files in a directory

Simple project to change specific files in a certain folder with Python 3.9 with buildt-in OS library.
When the main.py is called in Terminal, the program will ask for a specific directory,
what base you want for all filenames and wether you want the select files ending on a specific extension.

The filenames will be changes to to the base you select plus a counter.

## Example use-case

After a holiday you come home with many photos of your trip. These generally have names such as:
<br>DISC09221.jpg
<br>DISC09222.jpg
<br>DISC09223.jpg
<br>DISC09224.jpg
By calling the program to change these files with the basename barcelona042421. The files will be renamed to:
<br>barceonaDDMMYYYY_1.jpg
<br>barceonaDDMMYYYY_2.jpg
<br>barceonaDDMMYYYY_3.jpg
<br>barceonaDDMMYYYY_4.jpg

## Setup

To run this project install Python 3.9 on your machine:
$ cd ../file-rename
$ python main.py

## Running the script tutorial

<br> If you want to change the name of certain files, such as these:
![alt text](https://github.com/tvanrijsselt/file-renamer/master/tutorial_mages/files.png?raw=true)
<br> Open terminal
<br> Change directory to root of file-rename project folder
<br> Call python main.py
<br> Paste directory where you want files to change
<br> Enter yes if you only want to change files of a certain extension (i.e. png)
<br> Visualized steps in Terminal
![alt text](https://github.com/tvanrijsselt/file-renamer/master/tutorial_mages/screenshotfinal.png?raw=true)


## Improvements to be made

Pathlib module will be added to manage the file paths, such that the project can also be operating systems such as macOS / Linux. Because of the current usage of the double backslash (escape), this project will probably not run on operating systems other than Windows.
