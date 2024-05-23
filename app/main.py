from taipy.gui import Gui

from pages.root import root
from pages.home.home import home_md
from pages.company.company import company_md
from pages.keystories.keystories import keystories_md
from pages.methodology.methodology import methodology_md
from pages.contact.contact import contact_md

# Add pages
pages = {
    "/": root,
    "Home": home_md,
    "KeyStories": keystories_md,
    "Company": company_md,
    "Methodology": methodology_md,
    "Contact": contact_md
}

# Initialise Gui with pages and style sheet
gui_multi_pages = Gui(
    pages=pages,
    css_file="css/style.css"
)

# Customize the Stylekit
stylekit = {
    "color_primary": "#021978",
    "color_secondary": "#C0FFE",
    "color_paper_light": "#FFFFFF",
    "color_background_light": "#F2F2F2",
    "font_family": "Manrope"
}

if __name__ == "__main__":
    # Start the server
    gui_multi_pages.run(
        dark_mode=False,
        stylekit=stylekit,
        title="Taxplorer · EU Tax Observatory"
    )
