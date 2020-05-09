# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku
# /datasets/imiona.xlsx

import pandas as pd
import numpy as np
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)