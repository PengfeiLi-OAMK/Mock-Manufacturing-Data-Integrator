from src.converter import load_data, transform_data
from src.mock_pywats import PyWATSClient
import os 
from dotenv import load_dotenv

load_dotenv()
# data/factory_test_report.xlsx is a sample file included in the repo for testing
FILE_PATH = os.getenv("RAW_FILE", "data/factory_test_report.xlsx") 
# https://httpbin.org/post is the Mock endpoint for testing
API_URL = os.getenv("WATS_API", "https://httpbin.org/post")  
# 'mocked_token_12345' is the Mocked token for testing purposes
API_TOKEN = os.getenv("API_TOKEN", "mocked_token_12345")


def main():
	raw_df=load_data(FILE_PATH)
	if raw_df is not None:
		print("Data loaded successfully.")
		before_count=len(raw_df)
		standardized_data = transform_data(raw_df)
		after_count=len(standardized_data)
		print(f"Transformed {after_count} records.Dropped {before_count -after_count} invalid rows.")
	client = PyWATSClient(API_URL, API_TOKEN)
	for record in standardized_data:
			client.submit_report(record)
if __name__ == '__main__':
	main()