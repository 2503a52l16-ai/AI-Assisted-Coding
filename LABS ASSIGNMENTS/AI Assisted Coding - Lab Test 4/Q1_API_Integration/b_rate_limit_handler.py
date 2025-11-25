import requests
import time

def get_repo_with_rate_limit(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)

    # Handle rate limit
    if response.status_code == 403 and "X-RateLimit-Remaining" in response.headers:
        remaining = response.headers["X-RateLimit-Remaining"]
        reset_time = int(response.headers["X-RateLimit-Reset"])
        wait = reset_time - int(time.time())

        return {
            "error": "Rate limit exceeded",
            "remaining": remaining,
            "wait_seconds": wait
        }

    return response.json()

if __name__ == "__main__":
    output = get_repo_with_rate_limit("torvalds", "linux")
    print(output)
