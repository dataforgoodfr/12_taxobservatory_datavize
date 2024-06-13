import pandas as pd
from taipy.gui import Gui, State, navigate  # ,get_state_id

from app import config as cfg
from app.pages.company.company import company_md
from app.pages.company.company import on_init as on_init_company
from app.pages.contact.contact import contact_md
from app.pages.download.download import download_md
from app.pages.home.home import home_md
from app.pages.home.home import on_init as on_init_home
from app.pages.keystories.keystories import keystories_md
from app.pages.methodology.methodology import methodology_md
from app.pages.root import root

# Global variables
# APP
APP_TITLE = "Taxplorer"
FAVICON = "images/taxplorer-logo.svg"
# DATA
MAX_YEAR_OF_REPORTS = 2021
PATH_TO_DATA = f"{cfg.DATA}/data_final_dataviz.csv"

data: pd.DataFrame = None


def on_init(state: State):
    # print('MAIN ON_INIT...')
    # print(f'MAIN STATE {get_state_id(state)}')

    # Init data
    init_data(state)
    # Call company on_init
    on_init_company(state)
    # Call company on_init
    on_init_home(state)

    # print('MAIN ON_INIT...END')


# Performance optimization
def init_data(state: State):
    df = pd.read_csv(f"{PATH_TO_DATA}", sep=",", low_memory=False, encoding="utf-8")
    # Filter dataset with the maximum year to take in account
    df = df.loc[df["year"] <= MAX_YEAR_OF_REPORTS].reset_index()
    state.data = df


# Add pages
pages = {
    "/": root,
    "Home": home_md,
    "KeyStories": keystories_md,
    "Company": company_md,
    "Methodology": methodology_md,
    "Contact": contact_md,
    "Download": download_md,
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
gui_multi_pages = Gui(pages=pages, css_file="css/style.css")

# Customize the Stylekit
stylekit = {
    "color_primary": "#021978",
    "color_secondary": "#C0FFE",
    "color_paper_light": "#FFFFFF",
    "color_background_light": "#FFFFFF",
    "font_family": "Manrope",
}


if __name__ == "__main__":
    ## DEV
    # Start the local flask server
    gui_multi_pages.run(
        dark_mode=False,
        stylekit=stylekit,
        title=f"{APP_TITLE}",
        favicon=f"{FAVICON}",
        # Remove watermark "Taipy inside"
        watermark="LOCAL DEVELOPMENT",
    )
else:
    ## PRODUCTION
    # Start the app used by uwsgi server
    web_app = gui_multi_pages.run(
        dark_mode=False,
        stylekit=stylekit,
        title=f"{APP_TITLE}",
        favicon=f"{FAVICON}",
        run_server=False,
        debug=False,
        # Remove watermark "Taipy inside"
        watermark="",
        # IMPORTANT: Set the async_mode to gevent_uwsgi to use uwsgi
        # See https://python-socketio.readthedocs.io/en/latest/server.html#uwsgi
        async_mode="gevent_uwsgi",
    )
