from taipy.gui import Markdown

# Initialize dataset file path
dataset_filepath = "data/EUTO_Public_CbCR_Database_2021.xlsx"

# Initialise default name for file to download
download_filename = "EUTO_Public_CbCR_Database_2021.xlsx"

# Generate page from Markdown file
download_md = Markdown("pages/download/download.md")
