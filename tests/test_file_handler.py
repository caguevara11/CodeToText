# ./tests/test_file_handler.py
import pytest
from exporter.file_handler import FileHandler
from tests.test_common import create_test_project, common_test_empty_directory, common_test_nested_directories, common_test_mixed_content

@pytest.fixture
def file_handler():
    return FileHandler()

def test_generate_structure_no_ignored_files(file_handler, create_test_project):
    project_path = create_test_project({"test_file.py": "print('Hello World')"})

    structure, contents = file_handler.generate_project_structure(project_path, [])
    assert './' in structure
    assert '├── test_file.py' in structure
    assert f"{project_path}/test_file.py:\n```py\nprint('Hello World')\n```\n" in contents

def test_generate_structure_with_ignored_files(file_handler, create_test_project):
    project_path = create_test_project({"test_file.py": "print('Hello World')"})

    structure, contents = file_handler.generate_project_structure(project_path, ['test_file.py'])
    assert './' in structure
    assert 'test_file.py' not in structure

def test_handle_different_file_encodings(file_handler, create_test_project):
    project_path = create_test_project({
        "utf8_file.txt": "utf-8 text",
        "latin1_file.txt": "latin-1 text".encode("latin-1")
    })

    structure, contents = file_handler.generate_project_structure(project_path, [])
    assert 'utf8_file.txt' in structure
    assert 'latin1_file.txt' in structure
    assert f"{project_path}/utf8_file.txt:\n```txt\nutf-8 text\n```\n" in contents
    assert f"{project_path}/latin1_file.txt:\n```txt\nlatin-1 text\n```\n" in contents

def test_should_ignore(file_handler):
    assert file_handler._should_ignore('path/to/file.pyc', ['*.pyc'])
    assert file_handler._should_ignore('path/to/dir/', ['dir/'])
    assert not file_handler._should_ignore('path/to/file.py', ['*.pyc'])
    assert not file_handler._should_ignore('path/to/another_dir/', ['dir/'])
    assert file_handler._should_ignore('path/to/specific_file.py', ['specific_file.py'])
    assert file_handler._should_ignore('path/to/specific_dir/', ['specific_dir/'])

def test_empty_directory(file_handler, tmpdir):
    common_test_empty_directory(file_handler.generate_project_structure, tmpdir, needs_ignore_list=True)

def test_nested_directories(file_handler, create_test_project):
    common_test_nested_directories(file_handler.generate_project_structure, create_test_project, needs_ignore_list=True)

def test_mixed_content(file_handler, create_test_project):
    common_test_mixed_content(file_handler.generate_project_structure, create_test_project, needs_ignore_list=True)
