from taipy.gui import Markdown

# Path to images
ks1_image_path = "app/images/keystories/tax_revenue_loss_and_profits_shifted.png"
ks2_image_path = "app/images/keystories/reports_per_year.png"

# Generate page from Markdown file
keystories_md = Markdown("app/pages/keystories/keystories.md")
