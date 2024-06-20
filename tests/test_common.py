# ./tests/test_common.py
import pytest

@pytest.fixture
def create_test_project(tmpdir):
    def _create_project(structure):
        base_dir = tmpdir.mkdir("test_project")
        for path, content in structure.items():
            file = base_dir.join(path)
            file.dirpath().ensure(dir=True)  # Ensure all intermediate directories are created
            file.write(content)
        return str(base_dir)
    return _create_project

def common_test_empty_directory(export_func, tmpdir, needs_ignore_list=False):
    test_dir = tmpdir.mkdir("empty_project")

    if needs_ignore_list:
        structure, contents = export_func(str(test_dir), [])
    else:
        structure, contents = export_func(str(test_dir))

    assert './' in structure
    assert len(structure.strip().split('\n')) == 1  # Only the root directory
    assert contents == ''

def common_test_nested_directories(export_func, create_test_project, needs_ignore_list=False):
    project_path = create_test_project({
        "dir1/dir2/dir3/test_file.py": "print('Hello Nested World')"
    })

    if needs_ignore_list:
        structure, contents = export_func(project_path, [])
    else:
        structure, contents = export_func(project_path)

    assert './' in structure
    assert '├── dir1/' in structure
    assert '│   ├── dir2/' in structure
    assert '│   │   ├── dir3/' in structure
    assert '│   │   │   ├── test_file.py' in structure
    assert f"{project_path}/dir1/dir2/dir3/test_file.py:\n```py\nprint('Hello Nested World')\n```\n" in contents

def common_test_mixed_content(export_func, create_test_project, needs_ignore_list=False):
    project_path = create_test_project({
        "test_file.py": "print('Hello World')",
        "nested_dir/nested_file.py": "print('Nested File')"
    })

    if needs_ignore_list:
        structure, contents = export_func(project_path, [])
    else:
        structure, contents = export_func(project_path)

    assert './' in structure
    assert '├── test_file.py' in structure
    assert '├── nested_dir/' in structure
    assert '│   ├── nested_file.py' in structure
    assert f"{project_path}/test_file.py:\n```py\nprint('Hello World')\n```\n" in contents
    assert f"{project_path}/nested_dir/nested_file.py:\n```py\nprint('Nested File')\n```\n" in contents
