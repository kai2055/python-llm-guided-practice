

# Write save_config and load_config
# both handle missing files and bad JSON gracefully



import json
from pathlib import Path
import csv


def save_config(config: dict, path: Path) -> bool:
    """
    Saves a dictionary as JSON to the specified field path.

    Args: 
        config (dict): Dictionary to save as JSON
        path (Path): File path where JSON will be written


    Returns:
        bool: True if save suceeded, False if an error occured

    Raises: 
        OSError: If file cannot be written (permission denied, disk full etc.)
    """

    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)
        return True
    except OSError as e:
        print(f"Error writing to File: {e}")
        return False
    


def load_config(path: Path) -> dict:
    """
    Loads and returns a JSON dictionary from the specified file path.

    Args:
        path (Path): File path to read JSON from


    Returns:
        dict: Loaded dictionary from JSON, or empty dict if file missing or malformed

    Raises:
        FileNotFoundError: If file does not exist (caught and handled)
        json.JSONDecodeError: If file contains invalid JSON (caught and handled)
    """

    try:
        with open(path, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        return loaded
    except FileNotFoundError:
        print(f"File not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Malformed JSON: {e}")
        return {}




def append_log(path: Path, entry) -> bool:
    """
    Appends a log entry as a JSON line to a file.

    Args:
        path (Path): File path to append the log entry
        entry (any): Data to be logged (dict, list, str, int, etc)
    
    Returns:
        bool: True if append succeeded, False if an error occured.

    Raises:
        OSError: If file cannot be written (caught and handled)
    """
    try:
        with open(path, "a", encoding="utf-8") as f:
            json.dump(entry, f, separators=(',', ':'))
            f.write("\n")
        return True
    except OSError as e:
        print(f"Error writing to file: {e}")
        return False
    





def csv_to_json(csv_path: Path, json_path:Path) -> bool:
    """
    Reads a CSV file and writes contents to a JSON file as a list of dicts.

    Args:
        csv_path (Path): Path to input CSV filr
        json_path (Path): Path to output JSON file

    Returns:
        bool: True if sucessful, False if error eccoured

    Raises:
        FileNotFoundError: If CSV file doesn't exist
        csv.Error: If CSV is malformed

    """

    try:
        with open(csv_path, "r", newline="", encoding="utf-8") as f1, \
            open(json_path, "w", encoding="utf-8") as f2:

            reader = csv.DictReader(f1)
            data = list(reader)
            json.dump(data, f2, indent=2)

        return True
    except (FileNotFoundError, csv.Error, OSError) as e:
        print(f"Error: {e}")
        return False
    
            

    



