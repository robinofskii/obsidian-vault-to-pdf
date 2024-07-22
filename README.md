# Markdown to PDF Converter

## Table of Contents

- [Markdown to PDF Converter](#markdown-to-pdf-converter)
  - [Table of Contents](#table-of-contents)
  - [About ](#about-)
  - [Getting Started ](#getting-started-)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
  - [Usage ](#usage-)

## About <a name = "about"></a>

This project provides a simple Python script, [`markdown-to-pdf.py`](./markdown-to-pdf.py), that combines multiple Markdown files into a single PDF document. This is used here to export an entire [Obsidian](https://obsidian.md/) vault to one, single `.pdf` file. The script uses [Pandoc](https://pandoc.org/) and a PDF engine ([WeasyPrint](https://weasyprint.org/) by default) to generate the PDF.

I'm not proficient in Python, since Typescript is my main language, so I'm not sure if this is the best way to do this. I'm open to suggestions and improvements.

## Getting Started <a name = "getting_started"></a>

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the script, you need to have Python installed on your system along with the following dependencies:

- [Pandoc](https://pandoc.org/)
- [WeasyPrint](https://weasyprint.org/)

You can install them using your system's package manager or by following the instructions on their respective websites.

### Installing

1. Clone the repository to your local machine.
2. Ensure you have the required dependencies installed by running:

   ```bash
   pandoc --version
   weasyprint --version
   ```

   If the commands return version information, the dependencies are installed correctly.

3. Install the required dependencies using `brew`:

   ```bash
   brew install pandoc
   brew install weasyprint
   ```

4. Navigate to the project directory and run the script with Python:

   ```bash
   python markdown-to-pdf.py
   ```

## Usage <a name = "usage"></a>

To use the script, simply run it from the command line. The script is configured to search for Markdown files in the `vault_path` directory, combine them into a single Markdown file (`md_output_path`), and then convert this combined Markdown file into a PDF (`pdf_output_path`) using [Pandoc](https://pandoc.org/) and [WeasyPrint](https://weasyprint.org/).

You can modify the `vault_path`, `md_output_path`, `pdf_output_path`, `pdf_engine`, and `pdf_title` variables in the script to customize the input directory, intermediate Markdown file path, output PDF path, PDF engine, and PDF title, respectively.

I personally use this script to export my entire Obsidian vault to a single PDF file. I then use this PDF as a source file for chatGPT to help answer questions about my notes. The script is designed to work with Obsidian vaults, but you it can to work with any directory containing Markdown files.
