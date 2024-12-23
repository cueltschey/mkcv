import argparse
import yaml
import re

def replace_placeholders(template_text, variables):
    """
    Replace {variable} placeholders in the template_text with values from the variables dictionary.
    """
    pattern = re.compile(r"\{(\w+)\}")
    return pattern.sub(lambda match: variables.get(match.group(1), match.group(0)), template_text)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Replace {variable} placeholders in a text file with values from a YAML file.")
    parser.add_argument("yaml_file", help="Path to the YAML file containing variables.")
    parser.add_argument("template_file", help="Path to the template text file.")
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

    # Replace placeholders and print the result
    result = replace_placeholders(template_text, variables)
    print(result)

if __name__ == "__main__":
    main()

