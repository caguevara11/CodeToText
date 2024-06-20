import os
import sys
from exporter.main import ProjectExporter

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No project path provided. Usage: main.py <project_path>")
        sys.exit(1)

    project_path = sys.argv[1]

    # Eliminar el archivo si ya existe
    output_file_path = os.path.join(project_path, 'project_structure.txt')
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    exporter = ProjectExporter()
    project_structure, project_contents = exporter.export(project_path)

    with open(output_file_path, 'w') as file:
        file.write(project_structure)
        file.write('\n\n')
        file.write(project_contents)

    print("Project export completed.")
