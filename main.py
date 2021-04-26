"""This main module calls the helper functions in the main-function, such that the right files in the right folder are changed."""
import os
from helperfunctions import ask_input_for_path, ask_input_base_filename, files_ending_with_chars

def main():
    """Main function to call the helper functions and 
    rename the files at the destination"""
    path = ask_input_for_path()
    base_filename = ask_input_base_filename()

    file_end = files_ending_with_chars()

    for count, filename in enumerate(os.listdir(path)):
        if file_end is None or filename.endswith(file_end):
            file_extension = filename.split('.')[-1]
            full_name = f"{base_filename}_{count}.{file_extension}"
            source = path + filename # Actual name of the file
            destination = path + full_name # New name of the file
            os.rename(source, destination) #rename function will rename the files
    print(f"The filenames are changed. End of script")
if __name__ == '__main__':
    main() # Calling main() function
