markdown

# Create Project Structure

A Python script to create a directory structure from a text file describing the tree.

## Overview

This script reads a text file describing a directory structure in a tree-like format (similar to the output of the `tree` command) and creates the corresponding directories and files on the filesystem. It supports nested structures, folders, and files, and handles inline comments in the input file.

The script was originally developed to create a specific directory structure for an Obsidian-GitHub project, but it can be used for any project structure defined in a similar format.

## Requirements

- Python 3.x
- Write permissions on the Desktop directory (or modify `base_dir` in the script to another location).

## Usage

1. Save the script as `create_project.py`.
2. Make the script executable:
   ```bash
   chmod +x create_project.py

Run the script:
bash

./create_project.py

Follow the prompts:
Project name: Enter the name of the root directory (e.g., MyProject). The script will create this directory on your Desktop.

Tree structure: Enter either:
A space-separated list of paths (e.g., docs/notes.txt src/code/main.py README.md).

A path to a .txt file containing the tree structure (e.g., Desktop/project_structure.txt).

Example Input
Create a file (e.g., project_structure.txt) with the following content:

MyProject/
├── docs/
│   ├── setup.md
│   └── usage.md
├── src/
│   └── main.py
└── README.md

Run the script:
```bash

./create_project.py
Enter project name: MyProject
Enter tree structure: Desktop/project_structure.txt
```
The script will create the following structure on your Desktop:

MyProject/
├── docs/
│   ├── setup.md
│   └── usage.md
├── src/
│   └── main.py
└── README.md

Installation
Clone this repository:
```bash

git clone https://github.com/[your-username]/create-project-structure.git
```

Navigate to the project directory:
```bash

cd create-project-structure
```
Make the script executable:

```bash

chmod +x create_project.py
```
Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to suggest improvements or report bugs.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Author
infinitimeless
