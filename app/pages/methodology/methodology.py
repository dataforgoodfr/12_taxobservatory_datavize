from taipy.gui import Markdown
from app import config as cfg

# Path to equation image
equation = f"{cfg.IMAGES}/transparency-score-equation.svg"

# Generate page from Markdown file
methodology_md = Markdown(f"{cfg.PAGES}/methodology/methodology.md")
