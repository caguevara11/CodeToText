import subprocess
import sys
import os
import pytest

@pytest.fixture
def create_test_project(tmpdir):
    def _create_project(structure):
        base_dir = tmpdir.mkdir("test_project")
        for path, content in structure.items():
            file = base_dir.join(path)
            file.write(content)
        return str(base_dir)
    return _create_project

def test_main_script_no_project_path(monkeypatch, tmpdir):
    project_path = tmpdir.mkdir("test_project")
    test_file = project_path.join("test_file.py")
    test_file.write("print('Hello World')")

    # Set sys.argv for the main.py script without project path argument
    monkeypatch.setattr(sys, 'argv', ['main.py'])

    # Copy the content of main.py to the temporary directory for testing
    with open('main.py', 'r') as f:
        main_script_content = f.read()

    tmp_main_script = tmpdir.join("main.py")
    tmp_main_script.write(main_script_content)

    # Adjust the PYTHONPATH to include the root directory of the project
    env = os.environ.copy()
    env['PYTHONPATH'] = os.getcwd()

    # Execute main.py in the temporary environment with the adjusted PYTHONPATH
    result = subprocess.run([sys.executable, str(tmp_main_script)], cwd=str(tmpdir), env=env, text=True, capture_output=True)

    # Debugging: Print stdout and stderr to understand what happened during the execution
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    # Verify that the script failed with the correct error message
    assert result.returncode != 0
    assert "Error: No project path provided. Usage: main.py <project_path>" in result.stdout
