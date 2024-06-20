# ./tests/test_project_exporter.py
import pytest
from exporter.main import ProjectExporter
from tests.test_common import create_test_project, common_test_empty_directory, common_test_nested_directories, common_test_mixed_content

@pytest.fixture
def project_exporter():
    return ProjectExporter()

def test_export_project_structure_and_contents(project_exporter, create_test_project):
    project_path = create_test_project({"test_file.py": "print('Hello World')"})

    structure, contents = project_exporter.export(project_path)
    assert './' in structure
    assert '├── test_file.py' in structure
    assert f"{project_path}/test_file.py:\n```py\nprint('Hello World')\n```\n" in contents

def test_integration_with_ignore_parser_and_file_handler(project_exporter, create_test_project):
    project_path = create_test_project({
        "test_file.py": "print('Hello World')",
        ".gitignore": "*.pyc\n__pycache__/\n"
    })

    structure, contents = project_exporter.export(project_path)
    assert './' in structure
    assert '├── test_file.py' in structure
    assert "*.pyc" not in structure
    assert "__pycache__/" not in structure

def test_empty_project(project_exporter, tmpdir):
    common_test_empty_directory(project_exporter.export, tmpdir)

def test_nested_directories(project_exporter, create_test_project):
    common_test_nested_directories(project_exporter.export, create_test_project)

def test_mixed_content(project_exporter, create_test_project):
    common_test_mixed_content(project_exporter.export, create_test_project)
