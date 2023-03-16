import csv
import pandas as pd

def get_county_pop_data():
    with open('co-est2021-alldata.csv', 'r', encoding='utf-8') as input_file, open('county_pop_data.csv', 'w', newline='') as output_file:
        reader = csv.DictReader(input_file)
        writer = csv.writer(output_file)
        
        writer.writerow(['county', 'state', 'population'])
        
        for row in reader:
            county_name = row['CTYNAME'].replace(' County', '').replace(' Parish', '').strip()
            state_name = row['STNAME']
            population = row['POPESTIMATE2021']
            
            writer.writerow([county_name, state_name, population])

def get_county_population(filename):
    county_pop_df = pd.read_csv('county_pop_data.csv')
    unique_counties_df = pd.read_csv(filename)
    merged_df = pd.merge(unique_counties_df, county_pop_df, on=['county', 'state'], how='left')

    population_df = merged_df.dropna(subset=['population'])
    missing_df = merged_df[merged_df['population'].isna()]

    population_df.to_csv('population-' + filename, columns=['county', 'state', 'population'], index=False)

    missing_df.to_csv('missing-population-' + filename, columns=['county', 'state'], index=False)


# get_county_pop_data()
get_county_population('unique-us-counties-2021.csv')
get_county_population('unique-us-counties-2022.csv')
get_county_population('unique-us-counties-2023.csv')


