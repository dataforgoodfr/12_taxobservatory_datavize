import io

import numpy as np
import pandas as pd
from taipy.gui import Markdown, download

from app import algo
from app.data.data import data

# Path to image
header_right_image_path = "images/pexels-ingo-joseph-1880351.png"

# Initialize selected company and year
selected_company = "SHELL"
selected_year = 2020

# Create a filtered DataFrame with selected company
df_selected_company = data[data["mnc"] == selected_company]

# List companies to populate selector
colname_company = "mnc"
selector_company = list(np.sort(data[colname_company].astype(str).unique()))

# List years to populate selector
colname_year = "year"
selector_year = list(np.sort(data[colname_year].astype(str).unique()))

# Calculate number of reports for all companies
df_count_company = algo.number_of_tracked_reports_over_time_company(df_selected_company)

# Calculate sector, upe_code and number of reports for selected company
company_sector = list(df_selected_company["sector"].unique())[0]
company_upe_code = df_selected_company["upe_code"].unique()[0]
number_of_tracked_reports_company = algo.number_of_tracked_reports_company(df_selected_company)


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


def download_viz1(state):
    download_el(state, viz1)


def download_viz2(state):
    download_el(state, viz2)


def download_viz3(state):
    download_el(state, viz3)


def download_viz4(state):
    download_el(state, viz4)


def download_viz5(state):
    download_el(state, viz5)


def download_viz6(state):
    download_el(state, viz6)


def download_viz_26(state):
    download_el(state, viz_26)


def download_viz_13_key_metric(state):
    download_el(state, viz_13_key_metric)


def download_viz_14(state):
    download_el(state, viz_14)


def download_viz_15(state):
    download_el(state, viz_15)


def download_viz_16(state):
    download_el(state, viz_16)


def download_viz_17(state):
    download_el(state, viz_17)


def download_viz_18(state):
    download_el(state, viz_18)


def download_viz_19(state):
    download_el(state, viz_19)


def download_viz_21(state):
    download_el(state, viz_21)


# Generate visualizations
viz1 = {
    "data": company_sector,
    "title": "Sector",
    "sub_title": "",
    "on_action": download_viz1
}

viz2 = {
    "data": company_upe_code,
    "title": "Headquarter",
    "sub_title": "",
    "on_action": download_viz2
}

viz3 = {
    "data": number_of_tracked_reports_company,
    "title": "Reports",
    "sub_title": "CbC reports tracked",
    "on_action": download_viz3
}

viz4 = {
    'data': number_of_tracked_reports_company,
    'title': "CbC Transparency Grade",
    'sub_title': "average over all reports",
    'on_action': download_viz4
}

viz5 = {
    'data': number_of_tracked_reports_company,
    'title': "CbC Transparency  Grade",
    'sub_title': "selected fiscal year",
    'on_action': download_viz5
}

viz6 = {
    "data": df_selected_company,
    "title": "More on transparency (tbd)",
    "sub_title": "",
    "on_action": download_viz6
}

# viz26
data_viz_26 = algo.compute_transparency_score(data, selected_company)
viz_26 = {
    "data": data_viz_26,
    "title": "Transparency score over time ",
    "sub_title": "",
    "on_action": download_viz_26
}

# viz13
data_key_metric = algo.compute_company_key_financials_kpis(
    data, selected_company, int(selected_year))
data_viz_13 = pd.DataFrame.from_dict(data_key_metric).reset_index()
viz_13_key_metric = {
    "data": data_viz_13,
    "title": "Key metrics",
    "sub_title": f"Selected fiscal year ({selected_year})",
    "on_action": download_viz_13_key_metric
}

# viz14
data_viz_14 = algo.compute_top_jurisdictions_revenue(
    data, selected_company, int(selected_year))
fig_viz_14 = algo.display_jurisdictions_top_revenue(
    data, selected_company, int(selected_year)
)
viz_14 = {
    "fig": fig_viz_14,
    "data": data_viz_14,
    "title": "Distribution of revenues across partner jurisdictions",
    "sub_title": f"Selected fiscal year{selected_year}",
    "on_action": download_viz_14
}

# viz15
data_viz_15 = algo.compute_pretax_profit_and_employees_rank(
    data, selected_company, int(selected_year))
fig_viz_15 = algo.display_pretax_profit_and_employees_rank(
    data, selected_company, int(selected_year))
viz_15 = {
    "fig": fig_viz_15,
    "data": data_viz_15,
    "title": "% profit and employees by partner jurisdiction",
    "sub_title": "CbC reports tracked",
    "on_action": download_viz_15
}

viz_16 = {
    "data": None,
    "title": "% profit and profit / employee by partner jurisdiction",
    "sub_title": "CbC reports tracked",
    "on_action": download_viz_16
}

viz_17 = {
    "data": None,
    "title": "% profits, % employees and profit / employee",
    "sub_title": "domestic vs. havens vs. non havens, selected fiscal year",
    "on_action": download_viz_17
}

# viz18
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

# viz19
df_selected_company, df_selected_company_th_agg = (
    algo.tax_haven_used_by_company(df_selected_company))
data_viz_19 = df_selected_company_th_agg
viz_19 = {
    "data": data_viz_19,
    "title": "Profits, employees and revenue breakdown by tax haven",
    "sub_title": "selected fiscal year",
    "on_action": download_viz_19
}

# viz21
data_viz_21_dict = algo.compute_tax_havens_use_evolution(
    df=data, company=selected_company)
data_viz_21 = pd.DataFrame.from_dict(data_viz_21_dict)
print(data_viz_21)
viz_21 = {
    "data": data_viz_21,
    "title": "Percentage of profits, percentage of employees and profit per employees over time ",
    "sub_title": "domestic vs. havens vs. non havens, selected fiscal year",
    "on_action": download_viz_21,
}


# Update functions
def update_viz1(state):
    state.viz1["data"] = state.company_sector


def update_viz2(state):
    state.viz2["data"] = state.company_upe_code


def update_viz3(state):
    state.viz3["data"] = state.number_of_tracked_reports_company


def update_viz4(state):
    state.viz4["data"] = state.number_of_tracked_reports_company


def update_viz5(state):
    state.viz5["data"] = state.number_of_tracked_reports_company


def update_viz26(state):
    data_viz_26 = algo.compute_transparency_score(state.data, state.selected_company)
    state.viz_26["data"] = data_viz_26


def update_viz_13(state):
    data_key_metric = algo.compute_company_key_financials_kpis(
        state.data, state.selected_company, int(state.selected_year))
    data_viz_13 = pd.DataFrame.from_dict(data_key_metric)
    state.viz_13_key_metric["data"] = data_viz_13
    state.viz_13_key_metric["sub_title"] = \
        f"Selected fiscal year ({int(state.selected_year)})"


def update_viz_14(state):
    data_viz_14 = algo.compute_top_jurisdictions_revenue(
        state.data, state.selected_company, int(state.selected_year))
    fig_viz_14 = algo.display_jurisdictions_top_revenue(
        state.data, state.selected_company, int(state.selected_year))
    state.viz_14["fig"] = fig_viz_14
    state.viz_14["data"] = data_viz_14
    state.viz_14["sub_title"] = f"Selected fiscal year {selected_year}"


# Update data and figures when the selected company changes
def on_change_company(state):
    print("Chosen company: ", state.selected_company)

    state.df_selected_company = data[data["mnc"] == state.selected_company]
    state.df_count_company = algo.number_of_tracked_reports_over_time_company(state.df_selected_company)

    state.company_sector = list(state.df_selected_company["sector"].unique())[0]
    state.company_upe_code = state.df_selected_company["upe_code"].unique()[0]
    state.number_of_tracked_reports_company = (
        algo.number_of_tracked_reports_company(state.df_selected_company))

    update_viz_13(state)
    update_viz_14(state)

    data_viz_15 = algo.compute_pretax_profit_and_employees_rank(
        state.data, state.selected_company, int(state.selected_year))
    fig_viz_15 = algo.display_pretax_profit_and_employees_rank(
        state.data, state.selected_company, int(state.selected_year))

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

    data_viz_26 = algo.compute_transparency_score(state.data, state.selected_company)
    state.viz_26["data"] = data_viz_26

    update_viz1(state)
    # state.viz1["data"'"] = state.company_sector
    state.viz2["data"] = state.company_upe_code
    state.viz3["data"] = state.number_of_tracked_reports_company
    state.viz4["data"] = state.number_of_tracked_reports_company
    state.viz5["data"] = state.number_of_tracked_reports_company

    state.viz_15["fig"] = fig_viz_15
    state.viz_15["data"] = data_viz_15
    state.viz_18["fig"] = fig_viz_18
    state.viz_18["data"] = data_viz_18
    state.viz_19["data"] = data_viz_19
    state.viz_21["data"] = data_viz_21


# Update data and figures when the selected year changes
def on_change_year(state):
    print("Chosen year: ", state.selected_year)
    update_viz_13(state)
    update_viz_14(state)
    data_viz_15 = algo.compute_pretax_profit_and_employees_rank(
        state.data, state.selected_company, int(state.selected_year))
    fig_viz_15 = algo.display_pretax_profit_and_employees_rank(
        state.data, state.selected_company, int(state.selected_year))
    state.viz_15["fig"] = fig_viz_15
    state.viz_15["data"] = data_viz_15

    data_viz_18_dict = algo.compute_related_and_unrelated_revenues_breakdown(
        state.data, state.selected_company, int(state.selected_year))
    data_viz_18 = pd.DataFrame.from_dict(data_viz_18_dict, orient='index').reset_index()
    fig_viz_18 = algo.display_related_and_unrelated_revenues_breakdown(
        state.data, state.selected_company, int(state.selected_year)
    )
    state.viz_18["fig"] = fig_viz_18
    state.viz_18["data"] = data_viz_18


# Generate page from Markdown file
company_md = Markdown("pages/company/company.md")
