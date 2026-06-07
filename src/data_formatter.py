import pandas as pd

def format_posts(posts):
    return pd.DataFrame(posts)

if __name__ == "__main__":
    sample_posts = [
        {
            "userId": 1,
            "id": 1,
            "title": "Test Title",
            "body": "Test Body"
        }
    ]

    df = format_posts(sample_posts)

    print(df)
    print(type(df))