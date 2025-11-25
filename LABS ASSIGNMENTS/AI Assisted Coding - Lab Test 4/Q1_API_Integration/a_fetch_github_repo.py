import requests

def get_repo_data(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Repository Data Fetched Successfully:")
        return response.json()
    else:
        return {"error": f"Request failed with status {response.status_code}"}

if __name__ == "__main__":
    result = get_repo_data("torvalds", "linux")
    print(result)
