#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts.
    Args:
        subreddit (str): The name of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            title = post.get("data").get("title")
            print(title)
    else:
        print(None)


if __name__ == "__main__":
    subreddit = input("Enter the subreddit: ")
    top_ten(subreddit)
