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
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the exporter, run the `main.py` script with your project's path as an argument:

```bash
python main.py <project_path>
```

For example:

```bash
python main.py /path/to/your/project
```

This will generate a `project_structure.txt` file at the root of the specified project, containing the project's structure and contents (code).

## Project Structure

```
./
├── requirements.txt
├── main.py
├── exporter/
│   ├── __init__.py
│   ├── file_handler.py
│   ├── github_handler.py
│   ├── ignore_parser.py
│   ├── main.py
```

## File Descriptions

- **main.py**: The main script to run the exporter.
- **exporter/**: Contains the core modules of the exporter.
  - **file_handler.py**: Generates the project's structure and reads file contents.
  - **ignore_parser.py**: Parses the `.gitignore` file to get exclusion patterns.
  - **main.py**: Implements the `ProjectExporter` class that coordinates the export operations.

## Testing

To run the tests, use `pytest`:

```bash
pytest
```

The tests are organized into several files to cover different components of the system:

- **test_file_handler.py**: Tests for `FileHandler`.
- **test_ignore_parser.py**: Tests for `IgnoreParser`.
- **test_project_exporter.py**: Integration tests for `ProjectExporter`.
- **test_main.py**: Tests for the `main.py` script.

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License

This project is licensed under the GNU 3 License. See the [LICENSE](LICENSE) file for details.
