import pandas as pd
from bs4 import BeautifulSoup
import requests

cities = ["manhattan",
"bronx",
"brooklyn",
"queens",
"statenisland"]

columns = [
"BOROUGH",
"NEIGHBORHOOD",
"BUILDING CLASS CATEGORY",
"TAX CLASS AT PRESENT",
"BLOCK",
"LOT",
"BUILDING CLASS AT PRESENT",
"ADDRESS",
"APARTMENT NUMBER",
"ZIP CODE",
"YEAR BUILT",
"TAX CLASS AT TIME OF SALE",
"BUILDING CLASS AT TIME OF SALE",
"SALE PRICE",
"SALE DATE"]
appended_data = []

for city in cities:
    df = pd.read_excel(f"https://www.nyc.gov/assets/finance/downloads/pdf/rolling_sales/rollingsales_{city}.xlsx",
    skiprows=4,usecols=columns).query("`BUILDING CLASS AT TIME OF SALE` in ('R1','R2','R3','R4')")
    df.columns=[x.lower() for x in df.columns]
    df.columns=df.columns.str.replace("[ ]","_",regex=True)
    appended_data.append(df)

final_data_frame = pd.concat(appended_data)
final_data_frame.to_csv("C:\Property Project\propert.csv",index=False)
print(final_data_frame)

# url = "https://www.nyc.gov/site/finance/taxes/property-rolling-sales-data.page"
# base_url="https://www.nyc.gov/assets/finance/downloads/pdf/rolling_sales/rollingsales_"
# r = requests.get(url)

# page = BeautifulSoup(r.content,"html.parser")

# links=page.find_all("a", href=lambda href: href and "xlsx" in href)

# for link in links:
#     #print(link)
#     print(link['href'].split('_',2)[2].replace(".xlsx",""))

# columns = [
# "BOROUGH",
# "NEIGHBORHOOD",
# "BUILDING CLASS CATEGORY",
# "TAX CLASS AT PRESENT",
# "BLOCK",
# "LOT",
# "BUILDING CLASS AT PRESENT",
# "ADDRESS",
# "APARTMENT NUMBER",
# "ZIP CODE",
# "YEAR BUILT",
# "TAX CLASS AT TIME OF SALE",
# "BUILDING CLASS AT TIME OF SALE",
# "SALE PRICE",
# "SALE DATE"]
# x = pd.read_excel("https://www.nyc.gov/assets/finance/downloads/pdf/rolling_sales/rollingsales_statenisland.xlsx",
# skiprows=4,usecols=columns).query("`BUILDING CLASS AT TIME OF SALE` in ('R1','R2','R3','R4')")
# print(x)

# #R1,R2,R3,R4,R5
