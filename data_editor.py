import gspread
import os
import pandas as pd

# pobranie klucza API
API_KEY = os.getenv('GOOGLE_API_KEY')
SPREADSHEET_ID = '1c0q4djpUiU1xRmt4iOTKJkC87w7ZVU1XCPsXSUqcRTs'

# uruchomienie klienta API
gc = gspread.Client(None, API_KEY)

# otworzenie i wczytanie arkusza z Google Sheets
spreadsheet = gc.open_by_key(SPREADSHEET_ID)
worksheet = spreadsheet.get_worksheet(0)
data = worksheet.get_all_values()

# obróbka danych