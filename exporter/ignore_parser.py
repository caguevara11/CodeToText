import os

class IgnoreParser:
    def parse_gitignore(self, project_path: str) -> list:
        ignore_list = []
        ignore_file = os.path.join(project_path, '.gitignore')
        default_ignore_file = os.path.join(os.path.dirname(__file__), '..', '.default_gitignore')

        if not os.path.exists(ignore_file):
            ignore_file = default_ignore_file

        with open(ignore_file, 'r') as file:
            ignore_list = [line.strip() for line in file if line.strip() and not line.startswith('#')]

        if ignore_file != default_ignore_file:
            with open(default_ignore_file, 'r') as file:
                ignore_list.extend([line.strip() for line in file if line.strip() and not line.startswith('#')])

        return ignore_list
