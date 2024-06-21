"""
Handles operations related to GitHub repositories, such as
cloning a repository to a temporary directory.
"""

import os
import tempfile
import shutil
import requests
from git import Repo

class GitHubHandler:
    """
    Manages operations related to GitHub repositories, such as
    cloning a repository to a temporary directory.
    """
    def clone_repo(self, github_url: str) -> str:
        """
        Clone a GitHub repository to a temporary directory.

        :param github_url: URL of the GitHub repository
        :return: Path to the cloned repository
        """
        # Extract owner and repo name from the URL
        parts = github_url.rstrip('/').split('/')
        owner, repo = parts[-2], parts[-1]

        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()

        try:
            # Clone the repository
            Repo.clone_from(github_url, temp_dir)

            # Fetch the .gitignore file from GitHub API
            api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/.gitignore"
            response = requests.get(api_url, timeout=10)

            if response.status_code == 200:
                content = response.json()['content']
                gitignore_content = requests.utils.unquote(content)

                # Write the .gitignore file
                with open(os.path.join(temp_dir, '.gitignore'), 'w', encoding='utf-8') as f:
                    f.write(gitignore_content)

            return temp_dir
        except Exception as e:
            shutil.rmtree(temp_dir)
            raise e

    def is_github_url(self, url: str) -> bool:
        """
        Checks if the provided URL is a GitHub URL.

        :param url: The URL to check.
        :return: True if the URL is a GitHub URL, False otherwise.
        """
        return url.startswith("https://github.com/") or url.startswith("git@github.com:")

    def handle_url(self, url: str) -> str:
        """
        Determines if the URL is a GitHub repository URL and clones it if so,
        otherwise returns the URL as-is.

        :param url: The URL to process.
        :return: Path to the cloned repository or the original URL.
        """
        if self.is_github_url(url):
            return self.clone_repo(url)
        else:
            return url
