import pandas as pd
def clean_posts(posts):
    df = pd.DataFrame(posts)

    df.dropna(inplace=True)

    df = df.reset_index(drop=True)
    return df


if __name__ == "__main__":
    sample_data = {
            "userId": [1, 1, None],
            "id": [1, 1, 2],
            "title":["Test", "Another Test", None],
            "body": ["Test Body", "Another Test Body", None]
        }
    df = pd.DataFrame(sample_data)
    print("Before cleaning:")
    print(df)
    cleaned_df = clean_posts(sample_data)
    print("\nAfter cleaning:")
    print(cleaned_df)




