from taipy.gui import Gui, navigate

from app.pages.company.company import company_md
from app.pages.contact.contact import contact_md
from app.pages.download.download import download_md
from app.pages.home.home import home_md
from app.pages.keystories.keystories import keystories_md
from app.pages.methodology.methodology import methodology_md
from app.pages.root import root

# Add pages
pages = {
    "/": root,
    "Home": home_md,
    "KeyStories": keystories_md,
    "Company": company_md,
    "Methodology": methodology_md,
    "Contact": contact_md,
    "Download": download_md
}


# Functions used to navigate between pages
def goto_home(state):
    navigate(state, "Home")


def goto_keystories(state):
    navigate(state, "KeyStories")


def goto_company(state):
    navigate(state, "Company")


def goto_contact(state):
    navigate(state, "Contact")


def goto_methodology(state):
    navigate(state, "Methodology")


def goto_download(state):
    navigate(state, "Download")


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
    "color_background_light": "#FFFFFF",
    "font_family": "Manrope"
}

# Start the server
if __name__ == "__main__":
    web_app = gui_multi_pages.run(
        dark_mode=False,
        stylekit=stylekit,
        title="Taxplorer",
        favicon="./images/taxplorer-logo.svg",
        run_server=True,
        debug=False,
    )
else:
    web_app = gui_multi_pages.run(
        dark_mode=False,
        stylekit=stylekit,
        title="Taxplorer",
        favicon="./images/taxplorer-logo.svg",
        run_server=False,
        debug=False,
        async_mode='gevent_uwsgi'
    )

