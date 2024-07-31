import os
import subprocess

from helpers.generic_helpers import doesFileExist

def convertToPdf(pdf_output_path, pdf_engine):
    """
    Generate a PDF file from a combined markdown file.

    Args:
        md_output_path (str): The path to the combined markdown file.
        pdf_output_path (str): The path to save the generated PDF file.
        pdf_engine (str): The PDF engine to use for generating the PDF.

    Raises:
        Exception: If the combined markdown file does not exist or if there is an error creating the PDF.

    Returns:
        None
    """
    md_output_path = "combined_markdown.md"
    
    if not doesFileExist(md_output_path):
        raise Exception("Combined markdown file does not exist.")
    if doesFileExist(pdf_output_path):
        os.remove(pdf_output_path)

    pdf_title = os.path.splitext(os.path.basename(pdf_output_path))[0]
    
    result = subprocess.run(["pandoc", md_output_path, "-o", pdf_output_path, "--pdf-engine", pdf_engine, "--metadata", f"title={pdf_title}", "--from" ,"markdown-yaml_metadata_block"])
    if result.returncode != 0 or not doesFileExist(pdf_output_path):
        raise Exception("Error creating PDF")
    print(f"PDF created successfully: {pdf_output_path}")
    print("Removing combined markdown file...")
    os.remove(md_output_path)
