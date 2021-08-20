import requests

response = requests.get("https://api.github.com/users/Jeffreyricketts/repos")
my_repos = response.json()
print(my_repos)
for repo in my_repos:
    print(f"Repository Name: {repo['name']} | Respository Url: {repo['html_url']}")
