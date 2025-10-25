import requests
from bs4 import BeautifulSoup

def get_trending(language="python", limit=10):
    url = f"https://github.com/trending/{language}?since=daily"
    res = requests.get(url)
    if res.status_code != 200:
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.find_all("h2", class_="h3")[:limit]

    repos = []
    for item in items:
        repo_name = item.text.strip().replace("\n", "").replace(" ", "")
        repos.append({
            "author": repo_name.split("/")[0],
            "name": repo_name.split("/")[1],
            "url": "https://github.com/" + repo_name,
            "stars": "N/A",
            "language": language
        })
    return repos
