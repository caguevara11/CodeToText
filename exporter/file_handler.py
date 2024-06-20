import os
import fnmatch
from typing import Tuple

class FileHandler:
    def generate_project_structure(self, project_path: str, ignore_list: list) -> Tuple[str, str]:
        structure = []
        contents = []

        for root, dirs, files in os.walk(project_path):
            dirs[:] = [d for d in dirs if not self._should_ignore(os.path.join(root, d), ignore_list)]
            files = [f for f in files if not self._should_ignore(os.path.join(root, f), ignore_list)]

            level = root.replace(project_path, '').count(os.sep)
            indent = '│   ' * level
            structure.append(f'{indent}├── {os.path.basename(root)}/' if level > 0 else f'./')

            sub_indent = '│   ' * (level + 1)
            for file in files:
                file_path = os.path.join(root, file)
                structure.append(f'{sub_indent}├── {file}')
                content = self.read_file(file_path)
                extension = os.path.splitext(file)[1][1:]
                contents.append(f'{file_path}:\n```{extension}\n{content}\n```\n')

        return '\n'.join(structure), '\n'.join(contents)

    def read_file(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='latin-1') as f:
                    return f.read()
            except UnicodeDecodeError:
                return "Unable to decode file content"

    def _should_ignore(self, path: str, ignore_list: list) -> bool:
        for pattern in ignore_list:
            if pattern.endswith('/'):
                pattern = pattern.rstrip('/')
                if fnmatch.fnmatch(os.path.basename(path.rstrip('/')), pattern):
                    return True
                continue
            if fnmatch.fnmatch(path, pattern):
                return True
            if fnmatch.fnmatch(os.path.basename(path), pattern):
                return True
        return False
