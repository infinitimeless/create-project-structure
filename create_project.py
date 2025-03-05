#!/usr/bin/env python3

import os
import re
import shutil

# Prompt for project name
project_name = input("Enter project name: ")

# Prompt for tree structure in one shot (space-separated or file path)
tree_input = input("Enter tree structure (space-separated, e.g., docs/notes.txt src/code/main.py README.md, or path to .txt file): ").strip()

# Create project directory on Desktop
base_dir = os.path.join(os.path.expanduser("~/Desktop"), project_name)

# Clear the project directory if it exists to avoid conflicts
if os.path.exists(base_dir):
    shutil.rmtree(base_dir)
os.makedirs(base_dir, exist_ok=True)

# Process tree structure
if os.path.isfile(tree_input):
    with open(tree_input, 'r') as f:
        lines = f.read().splitlines()
    first_line = True
    levels = {}  # Dictionary to track the last entry at each indentation level

    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
        # Preserve the original line for folder/file detection
        original_line = line
        # Debug: Print the original line
        print(f"Original line: '{original_line}'")
        # Remove comments before checking for folder
        if '#' in original_line:
            folder_check_line = original_line[:original_line.index('#')].rstrip()
        else:
            folder_check_line = original_line.rstrip()
        # Determine if it's a folder (ends with /)
        is_folder = folder_check_line.endswith('/')
        # Handle comments (remove everything after # but keep the path)
        if '#' in line:
            line = line[:line.index('#')].rstrip()
        # Skip the first line if it matches the project name
        if first_line:
            first_line = False
            if line.strip().startswith(project_name + "/"):
                continue
        # Determine indentation level by counting leading spaces
        indent_match = re.match(r'^(.*?)(?:└──|├──)', line)
        if indent_match:
            indent_str = indent_match.group(1)
            # Count the number of spaces, treating │ as a space
            indentation = len(indent_str.replace('│', ' ')) // 2  # 2 spaces per level
        else:
            indentation = 0
        # Extract the folder/file name
        cleaned_name = re.sub(r'[│├──└──]+', '', original_line)
        if '#' in cleaned_name:
            cleaned_name = cleaned_name[:cleaned_name.index('#')]
        cleaned_name = cleaned_name.strip()
        cleaned_name = cleaned_name.strip('/')
        if not cleaned_name:
            continue
        # Debug: Print the processed line
        print(f"Processing: indentation={indentation}, cleaned_name={cleaned_name}, is_folder={is_folder}")
        # Build the path based on indentation
        # Start with an empty path stack for the current entry
        path_stack = []
        # Add parent entries from levels up to the current indentation
        for i in range(indentation):
            if i in levels:
                path_stack.append(levels[i])
        # Add the current entry
        path_stack.append(cleaned_name)
        # Update the levels dictionary with the current entry
        levels[indentation] = cleaned_name
        # Clear levels at higher indentation to start a new branch
        levels = {k: v for k, v in levels.items() if k <= indentation}
        # Build the current path by joining the stack
        current_path = '/'.join(path_stack)
        # Debug: Print the current path
        print(f"Current path: {current_path}")
        # Create the folder or file
        full_path = os.path.join(base_dir, current_path)
        try:
            if is_folder:
                os.makedirs(full_path, exist_ok=True)
                print(f"Created directory: {full_path}")
            else:
                # Ensure all parent paths are directories
                parent_dir = os.path.dirname(full_path)
                if parent_dir and os.path.exists(parent_dir) and not os.path.isdir(parent_dir):
                    os.remove(parent_dir)  # Remove file if it exists
                    os.makedirs(parent_dir, exist_ok=True)
                else:
                    os.makedirs(parent_dir, exist_ok=True)
                with open(full_path, 'a'):
                    os.utime(full_path, None)
                print(f"Created file: {full_path}")
        except Exception as e:
            print(f"Error creating {full_path}: {e}")
            continue
else:
    for path in tree_input.split():
        if path.strip():
            full_path = os.path.join(base_dir, path.strip())
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            if '.' in os.path.basename(path):
                with open(full_path, 'a'):
                    os.utime(full_path, None)
            else:
                os.makedirs(full_path, exist_ok=True)

print(f"Created project '{project_name}' at {base_dir}")