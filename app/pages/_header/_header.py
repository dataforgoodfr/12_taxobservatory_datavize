from taipy.gui import navigate

from app import config as cfg
from app.page import Page

page_id = "_header"


def to_text(val):
    return "{:,}".format(int(val)).replace(",", " ")


# Path to image
taxplorer_logo_path = f"{cfg.IMAGES}/taxplorer-logo.svg"

# Initialise navbar items
navbar_items = [
    ("/Home", "Home"),
    ("/KeyStories", "KeyStories"),
    ("/Company", "Company"),
    ("/Methodology", "Methodology"),
    ("/Contact", "Contact"),
    ("/Download", "Data"),
]


def goto_d4g_website(state):
    navigate(state, "https://dataforgood.fr/", tab="_blank")


# Generate page from Markdown file
header_md = Page(f"{__name__}").markdown()
