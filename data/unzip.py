import zipfile
import os

with zipfile.ZipFile("crimedata_csv_AllNeighbourhoods_AllYears.zip", 'r') as zip_ref:
    zip_ref.extractall(os.getcwd())

with zipfile.ZipFile("fullmoonarchive.zip", 'r') as zip_ref:
    zip_ref.extractall(os.getcwd())