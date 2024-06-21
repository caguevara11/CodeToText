"""
Main entry point for the CodeToText tool. This script handles the
conversion of a git repository into a single well-formatted.txt or.md file.
It supports both local and remote repositories, including GitHub URLs.
"""
import os
import sys
from exporter.main import ProjectExporter
from exporter.github_handler import GitHubHandler

def is_github_url(url: str) -> bool:
    """
    Checks if the provided URL is a GitHub URL.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is a GitHub URL, False otherwise.
    """
    return url.startswith("https://github.com/") or url.startswith("git@github.com:")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No project path or GitHub URL provided. \
              Usage: main.py <project_path_or_github_url>")
        sys.exit(1)

    project_path_or_url = sys.argv[1]

    if is_github_url(project_path_or_url):
        github_handler = GitHubHandler()
        project_path = github_handler.clone_repo(project_path_or_url)
    else:
        project_path = project_path_or_url

    # Remove the file if it already exists
    output_file_path = os.path.join(project_path, 'project_structure.txt')
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    exporter = ProjectExporter()
    project_structure, project_contents = exporter.export(project_path)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(project_structure)
        file.write('\n\n')
        file.write(project_contents)

    print("Project export completed.")

    # Clean up temporary directory if it was a GitHub repository
    if is_github_url(project_path_or_url):
        import shutil
        shutil.rmtree(project_path)
