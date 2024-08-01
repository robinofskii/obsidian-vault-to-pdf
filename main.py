import argparse
import os

from helpers.generic_helpers import checkDependencies
from helpers.markdown_helpers import mergeMarkdownFiles
from helpers.pdf_helpers import convertToPdf
from helpers.user_input_helpers import getUserInput

## Initialize argparse for command line arguments
parser = argparse.ArgumentParser(description="Convert a directory of markdown files into a single PDF file.")
parser.add_argument("--pdf_engine", type=str, help="PDF engine to use (e.g., weasyprint, wkhtmltopdf, pdflatex)")

## Initialize variables for command line arguments
args = parser.parse_args()
pdf_engine = args.pdf_engine or "weasyprint"

try:
    vault_path = getUserInput("Enter the Path to the directory containing markdown files (e.g., ./MyVault):\n")
    folders_to_skip = getUserInput("Enter the folders to skip (comma-separated, e.g., folder1,folder2):\n").split(",") or []
    # exclude .obsidian folder
    folders_to_skip.append(".obsidian")
    if not os.path.isdir(vault_path):
        raise ValueError("Invalid directory path provided.")
    
    pdf_output_path = os.path.join(os.path.basename(vault_path) + ".pdf")

    checkDependencies()
    mergeMarkdownFiles(vault_path, folders_to_skip)
    convertToPdf(pdf_output_path, pdf_engine)
except ValueError as ve:
    print(f"Value Error: {ve}")
except Exception as e:
    print(e)