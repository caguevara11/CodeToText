import os

class IgnoreParser:
    def parse_gitignore(self, project_path: str) -> list:
        ignore_list = []
        project_ignore_file = os.path.join(project_path, '.gitignore')
        default_ignore_file = os.path.join(os.path.dirname(__file__), '..', '.default_gitignore')

        # Always read the default ignore file
        ignore_list.extend(self._read_ignore_file(default_ignore_file))

        # Read the project-specific .gitignore if it exists
        if os.path.exists(project_ignore_file):
            ignore_list.extend(self._read_ignore_file(project_ignore_file))

        return ignore_list

    def _read_ignore_file(self, file_path: str) -> list:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]
