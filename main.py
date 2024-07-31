import argparse

from helpers.generic_helpers import checkDependencies
from helpers.markdown_helpers import mergeMarkdownFiles
from helpers.pdf_helpers import convertToPdf
from helpers.user_input_helpers import getUserInput

## Initialize argparse for command line arguments
parser = argparse.ArgumentParser(description="Convert a directory of markdown files into a single PDF file.")
parser.add_argument("--pdf_engine", type=str, help="PDF engine to use (e.g., weasyprint, wkhtmltopdf, pdflatex)")
parser.add_argument("--skip_folders", type=str, help="Comma-separated list of folders to skip (e.g., folder1,folder2)")

## Add required arguments
args = parser.parse_args()

## Initialize variables
pdf_engine = parser.parse_args().pdf_engine or "weasyprint"
folders_to_skip = parser.parse_args().skip_folders.split(",") if parser.parse_args().skip_folders else []

try:
    vault_path = getUserInput("Enter the Path to the directory containing markdown files (e.g., ./MyVault): ")
    md_output_path = getUserInput("Enter the name of the output markdown file (e.g., combined.md): ")
    pdf_output_path = getUserInput("Enter the name of the output PDF file (e.g., combined.pdf): ")

    checkDependencies()
    mergeMarkdownFiles(vault_path, md_output_path, folders_to_skip)
    convertToPdf(md_output_path, pdf_output_path, pdf_engine)
except Exception as e:
    print(e)