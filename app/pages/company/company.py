from mimetypes import init

import numpy as np
import pandas as pd
from app import algo
from app import config as cfg
from app.viz import Viz

company_image_path = f"{cfg.IMAGES}/pexels-ingo-joseph-1880351.png"

DEFAULT_COMPANY = "SHELL"

# Init bindings (used in md file)
selected_company = DEFAULT_COMPANY
selector_company: list[str] = []
selected_year: str = None
selector_year: list[str] = []
company_sector: str = None
company_upe_name: str = ""

df_selected_company: pd.DataFrame = None
df_count_company: pd.DataFrame = None

# Viz store map[viz_id,viz_dict]
# Important for taipy bindings
# Use Viz.init on each page with set of viz_id
viz: dict[str, dict] = Viz.init(
    (
        "company_sector",
        "company_upe_name",
        "company_nb_reports",
        "company_transparency_score",

        "fin_transparency_score",
        "fin_transparency_score_over_time_details",

        "fin_key_financials_kpis",
        "fin_jurisdictions_top_revenue",

        "fin_pretax_profit_and_employees_rank",
        "fin_pretax_profit_and_profit_per_employee",
    )
)


# Initialize state (Taipy callback function)
# Called by main.py/on_init
def on_init(state: State):
    # print('COMPANY ON INIT...')
    # print(f'COMPANY STATE ID {get_state_id(state)}')

    init_state(state)

    # print('COMPANY ON INIT...END')


def init_state(state: State):
    with state as s:
        # Path to image
        s.company_image_path = company_image_path

        s.selected_company = selected_company
        # print(f'company state selected_company:{s.selected_company}')

        # Performance: Done once in main.py
        # s.data = data
        # print(f'company state data:{s.data.head()}')

        # List companies to populate selector
        s.selector_company = list(np.sort(s.data["mnc"].astype(str).unique()))
        # print(f'company state selector_company:{s.selector_company}')

        s.viz = viz

    update_full(state)


def update_full(state: State):
    with state as s:
        update_state(s)
        update_viz(s)


def update_state(state: State):
    # Create a filtered DataFrame with selected company
    state.df_selected_company = state.data[state.data["mnc"]
                                           == state.selected_company]
    # print(f'company state df_selected_company:{state.df_selected_company.head()}')

    # List years to populate selector and initialise selected year
    state.selector_year = state.df_selected_company["year"].unique().astype(
        str).tolist()
    # print(f'company state selector_year:{state.selector_year}')
    state.selected_year = max(state.selector_year)
    # print(f'company state selected_year:{state.selected_year}')

    # Calculate number of reports for all companies
    state.df_count_company = algo.number_of_tracked_reports_over_time_company(
        state.df_selected_company)
    # print(f'company state df_count_company:{state.df_count_company.head()}')

    # Calculate sector, upe_code for selected company
    state.company_sector = list(
        state.df_selected_company["sector"].unique())[0]
    # print(f'company state company_sector:{state.company_sector}')
    state.company_upe_name = state.df_selected_company["upe_name"].unique()[0]
    # print(f'company state company_upe_name:{state.company_upe_name}')


def update_viz(state: State):
    update_viz_company(state)
    update_viz_year(state)


def update_viz_company(state: State):
    # print(f'update viz company : {state.selected_company}')

    id = "company_sector"
    state.viz[id] = Viz(id=id,
                        state=state,
                        data=state.company_sector,
                        title="Sector"
                        ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    id = "company_upe_name"
    state.viz[id] = Viz(id=id,
                        state=state,
                        data=state.company_upe_name,
                        title="Headquarter"
                        ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    id = "company_nb_reports"
    state.viz[id] = Viz(id=id,
                        state=state,
                        data=algo.number_of_tracked_reports_company(
                            state.df_selected_company),
                        title="Number of reports"
                        ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    id = "company_transparency_score"
    state.viz[id] = Viz(id=id,
                        state=state,
                        data=algo.display_transparency_score(
                            state.data, state.selected_company),
                        title="Transparency Score",
                        sub_title="average over all reports"
                        ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    # Ex Viz 6
    # id="company_transparency_more"
    # state.viz[id] = Viz(id=id,
    #                     state=state,
    #                     data=state.df_selected_company,
    #                     title="More on transparency",
    #                     sub_title=""
    #                 ).to_state()
    # # print(f'update viz id:{id} title:{state.viz[id].title}')


def update_viz_year(state: State):
    # # same order as previous code
    # print(f'update viz financial : {state.selected_company}')

    # Transparency
    id = "fin_transparency_score"
    state.viz[id] = Viz(id=id,
                        state=state,
                        data=algo.display_transparency_score(
                            state.data, state.selected_company, int(state.selected_year)),
                        title="Transparency Score",
                        sub_title=f"selected fiscal year : {
                            state.selected_year}"
                        ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    id = "fin_transparency_score_over_time_details"
    state.viz[id] = Viz(id=id,
                        state=state,
                        data=algo.display_transparency_score_over_time_details(
                            state.data, state.selected_company),
                        title="Transparency score over time ",
                        ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    # Profile
    id = "fin_key_financials_kpis"
    state.viz[id] = Viz(id=id,
                        state=state,
                        data=algo.display_company_key_financials_kpis(
                            state.data, state.selected_company, int(state.selected_year)),
                        title="Key metrics",
                        sub_title=f"selected fiscal year : {
                            state.selected_year}"
                        ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    id = "fin_jurisdictions_top_revenue"
    state.viz[id] = Viz(id=id,
                        state=state,
                        fig=algo.display_jurisdictions_top_revenue(
                            state.data, state.selected_company, int(state.selected_year)),
                        title="Distribution of revenues across countries",
                        sub_title=f"selected fiscal year : {
                            state.selected_year}"
                        ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    # Distribution
    id = "fin_pretax_profit_and_employees_rank"
    state.viz[id] = Viz(id=id,
                        state=state,
                        fig=algo.display_pretax_profit_and_employees_rank(
                            state.data, state.selected_company, int(state.selected_year)),
                        title="% profit and employees by country",
                        sub_title=f"selected fiscal year : {
                            state.selected_year}"
                        ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    id = "fin_pretax_profit_and_profit_per_employee"
    state.viz[id] = Viz(id=id,
                        state=state,
                        fig=algo.display_pretax_profit_and_profit_per_employee(
                            state.data, state.selected_company, int(state.selected_year)),
                        title="% profit and profit / employee by country",
                        sub_title=f"selected fiscal year : {
                            state.selected_year}"
                        ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    # Ex Viz 17
    # id = "fin_profit_and_employee_breakdown"
    # state.viz[id] = Viz(id=id,
    #                     state=state,
    #                     data=algo.display_profit_and_employee_breakdown(state.data, state.selected_company, int(state.selected_year)),
    #                     title="% profits, % employees and profit / employee",
    #                     sub_title="domestic vs. havens vs. non havens, selected fiscal year"
    #                 ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    # Ex Viz 18
    # id = "fin_related_and_unrelated_revenues_breakdown"
    # algo_data, algo_fig = algo.display_related_and_unrelated_revenues_breakdown(state.data, state.selected_company, int(state.selected_year))
    # state.viz[id] = Viz(id=id,
    #                     state=state,
    #                     data=algo_data,
    #                     fig=algo_fig,
    #                     title= "Breakdown of revenue between unrelated and related revenue",
    #                     sub_title=f"domestic vs. havens vs. non havens, selected fiscal year: {state.selected_year}",
    #                 ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    # Ex Viz 19
    # id = "fin_tax_haven_used_by_company"
    # _, algo_data = algo.tax_haven_used_by_company(state.df_selected_company)
    # state.viz[id] = Viz(id=id,
    #                     state=state,
    #                     data=algo_data,
    #                     title="Profits, employees and revenue breakdown by tax haven",
    #                     sub_title=f"selected fiscal year : {state.selected_year}",
    #                 ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

    # Ex Viz 21
    # id = "fin_tax_havens_use_evolution"
    # state.viz[id] = Viz(id=id,
    #                     state=state,
    #                     data=pd.DataFrame.from_dict(algo.compute_tax_havens_use_evolution(state.data, state.selected_company)), # no reset_index() ?
    #                     title="Percentage of profits, percentage of employees and profit per employees over time ",
    #                     sub_title=f"domestic vs. havens vs. non havens, selected fiscal year: {state.selected_year}",
    #                 ).to_state()
    # print(f'update viz id:{id} title:{state.viz[id].title}')

# Update data and figures when the selected company changes


def on_change_company(state: State):
    # print("Chosen company: ", state.selected_company)
    update_full(state)


# Update data and figures when the selected year changes
def on_change_year(state: State):
    # print("Chosen year: ", state.selected_year)
    update_viz_year(state)


# Generate page from Markdown file
company_md = Markdown(f"{cfg.PAGES}/company/company.md")
    