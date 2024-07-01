from taipy.gui import Markdown

from app import config as cfg

# Generate page from Markdown file
methodology_md = Markdown(f"{cfg.PAGES}/methodology/methodology.md")
