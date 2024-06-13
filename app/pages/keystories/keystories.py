from taipy.gui import Markdown

from app import config as cfg

# Path to images
ks1_image_path = f"{cfg.IMAGES}/keystories/tax_revenue_loss_and_profits_shifted.png"
ks2_image_path = f"{cfg.IMAGES}/keystories/reports_per_year.png"

# Generate page from Markdown file
keystories_md = Markdown(f"{cfg.PAGES}/keystories/keystories.md")
