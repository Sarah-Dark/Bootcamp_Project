# -*- coding: utf-8 -*-
"""Forbes 2023 Leading Sectors

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wLye531GDTuTC0sBGfwYThHPSFFCk_xy
"""

# requests library to fetch web page and Importing BeautifulSoup to parse HTML content
import requests
from bs4 import BeautifulSoup

# Sending a request to fetch the page content and Parsing the HTML content of the page using BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Fortune_Global_500'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
print(soup)

# Finding all tables in the page and selecting the fourth table (index 3)
soup.find_all('table')[3]

table = soup.find_all('table')[3]

# Extracting all table headers (th elements) from the selected table
sector_titles = table.find_all('th')

# Extracting and cleaning text from the headers
sector_table_title = [title.text.strip() for title in sector_titles]
print(sector_table_title)

import pandas as pd

df = pd.DataFrame(columns = sector_table_title)

# Extracting all rows from the table
column_data = table.find_all('tr')

# Iterating over each row (skipping the first row as it contains headers)
for row in column_data[1:]:
    row_data = row.find_all('td')# Extracting all data cells from the row
    idv_row_data = [data.text.strip() for data in row_data]  # Cleaning text

    length = len(df)  # Finding current length of DataFrame
    df.loc[length] = idv_row_data  # Appending new row to the DataFrame

df

# Saving the extracted data to a CSV file
df.to_csv(r'C:\Users\theda\OneDrive\Documents\Data Skills Bootcamp\Project\Sector.csv', index = False)



