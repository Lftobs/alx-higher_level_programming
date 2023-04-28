#!/usr/bin/python3
"""lists the 10 most recent commits on a particular gitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    results = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                results[i].get("sha"),
                results[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
