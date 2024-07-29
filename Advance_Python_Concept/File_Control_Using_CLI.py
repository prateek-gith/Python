import os
import argparse

# Error messages
INVALID_FILETYPE_MSG = "Error: Invalid file format. {} must be a .txt file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path {} does not exist."

def validate_file(file_name):
    """
    Validate file name and path.
    """
    if not valid_path(file_name):
        print(INVALID_PATH_MSG.format(file_name))
        quit()
    elif not valid_filetype(file_name):
        print(INVALID_FILETYPE_MSG.format(file_name))
        quit()

def valid_filetype(file_name):
    # Validate file type
    return file_name.endswith('.txt')

def valid_path(path):
    # Validate file path
    return os.path.exists(path)

def read(args):
    # Get the file name/path
    file_name = args.read[0]

    # Validate the file name/path
    validate_file(file_name)

    # Read and print the file content
    with open(file_name, 'r') as f:
        print(f.read())

def show(args):
    # Get path to directory
    dir_path = args.show[0]

    # Validate path
    if not valid_path(dir_path):
        print("Error: No such directory found.")
        exit()

    # Get text files in directory
    files = [f for f in os.listdir(dir_path) if valid_filetype(f)]
    print(f"{len(files)} text files found.")
    print('\n'.join(f for f in files))

def change_path_Drectory(args):
    # Get path to directory
    dir_path = args.chdir[0]

    # Validate path
    if not valid_path(dir_path):
        print("Error: No such directory found.")
        exit()

    # Change Path Dicectory 
    os.chdir(dir_path)
    print(f"Current Path Is {dir_path}")
    print(os.getcwd())

def delete(args):
    # Get the file name/path
    file_name = args.delete[0]

    # Validate the file name/path
    validate_file(file_name)

    # Delete the file
    os.remove(file_name)
    print(f"Successfully deleted {file_name}.")

def copy(args):
    # File to be copied
    file1 = args.copy[0]
    # File to copy upon
    file2 = args.copy[1]

    # Validate the file to be copied
    validate_file(file1)

    # Validate the type of file 2
    if not valid_filetype(file2):
        print(INVALID_FILETYPE_MSG.format(file2))
        exit()

    # Copy file1 to file2
    with open(file1, 'r') as f1:
        with open(file2, 'w') as f2:
            f2.write(f1.read())
    print(f"Successfully copied {file1} to {file2}.")

def rename(args):
    # Old file name
    old_filename = args.rename[0]
    # New file name
    new_filename = args.rename[1]

    # Validate the file to be renamed
    validate_file(old_filename)

    # Validate the type of new file name
    if not valid_filetype(new_filename):
        print(INVALID_FILETYPE_MSG.format(new_filename))
        exit()

    # Renaming
    os.rename(old_filename, new_filename)
    print(f"Successfully renamed {old_filename} to {new_filename}.")

def main():
    # Create parser object
    parser = argparse.ArgumentParser(description="A text file manager!")

    # Defining arguments for parser object
    parser.add_argument("-r", "--read", type=str, nargs=1,
                        metavar="file_name", default=None,
                        help="Opens and reads the specified text file.")
    
    parser.add_argument("-s", "--show", type=str, nargs=1,
                        metavar="path", default=None,
                        help="Shows all the text files in the specified directory path. Type '.' for current directory.")
    
    parser.add_argument("-d", "--delete", type=str, nargs=1,
                        metavar="file_name", default=None,
                        help="Deletes the specified text file.")
    
    parser.add_argument("-c", "--copy", type=str, nargs=2,
                        metavar=('file1', 'file2'),
                        help="Copy file1 contents to file2. Warning: file2 will be overwritten.")
    
    parser.add_argument("--rename", type=str, nargs=2,
                        metavar=('old_name', 'new_name'),
                        help="Renames the specified file to a new name.")
    
    parser.add_argument("--chdir", type=str, nargs=1,
                        metavar="path",
                        help="Change Directory the specified file to a new name.")

    # Parse the arguments from standard input
    args = parser.parse_args()

    # Calling functions depending on the type of argument
    if args.read:
        read(args)
    elif args.show:
        show(args)
    elif args.delete:
        delete(args)
    elif args.copy:
        copy(args)
    elif args.rename:
        rename(args)
    elif args.chdir:
        change_path_Drectory(args)

if __name__ == "__main__":
    # Calling the main function
    main()
