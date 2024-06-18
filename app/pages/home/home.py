from taipy.gui import Markdown, State  # , get_state_id

from app import algo
from app import config as cfg
from app.viz import Viz

# from app.data.data import data

# Path to images
world_map_path = f"{cfg.IMAGES}/world_map.png"
download_icon_path = f"{cfg.IMAGES}/Vector.svg"


# Initialize state (Taipy callback function)
# Called by main.py/on_init
def on_init(state: State):
    # print('HOME ON INIT...')
    # print(f'HOME STATE ID {get_state_id(state)}')
    with state as s:
        update_viz(s)
    # print('HOME ON INIT...END')


# Viz store map[viz_id,viz_dict]
# Important for taipy bindings
# Use Viz.init on each page with set of viz_id
viz: dict[str, dict] = Viz.init(
    (
        "general_number_of_tracked_reports",
        "general_number_of_tracked_reports_over_time",
        "general_number_of_tracked_mnc",
        "general_list_of_tracked_mnc_available",
    )
)


def update_viz(state: State):
    id = "general_number_of_tracked_reports"
    state.viz[id] = Viz(
        id=id,
        state=state,
        data=algo.number_of_tracked_reports(state.data),
        title="Reports tracked",
        sub_title="",
    ).to_state()

    id = "general_number_of_tracked_reports_over_time"
    # TODO PERF : all in once
    # algo_data, algo_fig = algo.display_number_of_tracked_reports_over_time(state.data)
    state.viz[id] = Viz(
        id=id,
        state=state,
        fig=algo.number_of_tracked_reports_over_time(state.data),
        title="Number of reports over time",
    ).to_state()

    id = "general_number_of_tracked_mnc"
    state.viz[id] = Viz(
        id=id,
        state=state,
        data=algo.number_of_tracked_mnc(state.data),
        title="Multinationals",
        sub_title="with 1+ report tracked",
    ).to_state()

    id = "general_list_of_tracked_mnc_available"
    state.viz[id] = Viz(
        id=id,
        state=state,
        fig=algo.mnc_tracked(state.data),
        title="Multinationals available",
        sub_title="with 1+ report tracked",
    ).to_state()


# Generate page from Markdown file
home_md = Markdown(f"{cfg.PAGES}/home/home.md")
# NOT WORKING: home_md: Markdown = Page("home").markdown()
