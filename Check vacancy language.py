import openpyxl
import langdetect
from langdetect import detect

# set var to workbook
wb=openpyxl.load_workbook("vacatures.xlsx")

# Sheets in workbook
wb.get_sheet_names()

# set var to active sheet
ws=wb.active

lang = detect(str_detect)

# for i in range(1,ws.max_row):
#     if ws.cell(row=1, column=1).value == find_str:
#         for j in range(i, ws.max_column):
#             print (ws.cell(row=i, column=j).value)

