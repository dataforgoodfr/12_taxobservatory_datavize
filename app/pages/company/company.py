import io

import numpy as np
import pandas as pd
from taipy.gui import Markdown, download

from app import algo
from app.data.data import data

# Path to image
company_image_path = "app/images/pexels-ingo-joseph-1880351.png"


# Initialize selected company
selected_company = "SHELL"

# Create a filtered DataFrame with selected company
df_selected_company = data[data["mnc"] == selected_company]

# List companies to populate selector
colname_company = "mnc"
selector_company = list(np.sort(data[colname_company].astype(str).unique()))

# List years to populate selector and initialise selected year
selector_year = data.loc[data["mnc"] == selected_company, "year"].unique().astype(str).tolist()
selected_year = max(data.loc[data["mnc"] == selected_company, "year"].unique().tolist())

# Calculate number of reports for all companies
df_count_company = algo.number_of_tracked_reports_over_time_company(df_selected_company)

# Calculate sector, upe_code for selected company
company_sector = list(df_selected_company["sector"].unique())[0]
company_upe_name = df_selected_company["upe_name"].unique()[0]

# Generate the digits, save them in a CSV file content, and trigger a download action
# so the user can retrieve them
def download_el(state, viz):
    buffer = io.StringIO()
    data = viz["data"]
    if type(data) == pd.DataFrame:
        data.to_csv(buffer)
    else:
        buffer.write(state["sub_title"] + "\n" + str(data))
    download(state, content=bytes(buffer.getvalue(), "UTF-8"), name="data.csv")


# Viz 1
def update_viz_1(state):
    state.viz_1 = viz_1.copy()
    state.viz_1["data"] = state.company_sector


def download_viz_1(state):
    download_el(state, viz_1)


viz_1 = {
    "data": company_sector,
    "title": "Sector",
    # Used for responsive to preserve layout
    "sub_title": "------------ --------- ---------",
    "on_action": download_viz_1
}


# Viz 2
def download_viz_2(state):
    download_el(state, viz_2)


def update_viz_2(state):
    state.viz_2 = viz_2.copy()
    state.viz_2["data"] = state.company_upe_name


viz_2 = {
    "data": company_upe_name,
    "title": "Headquarter",
    # Used for responsive to preserve layout
    "sub_title": "------------ --------- ---------",
    "on_action": download_viz_2
}


# Viz 3
def download_viz_3(state):
    download_el(state, viz_3)


def update_viz_3(state):
    state.viz_3 = viz_3.copy()
    state.viz_3["data"] = algo.number_of_tracked_reports_company(state.df_selected_company)


viz_3 = {
    "data": algo.number_of_tracked_reports_company(df_selected_company),
    "title": "Number of reports",
    # Used for responsive to preserve layout
    "sub_title": "------------ --------- ---------",
    "on_action": download_viz_3
}


# Viz 4
def download_viz_4(state):
    download_el(state, viz_4)


def update_viz_4(state):
    state.viz_4 = viz_4.copy()
    state.viz_4["data"] = algo.display_transparency_score(
        state.data, state.selected_company)


viz_4 = {
    'data': algo.display_transparency_score(data, selected_company),
    'title': "Transparency Score",
    'sub_title': "average over all reports",
    'on_action': download_viz_4
}


# Viz 5
def download_viz_5(state):
    download_el(state, viz_5)


def update_viz_5(state):
    state.viz_5 = viz_5.copy()
    state.viz_5["data"] = algo.display_transparency_score(
        state.data, state.selected_company, int(state.selected_year))
    state.viz_5["sub_title"] = f"selected fiscal year : {state.selected_year}"


viz_5 = {
    'data': algo.display_transparency_score(data, selected_company, selected_year),
    'title': "Transparency  Score",
    'sub_title': f"selected fiscal year : {selected_year}",
    'on_action': download_viz_5
}


# Viz 6
def download_viz_6(state):
    download_el(state, viz_6)


viz_6 = {
    "data": df_selected_company,
    "title": "More on transparency",
    "sub_title": "",
    "on_action": download_viz_6
}


# Viz 13
def download_viz_13(state):
    download_el(state, viz_13)


def update_viz_13(state):
    state.viz_13 = viz_13.copy()
    state.viz_13["data"] = algo.display_company_key_financials_kpis(
        state.data, state.selected_company, int(state.selected_year))
    state.viz_13["sub_title"] = f"selected fiscal year : {state.selected_year}"


viz_13 = {
    "data": algo.display_company_key_financials_kpis(data, selected_company, selected_year),
    "title": "Key metrics",
    "sub_title": f"selected fiscal year : {selected_year}",
    "on_action": download_viz_13
}


# Viz 14
def download_viz_14(state):
    download_el(state, viz_14)


def update_viz_14(state):
    state.viz_14 = viz_14.copy()
    state.viz_14["fig"] = algo.display_jurisdictions_top_revenue(
        state.data, state.selected_company, int(state.selected_year))
    state.viz_14["sub_title"] = f"selected fiscal year : {state.selected_year}"


viz_14 = {
    "fig": algo.display_jurisdictions_top_revenue(data, selected_company, selected_year),
    "title": "Distribution of revenues across countries",
    "sub_title": f"selected fiscal year : {selected_year}",
    "on_action": download_viz_14
}


# Viz 15
def download_viz_15(state):
    download_el(state, viz_15)


def update_viz_15(state):
    state.viz_15 = viz_15.copy()
    state.viz_15["fig"] = algo.display_pretax_profit_and_employees_rank(
        state.data, state.selected_company, int(state.selected_year))
    state.viz_15["sub_title"] = f"selected fiscal year : {state.selected_year}"


viz_15 = {
    "fig": algo.display_pretax_profit_and_employees_rank(data, selected_company, selected_year),
    "title": "% profit and employees by country",
    "sub_title": f"selected fiscal year : {selected_year}",
    "on_action": download_viz_15
}


# Viz 16
def download_viz_16(state):
    download_el(state, viz_16)


viz_16 = {
    "fig": algo.display_pretax_profit_and_profit_per_employee(data, selected_company, selected_year),
    "title": "% profit and profit / employee by country",
    "sub_title": f"selected fiscal year : {selected_year}",
    "on_action": download_viz_16
}


# Viz 17
def download_viz_17(state):
    download_el(state, viz_17)


viz_17 = {
    "data": None,
    "title": "% profits, % employees and profit / employee",
    "sub_title": "domestic vs. havens vs. non havens, selected fiscal year",
    "on_action": download_viz_17
}


# Viz 18
def download_viz_18(state):
    download_el(state, viz_18)


data_viz_18_dict = algo.compute_related_and_unrelated_revenues_breakdown(
    data, selected_company, int(selected_year))
data_viz_18 = pd.DataFrame.from_dict(data_viz_18_dict, orient="index").reset_index()
fig_viz_18 = algo.display_related_and_unrelated_revenues_breakdown(
    data, selected_company, int(selected_year)
)
viz_18 = {
    "fig": fig_viz_18,
    "data": data_viz_18,
    "title": "Breakdown of revenue between unrelated and related revenue",
    "sub_title": "domestic vs. havens vs. non havens, selected fiscal year",
    "on_action": download_viz_18
}


# Viz 19
def download_viz_19(state):
    download_el(state, viz_19)


def update_viz_16(state):
    state.viz_16 = viz_16.copy()
    state.viz_16["fig"] = algo.display_pretax_profit_and_profit_per_employee(
        state.data, state.selected_company, int(state.selected_year))
    state.viz_16["sub_title"] = f"selected fiscal year : {state.selected_year}"


df_selected_company, df_selected_company_th_agg = (
    algo.tax_haven_used_by_company(df_selected_company))
data_viz_19 = df_selected_company_th_agg
viz_19 = {
    "data": data_viz_19,
    "title": "Profits, employees and revenue breakdown by tax haven",
    "sub_title": "selected fiscal year",
    "on_action": download_viz_19
}


# Viz 21
def download_viz_21(state):
    download_el(state, viz_21)


data_viz_21_dict = algo.compute_tax_havens_use_evolution(
    df=data, company=selected_company)
data_viz_21 = pd.DataFrame.from_dict(data_viz_21_dict)
viz_21 = {
    "data": data_viz_21,
    "title": "Percentage of profits, percentage of employees and profit per employees over time ",
    "sub_title": "domestic vs. havens vs. non havens, selected fiscal year",
    "on_action": download_viz_21,
}


# Viz 26
def download_viz_26(state):
    download_el(state, viz_26)


def update_viz_26(state):
    state.viz_26 = viz_26.copy()
    state.viz_26["data"] = algo.display_transparency_score_over_time_details(
        data, state.selected_company)


viz_26 = {
    "data": algo.display_transparency_score_over_time_details(data, selected_company),
    "title": "Transparency score over time ",
    "sub_title": "------------ --------- ---------",
    "on_action": download_viz_26
}


# Update data and figures when the selected company changes
def on_change_company(state):
    print("Chosen company: ", state.selected_company)
    state.selected_company = state.selected_company

    # Update selected year and available years
    state.selector_year = data.loc[data["mnc"] == state.selected_company, "year"].unique().astype(str).tolist()
    state.selected_year = max(data.loc[data["mnc"] == state.selected_company, "year"].unique().tolist())
    print("Available years :", state.selected_year)

    state.df_selected_company = data[data["mnc"] == state.selected_company]
    state.df_count_company = algo.number_of_tracked_reports_over_time_company(state.df_selected_company)

    # Update content of page
    state.company_sector = list(state.df_selected_company["sector"].unique())[0]
    state.company_upe_name = state.df_selected_company["upe_name"].unique()[0]

    update_viz_3(state)
    update_viz_4(state)
    update_viz_5(state)
    update_viz_13(state)
    update_viz_14(state)
    update_viz_15(state)
    update_viz_16(state)
    update_viz_26(state)

    data_viz_18_dict = algo.compute_related_and_unrelated_revenues_breakdown(
        state.data, state.selected_company, int(state.selected_year))
    data_viz_18 = pd.DataFrame.from_dict(data_viz_18_dict, orient="index").reset_index()
    fig_viz_18 = algo.display_related_and_unrelated_revenues_breakdown(
        state.data, state.selected_company, int(state.selected_year)
    )

    df_selected_company, df_selected_company_th_agg = (
        algo.tax_haven_used_by_company(state.df_selected_company))
    data_viz_19 = df_selected_company_th_agg

    data_viz_21_dict = algo.compute_tax_havens_use_evolution(
        df=state.data, company=state.selected_company)
    data_viz_21 = pd.DataFrame.from_dict(data_viz_21_dict)

    update_viz_1(state)
    # state.viz1["data"'"] = state.company_sector
    state.viz_2 = viz_2.copy()
    state.viz_18 = viz_18.copy()
    state.viz_19 = viz_19.copy()
    state.viz_21 = viz_21.copy()
    
    state.viz_2["data"] = state.company_upe_name
    state.viz_18["fig"] = fig_viz_18
    state.viz_18["data"] = data_viz_18
    state.viz_19["data"] = data_viz_19
    state.viz_21["data"] = data_viz_21


# Update data and figures when the selected year changes
def on_change_year(state):
    print("Chosen year: ", state.selected_year)

    state.selected_year = state.selected_year
    state.selector_year = state.selector_year

    # Update content of page
    update_viz_5(state)
    update_viz_13(state)
    update_viz_14(state)
    update_viz_15(state)
    update_viz_16(state)

    data_viz_18_dict = algo.compute_related_and_unrelated_revenues_breakdown(
        state.data, state.selected_company, int(state.selected_year))
    data_viz_18 = pd.DataFrame.from_dict(data_viz_18_dict, orient='index').reset_index()
    fig_viz_18 = algo.display_related_and_unrelated_revenues_breakdown(
        state.data, state.selected_company, int(state.selected_year)
    )
    state.viz_18 = viz_18.copy()
    state.viz_18["fig"] = fig_viz_18
    state.viz_18["data"] = data_viz_18


# Generate page from Markdown file
company_md = Markdown("app/pages/company/company.md")
