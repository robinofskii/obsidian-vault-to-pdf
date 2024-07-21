import os
import subprocess

vault_path = "" # Path to the directory containing markdown files (e.g., ./MyVault)
md_output_path = "" # Path to the combined markdown file (e.g. ./combined.md)
pdf_output_path = "" # Path to the output PDF file (e.g., ./combined.pdf)
pdf_engine = "weasyprint" # PDF engine to use (e.g., weasyprint, wkhtmltopdf, pdflatex)
pdf_title = "" # Title of the PDF file (e.g., My Vault)

def doesFileExist(filePath):
    return os.path.exists(filePath)

def validateDependencies():
    dependencies = {"pandoc": "--version", "weasyprint": "--version"}
    for dep, arg in dependencies.items():
        if subprocess.run([dep, arg], stdout=subprocess.PIPE).returncode != 0:
            raise Exception(f"{dep} is not installed. Please install it before running this script.")

def combine_files(vault_path, output_path):
    if doesFileExist(output_path):
        os.remove(output_path)
    with open(output_path, "w") as output:
        for root, dirs, files in os.walk(vault_path):
            for file in files:
                if file.endswith(".md"):
                    with open(os.path.join(root, file), "r") as input:
                        output.write(input.read())
                        output.write("\n\n")
    print(f"Markdown files combined into {output_path}")

def generate_pdf(md_output_path, pdf_output_path):
    if not doesFileExist(md_output_path):
        raise Exception("Combined markdown file does not exist.")
    if doesFileExist(pdf_output_path):
        os.remove(pdf_output_path)
    result = subprocess.run(["pandoc", md_output_path, "-o", pdf_output_path, "--pdf-engine", pdf_engine, "--metadata", f"title={pdf_title}"])
    if result.returncode != 0 or not doesFileExist(pdf_output_path):
        raise Exception("Error creating PDF")
    print(f"PDF created successfully: {pdf_output_path}")

try:
    validateDependencies()
    combine_files(vault_path, md_output_path)
    generate_pdf(md_output_path, pdf_output_path)
except Exception as e:
    print(e)