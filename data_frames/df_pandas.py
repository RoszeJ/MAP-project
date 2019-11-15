import pandas as pd
df_xlsx = pd.read_excel('LA_and_Regional_Spreadsheet_201718_rev2.xlsx',sheet_name=None)
df_xlsx.keys()
#print(df_xlsx.head())
# print(df_xlsx['Table_1'].head(50))
# print(df_xlsx['Table_2'].columns)
# print(df_xlsx['Table_3'].columns)
table_1 = df_xlsx['Table_1']
# print(table_1)
# print(table_1.columns)
# print(table_1[['Financial Year','Region','Local Authority','Total local authority collected waste (tonnes)','Household - total waste (tonnes)','Non-household - total waste (tonnes)']])
print(table_1.loc[table_1['Local Authority'] == 'Darlington Borough Council'])