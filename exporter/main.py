import os
from exporter.file_handler import FileHandler
from exporter.ignore_parser import IgnoreParser

class ProjectExporter:
    def __init__(self):
        self.file_handler = FileHandler()
        self.ignore_parser = IgnoreParser()

    def export(self, project_path: str, output_file_path: str, repo_name: str, is_remote: bool):
        ignore_list = self.ignore_parser.parse_gitignore(project_path)
        project_structure, project_contents = self.file_handler.generate_project_structure(project_path, ignore_list, repo_name)
        
        # Print the location where the output file will be saved
        print(f"Exporting project structure and contents to: {output_file_path}")
        
        # Add information about the repository type and name
        repo_info = f"Repository Type: {'Remote (GitHub)' if is_remote else 'Local'}\n"
        repo_info += f"Repository Name: {repo_name}\n\n"
        
        return repo_info + project_structure, project_contents
