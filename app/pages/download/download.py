from taipy.gui import Markdown
from app import config as cfg

# Initialise default name for file to download
download_filename = "EUTO_Public_CbCR_Database_2021.xlsx"
# Initialize dataset file path

dataset_filepath = f"{cfg.DATA}/{download_filename}"

# Generate page from Markdown file
download_md = Markdown(f"{cfg.PAGES}/download/download.md")
