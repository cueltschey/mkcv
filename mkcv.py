import argparse
import yaml
import re
from markdown import markdown
from weasyprint import HTML
import pathlib

def replace_placeholders(template_text, variables):
    """
    Replace {variable} placeholders in the template_text with values from the variables dictionary.
    """
    pattern = re.compile(r"\{(\w+)\}")
    return pattern.sub(lambda match: variables.get(match.group(1), match.group(0)), template_text)

def convert_md_to_pdf(md_content, pdf_file):
    """
    Convert Markdown content to a PDF file.
    """
    # Convert Markdown to HTML
    html_content = markdown(md_content)

    # Convert HTML to PDF
    HTML(string=html_content).write_pdf(pdf_file)
    print(f"PDF successfully created: {pdf_file}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Replace {variable} placeholders in a text file and convert to PDF.")
    parser.add_argument("-y", "--yaml_file", required=True, help="Path to the YAML file containing variables.", type=pathlib.Path)
    parser.add_argument("-t", "--template_file", required=True, help="Path to the template text file.", type=pathlib.Path)
    parser.add_argument("-o", "--pdf_output", required=True, help="Path to the output PDF file.", type=pathlib.Path)
    args = parser.parse_args()

    # Load variables from the YAML file
    try:
        with open(args.yaml_file, "r") as file:
            variables = yaml.safe_load(file)
    except Exception as e:
        print(f"Error reading YAML file: {e}")
        return

    # Load the template text
    try:
        with open(args.template_file, "r") as file:
            template_text = file.read()
    except Exception as e:
        print(f"Error reading template file: {e}")
        return

    # Replace placeholders in the template text
    result = replace_placeholders(template_text, variables)

    # Convert the result to a PDF
    try:
        convert_md_to_pdf(result, args.pdf_output)
    except Exception as e:
        print(f"Error generating PDF: {e}")

if __name__ == "__main__":
    main()

