import os
import glob
import re

# Function to get all files in the specified directory
def get_files(directory):
    """
    Returns a list of all files in the specified directory.
    :param directory: Directory path to scan for files.
    :return: List of file paths.
    """
    return glob.glob(os.path.join(directory, "*"))

# Function to extract file extensions from the list of files
def get_file_extensions(files):
    """
    Extracts unique file extensions from the list of files.
    :param files: List of file paths.
    :return: Set of unique file extensions.
    """
    extensions = set()
    for file in files:
        match = re.search(r".+\.(.+)", file)
        if match:
            extensions.add(match.group(1))
    return extensions

# Function to create directories for each file extension
def create_directories(base_directory, extensions):
    """
    Creates a subdirectory for each file extension.
    :param base_directory: Base directory where subdirectories will be created.
    :param extensions: Set of file extensions.
    """
    for ext in extensions:
        directory = os.path.join(base_directory, f"{ext}_files")
        os.makedirs(directory, exist_ok=True)  # Avoid errors if directory already exists

# Function to move files into their respective directories
def organize_files(files, base_directory):
    """
    Moves files into directories based on their extensions.
    :param files: List of file paths.
    :param base_directory: Base directory containing the files.
    """
    for file in files:
        match = re.search(r".+\.(.+)", file)
        if match:
            ext = match.group(1)
            target_directory = os.path.join(base_directory, f"{ext}_files")
            try:
                os.replace(file, os.path.join(target_directory, os.path.basename(file)))
            except OSError as e:
                print(f"Error moving file {file}: {e}")

# Main function to execute the file organization process
def main():
    """
    Main function to organize files in a user-specified directory.
    """
    base_directory = input("Enter the directory path to organize: ").strip()

    # Check if the directory exists
    if not os.path.exists(base_directory):
        print("The provided directory does not exist.")
        return

    # Get all files in the directory
    files = get_files(base_directory)
    if not files:
        print("No files found in the directory.")
        return

    # Extract unique file extensions
    extensions = get_file_extensions(files)

    # Create directories for each extension
    create_directories(base_directory, extensions)

    # Organize files into respective directories
    organize_files(files, base_directory)

    print("Files have been organized successfully!")

# Run the main function if this script is executed
def __name__ == "__main__":
    main()
