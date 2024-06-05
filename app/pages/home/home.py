import io

import pandas as pd
from taipy.gui import Markdown, download

from app import algo
from app.data.data import data

# Path to images
world_map_path = "./images/world_map.png"
download_icon_path = "images/Vector.svg"


# Generate the digits, save them in a CSV file content, and trigger a download action
# so the user can retrieve them
def download_el(state, viz):
    buffer = io.StringIO()
    data = viz['data']
    if type(data) == pd.DataFrame:
        data.to_csv(buffer)
    else:
        buffer.write(state["sub_title"] + "\n" + str(data))
    download(state, content=bytes(buffer.getvalue(), "UTF-8"), name="data.csv")


def download_viz_1(state):
    download_el(state, viz_1)


# Viz 1
viz_1 = {
    "data": algo.number_of_tracked_reports(data),
    "title": "Reports tracked",
    "sub_title": "",
    "on_action": download_viz_1
}


# Viz 2
def download_viz_2(state):
    download_el(state, viz_2)


viz_2 = {
    "fig": algo.display_number_of_tracked_reports_over_time(data),
    "data": algo.number_of_tracked_reports_over_time(data),
    "title": "Number of reports over time",
    "sub_title": "------------ --------- ---------",
    "on_action": download_viz_2
}


def download_viz_3(state):
    download_el(state, viz_3)


# Viz 3
viz_3 = {
    "data": algo.number_of_tracked_mnc(data),
    "title": "Multinationals",
    "sub_title": "with 1+ report tracked",
    "on_action": download_viz_3
}


# Viz 24
def download_viz_24(state):
    download_el(state, viz_24)


viz_24 = {
    "fig": algo.viz_24_viz(data),
    "data": algo.viz_24_compute_data(data),
    "title": "Multinationals available",
    "sub_title": "with 1+ report tracked",
    "on_action": download_viz_24
}

# Generate page from Markdown file
home_md = Markdown("pages/home/home.md")
