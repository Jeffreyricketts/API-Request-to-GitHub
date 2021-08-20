import requests

#Sends request to Github
response = requests.get("https://api.github.com/users/Jeffreyricketts/repos")
my_repos = response.json()

#Prints data in json
print(my_repos)

#Prints specific values from json code, this ccase: Repository Names and Repository Urls
for repo in my_repos:
    print(f"Repository Name: {repo['name']} | Respository Url: {repo['html_url']}")
