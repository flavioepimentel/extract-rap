"""
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

"""

from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)

spreadsheet_id = 'SEU_ID_DA_PLANILHA'
range_ = 'Página1!A1'
values = [["Novo dado 1", "Novo dado 2"]]

body = {
    'values': values
}

result = service.spreadsheets().values().append(
    spreadsheetId=spreadsheet_id,
    range=range_,
    valueInputOption="RAW",
    body=body
).execute()

print(f"{result.get('updates').get('updatedCells')} células atualizadas.")

service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    range="Página1!B2",
    valueInputOption="RAW",
    body={"values": [["Novo valor"]]}
).execute()
