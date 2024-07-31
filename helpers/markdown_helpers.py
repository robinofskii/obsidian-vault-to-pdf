import os

from helpers.generic_helpers import doesFileExist

def combine_files(vault_path, output_path, folders_to_skip=[]):
    """
    Combines all markdown files in the specified vault path into a single file.

    Args:
        vault_path (str): The path to the directory containing the markdown files.
        output_path (str): The path to the output file where the combined markdown will be saved.

    Returns:
        None
    """
    if doesFileExist(output_path):
        os.remove(output_path)
    with open(output_path, "w") as output:
        for root, dirs, files in os.walk(vault_path):
            # Skip folders specified in the command line arguments
            dirs[:] = [d for d in dirs if d not in folders_to_skip]
            for file in files:
                if file.endswith(".md"):
                    with open(os.path.join(root, file), "r") as input:
                        output.write(input.read())
                        output.write("\n\n")
    print(f"Markdown files combined into {output_path}")