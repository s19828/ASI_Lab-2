import gspread
import os
import pandas as pd

API_KEY = os.getenv('GOOGLE_API_KEY')
SPREADSHEET_ID = '1c0q4djpUiU1xRmt4iOTKJkC87w7ZVU1XCPsXSUqcRTs'

gc = gspread.Client(auth=None)
gc.login()

spreadsheet_url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/Sheet1!A1?key={API_KEY}"

df = pd.read_csv('PJATK-ASI-2024/Lab2---Obr-bka-danych/data_student_19828.csv')
data = [df.columns.values.tolist()] + df.values.tolist()
sh = gc.open_by_key(SPREADSHEET_ID)
worksheet = sh.sheet1
worksheet.clear()
worksheet.update('A1', data)