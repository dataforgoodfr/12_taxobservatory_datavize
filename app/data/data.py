import pandas as pd

# Load dataset
path_to_data = "./data/data_final_dataviz.csv"
data = pd.read_csv(path_to_data, sep=",", low_memory=False)
