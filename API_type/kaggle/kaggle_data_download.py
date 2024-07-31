import os
from dotenv import load_dotenv
import kaggle
import datetime

# Load environment variables from the .env file
env_path = '/Users/paigeblackstone/Desktop/Portfolio29/Portfolio29/env/.env'
load_dotenv(env_path)

def authenticate_kaggle():
    try:
        kaggle.api.authenticate()
        print("API authenticated successfully.")
    except Exception as e:
        print(f"An error occurred during authentication: {e}")

def download_dataset(dataset_id, path):
    try:
        authenticate_kaggle()
        kaggle.api.dataset_download_files(dataset_id, path=path, unzip=True)
        print(f"Dataset {dataset_id} downloaded successfully.")
    except Exception as e:
        print(f"An error occurred while downloading the dataset: {e}")

def fetch_and_download_datasets():
    try:
        authenticate_kaggle()
        print("Fetching datasets...")

        # Fetch datasets by votes
        datasets_by_votes = kaggle.api.dataset_list(sort_by='votes', page_size=5)
        print("Top datasets by votes:")
        for dataset in datasets_by_votes:
            dataset_id = dataset.ref
            title = dataset.title
            print(f"Title: {title}, ID: {dataset_id}")
            download_dataset(dataset_id, './datasets_by_votes')

        # Fetch datasets by file size (not directly available in API, this is a conceptual placeholder)
        # Replace with appropriate method or fetch and sort after download
        print("Fetching datasets by file size is not directly supported by Kaggle API.")
        
        # Fetch datasets by date updated
        datasets_by_date = kaggle.api.dataset_list(sort_by='date', page_size=5)
        print("Top datasets by date updated:")
        for dataset in datasets_by_date:
            dataset_id = dataset.ref
            title = dataset.title
            print(f"Title: {title}, ID: {dataset_id}")
            download_dataset(dataset_id, './datasets_by_date')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_and_download_datasets()
