import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
import os
import json


# Define API scopes
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from JSON file (downloaded from Google Cloud Console)
creds = service_account.Credentials.from_service_account_file('/etc/secrets/project-a462568f0ad8.json',scopes=scope)

def fetch_data():

    # Authorize gspread client
    client = gspread.authorize(creds)

    sheet = client.open_by_key("1twGCBbDdXSUbxUSDA_pUY2HXexz0VQ7OWjRyKESuVLI").sheet1

    # Read all records as list of dictionaries
    data = sheet.get_all_records()

    # Print all form responses
    for row in data:
        print(row)
