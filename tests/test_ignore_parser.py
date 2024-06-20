import os
import pytest
from exporter.ignore_parser import IgnoreParser

@pytest.fixture
def ignore_parser():
    return IgnoreParser()

@pytest.fixture
def create_gitignore(tmpdir):
    def _create_ignore_file(file_name, rules):
        test_dir = tmpdir.mkdir("test_project")
        ignore_file = test_dir.join(file_name)
        ignore_file.write("\n".join(rules))
        return str(test_dir)
    return _create_ignore_file

def test_parse_standard_gitignore(ignore_parser, create_gitignore):
    project_path = create_gitignore(".gitignore", ["*.pyc", "__pycache__/"])

    ignore_list = ignore_parser.parse_gitignore(project_path)
    assert "*.pyc" in ignore_list
    assert "__pycache__/" in ignore_list

def test_fallback_to_default_gitignore(ignore_parser, tmpdir):
    test_dir = tmpdir.mkdir("test_project")

    ignore_list = ignore_parser.parse_gitignore(str(test_dir))
    assert ".vscode/" in ignore_list
    assert "*.pyc" in ignore_list

def test_handle_comments_and_empty_lines(ignore_parser, create_gitignore):
    project_path = create_gitignore(".gitignore", ["# Comment line", "", "*.pyc", "", "__pycache__/"])

    ignore_list = ignore_parser.parse_gitignore(project_path)
    assert "*.pyc" in ignore_list
    assert "__pycache__/" in ignore_list
    assert "# Comment line" not in ignore_list
    assert "" not in ignore_list

def test_combined_ignore_rules(ignore_parser, tmpdir):
    test_dir = tmpdir.mkdir("test_project")
    gitignore_file = test_dir.join(".gitignore")
    gitignore_file.write("*.pyc\n")
    default_gitignore_file = os.path.join(os.path.dirname(__file__), '..', '.default_gitignore')

    ignore_list = ignore_parser.parse_gitignore(str(test_dir))
    assert "*.pyc" in ignore_list
    with open(default_gitignore_file, 'r') as f:
        for line in f:
            rule = line.strip()
            if rule and not rule.startswith('#'):
                assert rule in ignore_list

def test_missing_gitignore(ignore_parser, tmpdir):
    test_dir = tmpdir.mkdir("test_project")
    ignore_list = ignore_parser.parse_gitignore(str(test_dir))
    assert ".vscode/" in ignore_list
    assert "*.pyc" in ignore_list

