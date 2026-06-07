from data_source import fetch_posts
from data_formatter import format_posts
from data_cleaner import clean_posts
from data_saver import save_csv


def run_pipeline():
    # Step 1: Fetch data
    print("Fetching posts...")
    posts = fetch_posts()

    # Step 2: Format data
    print("Formatting posts...")
    df = format_posts(posts)

    # Step 3: Clean data
    print("Cleaning posts...")
    cleaned_posts = clean_posts(df)

    # Step 4: Save data
    print("Saving data...")
    save_csv(cleaned_posts, "data/processed/posts.csv")

    print("Pipeline completed successfully")



if __name__ == "__main__":
    run_pipeline()