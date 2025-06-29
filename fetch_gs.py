import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
import os
import json

creds_json = os.environ.get('GOOGLE_CREDS_JSON')

# Define API scopes
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from JSON file (downloaded from Google Cloud Console)
creds = service_account.Credentials.from_service_account_info(json.loads(creds_json))


def fetch_data():

    # Authorize gspread client
    client = gspread.authorize(creds)

    sheet = client.open_by_key("1twGCBbDdXSUbxUSDA_pUY2HXexz0VQ7OWjRyKESuVLI").sheet1

    # Read all records as list of dictionaries
    data = sheet.get_all_records()

    # Print all form responses
    for row in data:
        print(row)
