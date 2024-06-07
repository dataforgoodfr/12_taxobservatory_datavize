import pandas as pd

# Load dataset
path_to_data = "./app/data/data_final_dataviz.csv"
data = pd.read_csv(path_to_data, sep=",", low_memory=False)

# Filter dataset with the maximum year to take in account
max_year_of_reports = 2021
data = data.loc[data["year"] <= max_year_of_reports]
