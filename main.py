import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} | Project Url: {project['web_url']}")

print()
response = requests.get("https://api.github.com/users/Jeffreyricketts/repos")
my_repos = response.json()

for repo in my_repos:
    print(f"Repository Name: {repo['name']} | Respository Url: {repo['html_url']}")