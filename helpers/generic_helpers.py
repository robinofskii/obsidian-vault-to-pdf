import os
import subprocess

def doesFileExist(filePath):
    """
    Check if a file exists at the given file path.

    Args:
        filePath (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(filePath)

def checkDependencies():
    """
    Checks if the required dependencies are installed.

    This function checks if the dependencies 'pandoc' and 'weasyprint' are installed on the system.
    If any of the dependencies are not installed, it raises an exception with an appropriate error message.

    Raises:
        Exception: If any of the dependencies are not installed.
        
    Returns:
        None
    """
    dependencies = {"pandoc": "--version", "weasyprint": "--version"}
    for dep, arg in dependencies.items():
        if subprocess.run([dep, arg], stdout=subprocess.PIPE).returncode != 0:
            raise Exception(f"{dep} is not installed. Please install it before running this script.")