import pandas as pd


excel_file="first_1.xlsx"

df =pd.read_excel(excel_file)
df.to_html("test.html")
