#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of
If an invalid subreddit is given, returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API.
    Args:
        subreddit (str): The name of the subreddit.
    Returns:
        int: The number of subscribers for the subreddit, or 0 if invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0


if __name__ == "__main__":
    subreddit = input("Enter the subreddit: ")
    print("Number of subscribers:", number_of_subscribers(subreddit))
