import os
import subprocess
import argparse

## Initialize argparse for command line arguments
parser = argparse.ArgumentParser(description="Convert a directory of markdown files into a single PDF file.")
parser.add_argument("--pdf_engine", type=str, help="PDF engine to use (e.g., weasyprint, wkhtmltopdf, pdflatex)")
parser.add_argument("--skip_folders", type=str, help="Comma-separated list of folders to skip (e.g., folder1,folder2)")

## Add required arguments
args = parser.parse_args()

## Initialize variables
pdf_engine = parser.parse_args().pdf_engine or "weasyprint"
folders_to_skip = parser.parse_args().skip_folders.split(",") if parser.parse_args().skip_folders else []

def doesFileExist(filePath):
    return os.path.exists(filePath)

def validateDependencies():
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

def combine_files(vault_path, output_path):
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

def generate_pdf(md_output_path, pdf_output_path):
    """
    Generate a PDF file from a combined markdown file.

    Args:
        md_output_path (str): The path to the combined markdown file.
        pdf_output_path (str): The path to save the generated PDF file.

    Raises:
        Exception: If the combined markdown file does not exist or if there is an error creating the PDF.

    Returns:
        None
    """
    if not doesFileExist(md_output_path):
        raise Exception("Combined markdown file does not exist.")
    if doesFileExist(pdf_output_path):
        os.remove(pdf_output_path)

    pdf_title = os.path.splitext(os.path.basename(pdf_output_path))[0]
    
    print(f"Creating PDF using {pdf_engine}...")
    print(f"Title: {pdf_title}")
    print(f"Output Path: {pdf_output_path}")
    print(f"Markdown Path: {md_output_path}")
    
    result = subprocess.run(["pandoc", md_output_path, "-o", pdf_output_path, "--pdf-engine", pdf_engine, "--metadata", f"title={pdf_title}", "--from" ,"markdown-yaml_metadata_block"])
    if result.returncode != 0 or not doesFileExist(pdf_output_path):
        raise Exception("Error creating PDF")
    print(f"PDF created successfully: {pdf_output_path}")

try:
    vault_path = input("Enter the Path to the directory containing markdown files (e.g., ./MyVault): ")
    md_output_path = input("Enter the name of the output markdown file (e.g., combined.md): ")
    pdf_output_path = input("Enter the name of the output PDF file (e.g., combined.pdf): ")

    validateDependencies()
    combine_files(vault_path, md_output_path)
    generate_pdf(md_output_path, pdf_output_path)
except Exception as e:
    print(e)