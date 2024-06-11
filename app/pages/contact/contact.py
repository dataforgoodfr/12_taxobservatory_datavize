from taipy.gui import Markdown
from app import config as cfg

# Generate page from Markdown file
contact_md = Markdown(f"{cfg.PAGES}/contact/contact.md")
