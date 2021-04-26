"""The helperfunctions of the file-renamer project"""
import os
import contextlib


def ask_input_for_path():
    """This function asks for a path in which
        you want to change filenames and changes
        the current workdirectory to this path
        Input None, return path"""
    while True:
        path = input('In which path do you want to rename files?: ')
        try:
            os.chdir(path)
        except FileNotFoundError:
            print("This path does not exist. Try again")
            continue
        break
    # function adds a backslash if necessary
    path = path_ends_on_backslash(path)
    return path


def path_ends_on_backslash(path):
    """In case the input of the user does not end on a backslash
    the backslash is added to the path"""
    if path[-1] != '\\':
        path += '\\'
    return path


def ask_input_base_filename():
    """This functions asks for base filename
    for all files that you want to change in
    a specified directory. Input None, returns base filename"""
    return input("What base filename do you want to give the files?: ")


def files_ending_with_chars():
    """Function asks input for file names to end with specific characters."""
    if input('Do you want to selected specific filenames?: yes/no ') == 'yes':
        return input('What do you want the file to end with?: ')
    return None


def change_destination_files():
    """Function to change the destination of the files"""
    # TO-DO


def files_containing_chars():
    """Function to filter on files that contain a certain character(s)"""
    # TO-DO


def files_starting_with_chars():
    """Function toe filter on files that start with certain character(s)"""
    # TO-DO
