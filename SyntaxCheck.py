"""
    License:    GPLv3, 2024.11.22
    Version:    0.3
    Author:     Sri-Arjuna, Switzerland
    Source:     https://github.com/sri-arjuna/SD-DynPrompt-SyntaxCheck
"""
#
#   Imports
#
import os
import re

#
#   Functions
#
def check_syntax(file_path, line_number, line_content):
    """
    Check the syntax of a line of text based on specified rules.
    """
    # Pattern to detect {<num>-<num>$$} without enclosing {{ }}
    pattern = r'(?<!{{)\{\d+-\d+\$\$(?!}})'

    # Check the line for pattern
    if re.search(pattern, line_content):

        # Check if opening '{{' is missing
        if not re.search(r'\{\{', line_content):
            print(f"Unmatched double-braces in file '{file_path}' at line {line_number}")

        # Check if closing '}}' is missing
        if not re.search(r'\}\}', line_content):
            print(f"Unmatched double-braces in file '{file_path}' at line {line_number}")

        # Check for balanced '{{' and '}}'
        open_braces = line_content.count('{{')
        close_braces = line_content.count('}}')
        if open_braces != close_braces:
            print(f"Unmatched double-braces in file '{file_path}' at line {line_number}")

    # Check for unmatched braces
    open_braces = line_content.count('{')
    close_braces = line_content.count('}')
    if open_braces != close_braces:
        print(f"Unmatched braces in file '{file_path}' at line {line_number}")

    # Check for unmatched double underscores
    underscore_pairs = line_content.count('__')
    if underscore_pairs % 2 != 0:
        print(f"Unmatched '__' in file '{file_path}' at line {line_number}")

def process_files(root_dir):
    """
    Recursively check all .txt files in the directory for syntax issues.
    """
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line_content in enumerate(f, start=1):
                        check_syntax(file_path, line_number, line_content)

#
#   Handler
#
if __name__ == "__main__":
    root_dir = os.getcwd()
    process_files(root_dir)
    print("Syntax check completed.")
