import pandas as pd

def get_unique_counties(filename):
    df = pd.read_csv(filename)
    df = df.dropna(subset=['county', 'state'])
    df['county'] = df['county'].str.strip()
    df['state'] = df['state'].str.strip()
    unique_df = df[['county', 'state']].drop_duplicates()
    
    unique_df.to_csv('unique-' + filename, index=False)

get_unique_counties('us-counties-2021.csv')
get_unique_counties('us-counties-2022.csv')
get_unique_counties('us-counties-2023.csv')