# CodeToText - Project Exporter

## Description

CodeToText is a tool designed to export the structure and content of a programming project directory or a GitHub repository. It processes the directory tree or GitHub repository and generates a detailed report in a text file, excluding files and directories specified in a `.gitignore` file.

## Requirements

- Python 3.x
- requests library (for GitHub support)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/caguevara11/CodeToText.git
   cd CodeToText
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On