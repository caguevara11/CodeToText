from exporter.file_handler import FileHandler
from exporter.ignore_parser import IgnoreParser

class ProjectExporter:
    def __init__(self):
        self.file_handler = FileHandler()
        self.ignore_parser = IgnoreParser()

    def export(self, project_path: str):
        ignore_list = self.ignore_parser.parse_gitignore(project_path)
        project_structure, project_contents = self.file_handler.generate_project_structure(project_path, ignore_list)
        return project_structure, project_contents

