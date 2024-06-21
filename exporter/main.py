import os
from exporter.file_handler import FileHandler
from exporter.ignore_parser import IgnoreParser

class ProjectExporter:
    def __init__(self):
        self.file_handler = FileHandler()
        self.ignore_parser = IgnoreParser()

    def export(self, project_path: str):
        ignore_list = self.ignore_parser.parse_gitignore(project_path)
        project_structure, project_contents = self.file_handler.generate_project_structure(project_path, ignore_list)
        
        # Save project structure to a file
        structure_file = os.path.join(project_path, 'project_structure.txt')
        with open(structure_file, 'w') as f:
            f.write(project_structure)
        
        # Save project contents to a file
        contents_file = os.path.join(project_path, 'project_contents.txt')
        with open(contents_file, 'w') as f:
            f.write(project_contents)
        
        print(f"Project structure exported to: {structure_file}")
        print(f"Project contents exported to: {contents_file}")
        
        return project_structure, project_contents
