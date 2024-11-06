import requests
import os

# Repository and path details
repo_owner = "Wattysaid"
repo_name = "dsif-git-main-project"
repo_path = "elvtr_main_project/reports"

# GitHub API endpoint for repository contents
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{repo_path}"

# Headers (optional: include personal access token for private repos or rate limits)
headers = {
    "Accept": "application/vnd.github.v3+json"
    # "Authorization": "token YOUR_GITHUB_TOKEN" # Uncomment if authentication is required
}

# Function to check if a file is an image based on its extension
def is_image(file_name):
    image_extensions = (".png", ".jpg", ".jpeg", ".gif", ".svg")
    return file_name.lower().endswith(image_extensions)

# Function to generate markdown content for images
def create_markdown_image_content(file_name, file_url):
    return f"![{file_name}]({file_url})\n"

# Initialize markdown content
markdown_content = "# Reports\n\nThis document contains all image files from the reports directory.\n\n"

# Fetch directory contents
response = requests.get(url, headers=headers)

# Check response status
if response.status_code == 200:
    files = response.json()
    for file in files:
        file_name = file["name"]
        if is_image(file_name):
            file_url = file["download_url"]
            if file_url:
                # Add image markdown to content
                markdown_content += create_markdown_image_content(file_name, file_url)
else:
    print(f"Failed to fetch contents. Status code: {response.status_code}")

# Write to Reports.md
with open("Reports.md", "w") as md_file:
    md_file.write(markdown_content)

print("Reports.md has been created with all image files embedded.")
