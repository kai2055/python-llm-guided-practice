"""
This program is a simple practice of python file handling exceptions.

"""

from pathlib import Path





def file_reader(file_path: Path) -> str:

    """
    Read and return the contents of a file.

    Args:
        file_path: Path object pointing to the file to read

    Returns:
        str: Contents of the file

    Raises:
        ValueError: If file_path is empty or None
        FileNotFoundError: If the file doesn't exist
        IsADirectoryError: If the path points to a directory
        PermissionError: If lacking permissions to read the file
        OSError: For other system-related errors opening the file
    """
    # Check for empty/None path
    if not file_path:
        raise ValueError("File path cannot be empty or None")

    # Check if path exists
    if not file_path.exists():
        raise FileNotFoundError(
            f"The file path: {file_path} does not exist. "
            f"Please enter a valid file path.")
    
    # Check if it's a file (not a directory)
    if not file_path.is_file():
        raise IsADirectoryError(
            f"The file path: {file_path} given is a directory."
            "Please enter a path that leads to a file.")
    
    # Opening and reading the file
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            return content
    except PermissionError:
        raise PermissionError(f"Cannot open '{file_path}': Permission denied")
    except OSError as e:
        raise OSError(f"Cannot open 'file_path': {e}")
    
        

    

    





