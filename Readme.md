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

By calling the program to change these files with the basename barcelona042421. 
The files will be renamed to:
<br>barceonaDDMMYYYY_1.jpg
<br>barceonaDDMMYYYY_2.jpg
<br>barceonaDDMMYYYY_3.jpg
<br>barceonaDDMMYYYY_4.jpg

## Setup

To run this project install Python 3.9 on your machine:
$ cd ../file-rename
$ python main.py

## Warning

This project was created on a Windows machine, no guarentee that the program will run without errors on other operatingsystems, because of the different path names.
