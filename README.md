
# Create Project Structure

A Python script to create a directory structure from a text file describing the tree.

## Overview

This script reads a text file describing a directory structure in a tree-like format (similar to the output of the `tree` command) and creates the corresponding directories and files on the filesystem. It supports nested structures, folders, and files, and handles inline comments in the input file.

The script was originally developed to create a specific directory structure for an Obsidian-GitHub project, but it can be used for any project structure defined in a similar format.

## Requirements

- Python 3.x
- Write permissions on the Desktop directory (or modify `base_dir` in the script to another location).

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/[your-username]/create-project-structure.git
   ```
Navigate to the project directory:
```bash
cd create-project-structure
```
Add your tree project structure .txt file to the 'create-project-structure' folder (place it in the root of the repository). For example, if your tree structure file .txt is named name_of_this_tree_structure_file.txt, copy it to the create-project-structure/ directory:
```bash
cp /path/to/name_of_this_tree_structure_file.txt create-project-structure/
```
Make the script executable:
```bash
chmod +x create_project.py
```
Run the script:
```bash
./create_project.py
```
Follow the prompts:
1. Project name: Enter the name of the root directory (e.g., xxxxxx). The script will create this directory on your Desktop (e.g., ~/Desktop/xxxxxx/).

2. Tree structure: Enter the name of your tree structure file located in the create-project-structure/ directory (e.g., name_of_this_tree_structure_file.txt). 

## Installation
Clone this repository:
```bash
git clone https://github.com/[your-username]/create-project-structure.git
````
Navigate to the project directory:
```bash
cd create-project-structure
```
Make the script executable:
```bash
chmod +x create_project.py
```
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to suggest improvements or report bugs.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Author
infinitimeless
