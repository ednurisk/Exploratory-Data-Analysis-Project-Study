import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

df_companies = pd.read_csv('Unicorn_Companies.csv')
#Data exploration
df_companies.head(5)
df_companies.shape
df_companies.info()
df_companies.describe()

#Data Preprocessing
df_companies['Year_Joined'] = pd.to_datetime(df_companies['Date Joined']).dt.year
df_companies.isna().sum()

mask = mask.any(axis=1)
mask.head()
df_missing_rows = df_companies[mask]
df_missing_rows

#Model
count_total = df_companies.size
count_total

count_dropna_rows = df_companies.dropna().size
count_dropna_rows

count_dropna_columns = df_companies.dropna(axis=1).size
count_dropna_columns

row_percent = ((count_total - count_dropna_rows) / count_total) * 100
print(f'Percentage removed, rows: {row_percent:.3f}')
col_percent = ((count_total - count_dropna_columns) / count_total) * 100
print(f'Percentage removed, columns: {col_percent:.3f}')


df_companies_backfill = df_companies.fillna(method='backfill')
df_companies_backfill.iloc[df_missing_rows.index, :]


cities = ['Beijing', 'San Francisco', 'London']
mask = (
    (df_companies['Industry']=='Hardware') & (df_companies['City'].isin(cities))
) | (
    (df_companies['Industry']=='Artificial intelligence') & (df_companies['City']=='London')
)

df_invest = df_companies[mask]
df_invest

#Create barplot for top 20 non-big-4 countries
national_valuations = df_companies.groupby(['Country/Region'])['valuation_num'].sum(
).sort_values(ascending=False).reset_index()

national_valuations_no_big4 = national_valuations.iloc[4:, :]
national_valuations_no_big4.head()

sns.barplot(data=national_valuations_no_big4.head(20),
            y='Country/Region',
            x='valuation_num')
plt.title('Top 20 non-big-4 countries by total company valuation')
plt.show();
