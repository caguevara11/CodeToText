import os
import tempfile
import shutil
import requests
from git import Repo

class GitHubHandler:
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
            response = requests.get(api_url)
            
            if response.status_code == 200:
                content = response.json()['content']
                gitignore_content = requests.utils.unquote(content)
                
                # Write the .gitignore file
                with open(os.path.join(temp_dir, '.gitignore'), 'w') as f:
                    f.write(gitignore_content)
            
            return temp_dir
        except Exception as e:
            shutil.rmtree(temp_dir)
            raise e
