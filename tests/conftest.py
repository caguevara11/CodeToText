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
