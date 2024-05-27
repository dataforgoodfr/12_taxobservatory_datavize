from taipy.gui import Markdown

# Initialize dataset file path
dataset_filepath = "./data/data_final_dataviz.csv"

# Initialise default name for file to download
download_filename = "data_final_dataviz.csv"

# Generate page from Markdown file
download_md = Markdown("pages/download/download.md")
