import pandas as pd

def save_csv(df, file_path):
    df.to_csv(file_path, index=False)



if __name__ == "__main__":
    sample_data = {
        "userId": [1, 2],
        "id": [1, 2],
        "title": ["Post 1", "Post 2"],
        "body": ["Body 1", "Body 2"]
    }

    df = pd.DataFrame(sample_data)

    save_csv(df, "data/processed/posts.csv")
    print("Data saved successfully")