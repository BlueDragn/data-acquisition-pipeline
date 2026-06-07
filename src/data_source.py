# src/data_source.py

import requests

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors
    return response.json()

if __name__ == "__main__":
    posts = fetch_posts()

    print(f"Total posts fetched: {len(posts)}")
    print(posts[0])  # Print the first post as a sample