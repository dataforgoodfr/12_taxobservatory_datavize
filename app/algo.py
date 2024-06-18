"""
This module contains functions to compute and/or display the visualizations, defined by EU Tax Observatory, which
are needed in Taxplorer tool. Below functions will be used in different pages of the website.
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import humanize
from wordcloud import WordCloud, get_single_color_func

# Define color sequence for plots
COLOR_SEQUENCE = ["#D9D9D9", "#1E2E5C"]


# Viz 1 : Number of tracked reports
def number_of_tracked_reports(
    df: pd.DataFrame, filter_name: str = None, filter_value: str = None
) -> int:
    """Calculate the number of tracked reports with possibility to filter on company name, sector or headquarter
    location.

    Args:
        df (pd.DataFrame): CbCRs database.
        filter_name (str, optional): Filter to apply, could be "mnc", "sector" or "upe_name". Defaults to None.
        filter_value (str, optional): Value to filter with. Defaults to None.

    Returns:
        int: number of tracked reports.
    """

    # Initialise available filters
    filter_values = [None, "mnc", "sector", "upe_name"]

    # Raise an error if "filter_value" not in list
    if filter_name not in filter_values:
        raise ValueError(f"Filter '{filter_name}' is not a valid filter.")

    # Compute number of reports
    if filter_name:
        n_reports = (
            df.loc[df[filter_name] == filter_value].groupby("mnc")["year"].nunique().sum()
        )
    else:
        n_reports = df.groupby("mnc")["year"].nunique().sum()

    return int(n_reports)


# Viz 2 : Number of tracked reports over time
def number_of_tracked_reports_over_time(
    df: pd.DataFrame, filter_name: str = None, filter_value: str = None
) -> go.Figure:
    """Compute and plot the number of tracked reports over time with possibility to filter on company name, sector or
    headquarter location.

    Args:
        df (pd.DataFrame): CbCRs database.
        filter_name (str, optional): Filter to apply, could be "mnc", "sector" or "upe_name". Defaults to None.
        filter_value (str, optional): Value to filter with. Defaults to None.

    Returns:
        go.Figure: number of tracked reports over time in a Plotly figure.
    """

    # Initialise available filters
    filter_values = [None, "mnc", "sector", "upe_name"]

    # Raise an error if "filter_value" not in list
    if filter_name not in filter_values:
        raise ValueError(f"Filter '{filter_name}' is not a valid filter.")

    # Compute number of reports
    if filter_name:
        data = (
            df.loc[df[filter_name] == filter_value]
            .groupby("year")["mnc"]
            .nunique()
            .reset_index()
        )
    else:
        data = df.groupby("year")["mnc"].nunique().reset_index()

    # Create figure
    fig = px.bar(
        data, x="year", y="mnc", color_discrete_sequence=COLOR_SEQUENCE, text_auto=True
    )

    # Force position and color of bar values
    fig.update_traces(textposition="outside", textfont=dict(color="black"))

    # Update layout settings
    fig.update_layout(
        autosize=True,
        height=360,
        font_family="Roboto",
        title=None,
        xaxis=dict(title=None, tickvals=data["year"].unique()),
        yaxis=dict(
            title=None,
            visible=False,
        ),
        plot_bgcolor="white",
        margin=dict(l=0, r=0, b=0, t=0),
    )

    # Define style of hover on bars
    fig.update_traces(
        hovertemplate="%{x} : %{y} reports",
    )

    return go.Figure(fig)


# Viz 3 : Number of tracked mnc
def number_of_tracked_mnc(
    df: pd.DataFrame, filter_name: str = None, filter_value: str = None
) -> int:
    """Calculate the number of tracked reports with possibility to filter on company name, sector or headquarter
    location.

    Args:
        df (pd.DataFrame): CbCRs database.
        filter_name (str, optional): Filter to apply, could be "sector" or "upe_name". Defaults to None.
        filter_value (str, optional): Value to filter with. Defaults to None.

    Returns:
        int: number of companies in the database.
    """

    # Initialise available filters
    filter_values = [None, "sector", "upe_name"]

    # Raise an error if "filter_value" not in list
    if filter_name not in filter_values:
        raise ValueError(f"Filter '{filter_name}' is not a valid filter.")

    # Compute number of reports
    if filter_name:
        n_company = df.loc[df[filter_name] == filter_value, "mnc"].nunique()
    else:
        n_company = df["mnc"].nunique()

    return int(n_company)


# Viz 4 : Breakdown of reports by sector
def breakdown_of_reports_by_sector(df):
    # Dataframe called df
    df_reports_per_sector_year = (
        df.groupby(["sector", "year"])["mnc"].nunique().reset_index(name="unique_company_count")
    )

    # Aggregate the counts of unique companies across all years for each sector
    df_reports_per_sector = (
        df_reports_per_sector_year.groupby("sector")["unique_company_count"].sum().reset_index()
    )

    # Calculate the total count of unique companies across all sectors
    total_companies = df_reports_per_sector["unique_company_count"].sum()

    # Calculate the percentage of each sector's count relative to the total count and round to 2 decimals
    df_reports_per_sector["percent"] = (
        (df_reports_per_sector["unique_company_count"] / total_companies) * 100
    ).round(2)

    # Sort the DataFrame by the count of unique companies in ascending order
    df_reports_per_sector = df_reports_per_sector.sort_values(
        by="unique_company_count", ascending=True
    )

    return df_reports_per_sector


def breakdown_of_reports_by_sector_viz(df_reports_per_sector):
    # Plotting the horizontal bar chart with Plotly Express
    fig = px.bar(
        df_reports_per_sector,
        y="sector",
        x="percent",
        orientation="h",  # Horizontal orientation
        title="Breakdown of Reports by Sector (All Years)",
        labels={"percent": "Percentage of Companies (%)", "sector": "Sector"},
        text="percent",  # Show the percentage as text label
        hover_data={"unique_company_count": True, "percent": ":.2f%"},
        # Add tooltip for count and rounded percentage
    )

    # Update layout to display the title above the chart
    fig.update_layout(
        title="Breakdown of Reports by Sector",
        title_x=0.5,
        title_y=0.9,  # Adjust position
        title_font_size=20,
    )  # Adjust font size

    # Show the horizontal bar chart
    return go.Figure(fig)


# Viz 5 : Breakdown of reports by hq country
def breakdown_of_reports_by_hq_country(df):
    # Group the DataFrame by 'upe_name' (HQ country) and 'year' and count the number of unique companies for each HQ country and year
    df_reports_per_country_year = (
        df.groupby(["upe_name", "year"])["mnc"]
        .nunique()
        .reset_index(name="unique_company_count")
    )

    # Aggregate the counts of unique companies across all years for each HQ country
    df_reports_per_country = (
        df_reports_per_country_year.groupby("upe_name")["unique_company_count"]
        .sum()
        .reset_index()
    )

    # Calculate the total count of unique companies across all HQ countries
    total_companies = df_reports_per_country["unique_company_count"].sum()

    # Calculate the percentage of each HQ country's count relative to the total count and round to 2 decimals
    df_reports_per_country["percent"] = (
        (df_reports_per_country["unique_company_count"] / total_companies) * 100
    ).round(2)

    # Sort the DataFrame by the count of unique companies in ascending order
    df_reports_per_country = df_reports_per_country.sort_values(
        by="unique_company_count", ascending=True
    )

    return df_reports_per_country


def breakdown_of_reports_by_hq_country_viz(df_reports_per_country):
    # Plotting the horizontal bar chart with Plotly Express
    fig = px.bar(
        df_reports_per_country,
        y="upe_name",
        x="percent",
        orientation="h",  # Horizontal orientation
        title="Breakdown of Reports by HQ Country over Time",
        labels={"percent": "Percentage of Companies (%)", "upe_name": "HQ Country"},
        text="percent",  # Show the percentage as text label
        hover_data={"unique_company_count": True, "percent": ":.2f%"},
        # Add tooltip for count and rounded percentage
    )

    # Update layout to display the title above the chart
    fig.update_layout(
        title="Breakdown of Reports by HQ Country over Time",
        title_x=0.5,
        title_y=0.95,  # Adjust position
        title_font_size=20,
    )  # Adjust font size

    # Show the horizontal bar chart
    # fig.show()
    return go.Figure(fig)


# Viz 6 : Breakdown of reports by sector over time
def breakdown_of_reports_by_sector_over_time(df):
    # df_reports_per_sector_over_time = df
    # return df_reports_per_sector_over_time

    # Step 1: Determine the top 10 sectors that released reports
    top_10_sectors = df["sector"].value_counts().nlargest(10).index.tolist()

    # Step 2: Group all other sectors as "Others"
    df["Sectors"] = df["sector"].apply(lambda x: x if x in top_10_sectors else "Others")

    # Step 3: Group the DataFrame by 'year', 'Sectors', and count the number of unique companies for each year and sector
    df_reports_per_year_sector = (
        df.groupby(["year", "Sectors"])["mnc"]
        .nunique()
        .reset_index(name="unique_company_count")
    )

    # Sort sectors alphabetically
    df_reports_per_year_sector = df_reports_per_year_sector.sort_values(
        by="Sectors", ascending=False
    )

    return df_reports_per_year_sector, top_10_sectors


def breakdown_of_reports_by_sector_over_time_viz(df_reports_per_year_sector, top_10_sectors):
    # Define the order of sectors for the stacked bar chart and legend, reversed
    chart_order = ["Others"] + top_10_sectors[::-1]
    legend_order = ["Others"] + top_10_sectors[::-1]

    # Plotting the bar chart using Plotly Express
    fig = px.bar(
        df_reports_per_year_sector,
        x="year",
        y="unique_company_count",
        color="Sectors",
        title="Breakdown of Reports by Sector over Time",
        labels={"unique_company_count": "Number of Companies Reporting", "year": "Year"},
        barmode="stack",
        category_orders={"Sectors": chart_order},
    )

    # Reverse the order of legend items
    fig.update_layout(legend=dict(traceorder="reversed"))

    # Adjusting the legend order and formatting the legend labels
    for i, trace in enumerate(fig.data):
        trace.name = legend_order[i]
        # Change color of the "Others" bar to grey
        if trace.name == "Others":
            trace.marker.color = "grey"

    # Show the plot
    # fig.show()
    return go.Figure(fig)


# Viz 7 : Breakdown of reports by hq country over time
# TODO add code


# Viz 8 : Breakdown of MNC by sector
# TODO add code


# Viz 9 : Breakdown of MNC by HQ country
# TODO add code


# Viz 10/11 : Breakdown of MNC by sector
# TODO add code


# Viz 11 : Breakdown of MNC by HQ country
# TODO add code


# Viz 12 : available reports by company
def compute_company_available_reports(df: pd.DataFrame, company: str) -> dict:
    """Compute the number of reports tracked for a specific company and the
    available fiscal years.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): company name.

    Returns:
        dict: numbers of reports and fiscal years.
    """
    available_years = df.loc[df["mnc"] == company, "year"].unique()
    n_reports = len(available_years)

    # Convert type of items from 'int' to 'str' in available years list
    years_string_list = [str(year) for year in available_years]

    # Summarize all available years in one string
    if len(years_string_list) == 1:
        years_string = years_string_list[0]
    elif len(years_string_list) > 1:
        years_string = ", ".join(years_string_list[:-1])
        years_string += " and " + years_string_list[-1]

    # Create a dictionnary with the results
    data = {"Company": company, "Reports": n_reports, "Fiscal year(s) available": years_string}

    return data


def display_company_available_reports(
    df: pd.DataFrame, company: str, hide_company: bool = True
) -> pd.DataFrame:
    """Display the number of reports tracked for a specific company and the
    available fiscal years.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): company name.
        hide_company (bool, optional): hide company name in final table. Defaults to True.

    Returns:
        pd.DataFrame: numbers of reports and fiscal years.
    """

    # Compute data
    data = compute_company_available_reports(df=df, company=company)

    # Create the table
    df = pd.DataFrame.from_dict(data=data, orient="index")

    if hide_company:
        return df[1:].style.hide(axis="columns")

    return df.style.hide(axis="columns")


# Viz 13 : Company key financials kpis
def company_key_financials_kpis(
    df: pd.DataFrame, company: str, year: int = None
) -> dict:
    """Compute key financial KPIs for a company in a table.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): company name.
        year (int, optional): fiscal year to filter the results with. Defaults to None.

    Returns:
        pd.DataFrame: table with company key financial KPIs.
    """

    kpis_list = [
        "total_revenues",
        "unrelated_revenues",
        "related_revenues",
        "profit_before_tax",
        "tax_paid",
        "employees",
    ]

    years_list = df.loc[df["mnc"] == company, "year"].unique()

    # Compute sum of kpis
    if not year or year not in years_list:
        df = (
            df.loc[df["mnc"] == company]
            .groupby(["year", "upe_name"], as_index=False)[kpis_list]
            .sum()
        )
    else:
        df = (
            df.loc[(df["mnc"] == company) & (df["year"] == year)]
            .groupby(["year", "upe_name"], as_index=False)[kpis_list]
            .sum()
        )

    # Make financial numbers easily readable with 'humanize' package
    for column in df.columns:
        if column not in ["employees", "upe_name"]:
            df[column] = df[column].apply(
                lambda x: humanize.intword(x) if isinstance(x, (int, float)) else x
            )
            df[column] = "€ " + df[column]
        elif column == "employees":
            df[column] = df[column].astype(int)

    # Remove 'upe_name' and 'year''
    df = df.drop(columns=["upe_name", "year"])

    # Clean columns string
    df.columns = df.columns.str.replace("_", " ").str.capitalize()

    # Transpose DataFrame
    df = df.T.reset_index()

    # Rename columns
    df = df.rename(columns={"index": "Variable", 0: "Value"})

    # Replace 0 values with 'N/A'
    df.loc[df["Value"] == "€ 0", "Value"] = "N/A"

    return df


# Viz 14 : company top jurisdictions for revenue
def top_jurisdictions_revenue(df: pd.DataFrame, company: str, year: int) -> go.Figure:
    """Compute and plot top jurisdictions on their percentage of total revenues.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name
        year (int): Fiscal year.

    Returns:
        go.Figure: Jurisdictions by percentage of total revenues in a Plotly figure.
    """

    df = df.loc[
        (df["mnc"] == company) & (df["year"] == year),
        ["jur_name", "related_revenues", "unrelated_revenues", "total_revenues"],
    ]

    # Calculate missing values in 'total_revenues' if 'related_revenues' and
    # 'unrelated_revenues' are available
    df.loc[
        df["related_revenues"].notna()
        & df["unrelated_revenues"].notna()
        & df["total_revenues"].isna(),
        "total_revenues",
    ] = df["related_revenues"] + df["unrelated_revenues"]

    # Subset DataFrame
    df = df[["jur_name", "total_revenues"]]

    # Remove rows where 'total_revenues' is missing
    df = df.dropna(subset=["total_revenues"])

    # Compute percentage of revenue
    df["total_revenues_%"] = df["total_revenues"] / df["total_revenues"].sum()


    # Sort jurisdictions by percentage of total revenues
    df = df.sort_values(by="total_revenues_%")

    # Create figure
    fig = px.bar(
        df,
        x="total_revenues_%",
        y="jur_name",
        orientation="h",
        color_discrete_sequence=COLOR_SEQUENCE,
        text_auto=".1%",
    )

    # Set figure height (min. 480) depending on the number of jurisdictions
    fig_height = max(480, (48 * len(df["jur_name"])))

    # Update layout settings
    fig.update_layout(
        font_family="Roboto",
        xaxis=dict(title="Percentage of total revenue", tickformat=".0%"),
        yaxis_title=None,
        plot_bgcolor="white",
        height=fig_height,
        margin=dict(l=0, r=0, t=0, b=0),
    )

    # Define position of text values
    values_positions = [
        "outside" if value <= 0.05 else "inside" for value in df["total_revenues_%"]
    ]

    fig.update_traces(textangle=0, textposition=values_positions, selector=dict(name=""))

    # Define style of hover on bars
    fig.update_traces(
        hovertemplate=("<b>%{hovertext}</b><br><br>% revenue: %{x:.3%}<br>"),
        hovertext=df["jur_name"],
    )

    return go.Figure(fig)


# Viz 15 : company’s % pre-tax profit and % employees by jurisdiction
def pretax_profit_and_employees_rank(
    df: pd.DataFrame, company: str, year: int
) -> go.Figure:
    """Compute and plot jurisdictions percentage of profit before tax and percentage of employees then rank by 
    percentage of profit.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name
        year (int): Fiscal year.

    Returns:
        go.Figure:: rank of jurisdictions with percentage of profit before and percentage of employees in a Plotly 
        figure.
    """

    # Filter rows with selected company/year and subset with necessary features
    features = ["jur_name", "profit_before_tax", "employees"]
    df = df.loc[(df["mnc"] == company) & (df["year"] == year), features]

    # Keep only profitable jurisdictions
    df = df.loc[df["profit_before_tax"] >= 0]

    # Sort jurisdictions by profits
    df = df.sort_values(by="profit_before_tax").reset_index(drop=True)

    # Calculate percentages
    df["profit_before_tax_%"] = df["profit_before_tax"] / df["profit_before_tax"].sum()
    df["employees_%"] = df["employees"] / df["employees"].sum()
    df = df.drop(columns=["profit_before_tax", "employees"])

    # Rename columns
    df = df.rename(columns={"profit_before_tax_%": "% profit", "employees_%": "% employees"})

    # Create figure
    fig = px.bar(
        df,
        x=["% employees", "% profit"],
        y="jur_name",
        barmode="group",
        orientation="h",
        text_auto=".1%",
        color_discrete_sequence=COLOR_SEQUENCE
    )

    # Set figure height (min. 640) depending on the number of jurisdictions
    fig_height = max(480, (48 * len(df["jur_name"])))

    # Set maximum value for x axis
    if not df[["% profit", "% employees"]].isna().all().all():
        max_x_value = max(df[["% profit", "% employees"]].max(axis="columns")) + 0.1
    else:
        max_x_value = 1

    # Update layout settings
    fig.update_layout(
        font_family="Roboto",
        title=None,
        xaxis=dict(title=None, tickformat=".0%", range=[0, max_x_value]),
        yaxis_title=None,
        legend=dict(
            x=0.1, y=1.05, xanchor="center", yanchor="top", title=dict(text=""), orientation="h"
        ),
        plot_bgcolor="white",
        height=fig_height,
        margin=dict(l=0, r=0, t=10, b=0),
    )

    # Add annotations for NaN values where there should have been a bar
    for index, row in df.iterrows():
        if pd.isna(row["% employees"]):
            fig.add_annotation(
                xanchor="left",
                x=0.001,
                y=df.index[index],
                yshift=-10,
                text="Information not provided",
                showarrow=False,
                font=dict(size=12),
            )
        if pd.isna(row["% profit"]):
            fig.add_annotation(
                xanchor="left",
                x=0.001,
                y=df.index[index],
                yshift=10,
                text="Information not provided",
                showarrow=False,
                font=dict(size=12),
            )

    # Loop through each bar trace and hide the text if the value is NaN
    for trace in fig.data:
        values = df[trace.name]
        text_position = ["outside" if not np.isnan(value) else "none" for value in values]
        trace.textposition = text_position

        if trace.name == "% employees":
            trace.hovertemplate = "<b>%{y}</b><br><br>Employees : %{x:.3%}<extra></extra>"
        elif trace.name == "% profit":
            trace.hovertemplate = "<b>%{y}</b><br><br>Profit : %{x:.3%}<extra></extra>"

    return go.Figure(fig)


# Viz 16 : company’s % pre-tax profit and profit per employee
def pretax_profit_and_profit_per_employee(
    df: pd.DataFrame, company: str, year: int
) -> go.Figure:
    """Compute and plot jurisdictions percentage of profit before tax and profit by employee.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name
        year (int): Fiscal year.

    Returns:
        go.Figure: Percentage of profit and profit/employee in a Plotly Figure.
    """
    
    # Filter rows with selected company/year and subset with necessary features
    features = ["jur_name", "profit_before_tax", "employees", "jur_tax_haven"]
    df = df.loc[(df["mnc"] == company) & (df["year"] == year), features]

    # Keep only profitable jurisdictions
    df = df.loc[df["profit_before_tax"] >= 0]

    # Sort jurisdictions by profits
    df = df.sort_values(by="profit_before_tax").reset_index(drop=True)

    # Replace 0 employees by 1
    df.loc[df["employees"] == 0, "employees"] = 1

    # Calculate percentages
    df["profit_before_tax_%"] = df["profit_before_tax"] / df["profit_before_tax"].sum()
    df["profit_per_employee"] = df["profit_before_tax"] / df["employees"]
    df = df.drop(columns=["profit_before_tax", "employees"])

    # Replace bool values of Tax haven by string values
    df["jur_tax_haven"] = df["jur_tax_haven"].map({True: "Tax haven", False: "Non tax haven"})

    # Create figure
    fig = px.scatter(
        df,
        x="profit_before_tax_%",
        y="profit_per_employee",
        size="profit_before_tax_%",
        color="jur_tax_haven",
        color_discrete_sequence=COLOR_SEQUENCE,
        custom_data=["jur_name"],
    )

    # Update layout settings
    fig.update_layout(
        title=None,
        font_family="Roboto",
        autosize=True,
        height=360,
        xaxis=dict(
            title="% profit",
            tickformat=".0%",
        ),
        yaxis=dict(
            title="Profit/employee",
        ),
        legend=dict(
            x=0.1, y=1.05, xanchor="center", yanchor="top", title=dict(text=""), orientation="h"
        ),
        plot_bgcolor="white",
        margin=dict(l=0, r=0, t=0, b=0),
    )

    # Define hover
    fig.update_traces(
        hovertemplate=f"{company} reports %{{x:.1%}} of profit and %{{y:.3s}}€ profits per employee in %{{customdata[0]}}"
    )

    return go.Figure(fig)


# Viz 17 : company’s % pre-tax profit and % employees in TH vs domestic vs non TH
# TODO add code


# Viz 18 : breakdown of revenue between related party and unrelated party in TH vs domestic vs non TH
def compute_related_and_unrelated_revenues_breakdown(
    df: pd.DataFrame, company: str, year: int
) -> dict:
    """Compute related and unrelated revenues in tax heaven, non tax heaven and
    domestic jurisdictions.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name
        year (int): fiscal year to filter the results with.

    Returns:
        dict: revenues percentage for different type of jurisdictions.
    """

    # Filter rows with selected company/year and subset with necessary features
    features = [
        "upe_code",
        "jur_code",
        "jur_name",
        "jur_tax_haven",
        "unrelated_revenues",
        "related_revenues",
    ]

    df = df.loc[(df["mnc"] == company) & (df["year"] == year), features]

    # Drop rows where either unrelated or related revenues are missing
    df = df.dropna(subset=["unrelated_revenues", "related_revenues"])

    # 'total_revenues' is recreated using related and unrelated revenues since the one
    # reported by companies is not always reliable
    df["total_revenues"] = df["unrelated_revenues"] + df["related_revenues"]

    # Create a column to check if 'jur_code' is the domestic country
    df["domestic"] = df.apply(lambda row: row["jur_code"] == row["upe_code"], axis="columns")

    # Compute kpis in a new DataFrame
    data = pd.DataFrame()
    data["tax_haven"] = df.loc[
        df["jur_tax_haven"] == True, ["unrelated_revenues", "related_revenues"]
    ].sum()
    data["non_tax_haven"] = df.loc[
        df["jur_tax_haven"] == False, ["unrelated_revenues", "related_revenues"]
    ].sum()
    data["domestic"] = df.loc[
        df["domestic"] == True, ["unrelated_revenues", "related_revenues"]
    ].sum()

    # Replace values with share (%) of 'unrelated/related revenues'
    data = data.div(data.sum(axis="rows"), axis="columns")

    # Rename indexes
    data = data.rename(
        index={
            "unrelated_revenues": "unrelated_revenues_percentage",
            "related_revenues": "related_revenues_percentage",
        }
    )

    # Convert DataFrame to dictionary
    data = data.to_dict()

    return data


def display_related_and_unrelated_revenues_breakdown(
    df: pd.DataFrame, company: str, year: int
) -> tuple[pd.DataFrame, go.Figure]:
    """Display related and unrelated revenues in tax heaven, non tax heaven and
    domestic jurisdictions.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name
        year (int): fiscal year to filter the results with.
    """

    # Compute data
    data = compute_related_and_unrelated_revenues_breakdown(df=df, company=company, year=year)

    # Create DataFrame
    df = pd.DataFrame.from_dict(data, orient="index")

    # Rename columns and indexes
    df.columns = df.columns.str.replace("_", " ").str.capitalize()
    df.index = df.index.str.replace("_", " ").str.capitalize()

    # Create figure
    fig = px.bar(
        df,
        x=["Unrelated revenues percentage", "Related revenues percentage"],
        y=df.index,
        orientation="h",
        text_auto=".0%",
    )

    # Update layout settings
    fig.update_layout(
        title="Breakdown of revenue",
        xaxis=dict(title=None, tickformat=".0%"),
        yaxis_title=None,
        legend=dict(title=dict(text=""), orientation="h"),
        plot_bgcolor="white",
        width=800,
        height=480,
    )

    # Define position of text values
    for col in ["Unrelated revenues percentage", "Related revenues percentage"]:
        values_positions = ["outside" if value <= 0.05 else "inside" for value in df[col]]

        fig.update_traces(textangle=0, textposition=values_positions, selector=dict(name=col))

    # Add annotation if no values are availables (no bar displayed)
    for i, index in enumerate(df.index):
        if df.loc[index].isna().all():
            fig.add_annotation(
                x=0.5,
                y=df.index[i],
                text="No information to display",
                showarrow=False,
                font=dict(size=13),
            )

    # fig.show()
    return pd.DataFrame.from_dict(data, orient="index"), go.Figure(fig)


# Viz 19 : what are the tax havens being used by the company
def tax_haven_used_by_company(df_selected_company):
    company_upe_code = df_selected_company["upe_code"].unique()[0]
    pc_list = ["employees", "profit_before_tax", "related_revenues"]
    # grouper = df_selected_company.groupby('jur_name')

    df = pd.DataFrame(df_selected_company)

    df_domestic_company = df[df["jur_code"] == company_upe_code]
    df_selected_company_th = df[df["jur_tax_haven"] != "not.TH"]
    df_selected_company_nth = df[df["jur_tax_haven"] == "not.TH"]

    for col in pc_list:
        df.insert(
            len(df_selected_company.columns),
            col + "_domestic_sum",
            df_domestic_company[col].sum(),
        )

        df.insert(
            len(df_selected_company.columns), col + "_th_sum", df_selected_company_th[col].sum()
        )

        df.insert(len(df.columns), col + "_nth_sum", df_selected_company_nth[col].sum())

        df.insert(len(df.columns), col + "_sum", df_selected_company[col].sum())

        df.insert(len(df.columns), col + "_pc", 100 * df[col] / df[col + "_sum"])
        # df_selected_company[col + '_pc'] = 100 * df_selected_company[col] / df_selected_company[col+'_sum']

    df_selected_company_th = df[df["jur_tax_haven"] != "not.TH"]
    df_selected_company_th_agg = df_selected_company_th.groupby(["mnc", "jur_name"]).agg(
        profit_before_tax=("profit_before_tax", "sum"),
        profit_before_tax_pc=("profit_before_tax_pc", "sum"),
        employees_pc=("employees_pc", "sum"),
        employees=("employees", "sum"),
        related_revenues_pc=("related_revenues_pc", "sum"),
    )
    df_selected_company_th_agg = df_selected_company_th_agg.reset_index()
    df_selected_company_th_agg["profit per employee"] = (
        df_selected_company_th_agg["profit_before_tax"]
        / df_selected_company_th_agg["employees"]
    )
    df_selected_company_th_agg["profit per employee"] = df_selected_company_th_agg[
        "profit per employee"
    ].replace([np.inf, -np.inf], None)

    return df_selected_company, df_selected_company_th_agg


# Viz 20 : complete table table showing for all jurisdictions revenues, profits, employees, taxes with % of total for
# each (color code for tax havens)
def company_table(df_selected_company):
    # company_upe_code = df_selected_company['upe_code'].unique()[0]
    pc_list = [
        "employees",
        "profit_before_tax",
        "unrelated_revenues",
        "related_revenues",
        "total_revenues",
        "tax_paid",
    ]

    df = pd.DataFrame(df_selected_company)
    for col in pc_list:
        if col + "_sum" not in df.columns:
            df.insert(len(df.columns), col + "_sum", df[col].sum())

            df.insert(len(df.columns), col + "_pc", 100 * df[col] / df[col + "_sum"])
            # f_selected_company[col + '_sum'] = df_selected_company[col].sum()
            # df_selected_company[col + '_pc'] = 100 * df_selected_company[col] / df_selected_company[col + '_sum']

    # complete table table showing for all jurisdictions revenues, profits, employees, taxes with % of total for each (color code for tax havens)
    df_selected_company_by_jur = df.groupby(["mnc", "jur_name"]).agg(
        related_revenues_pc=("related_revenues_pc", "sum"),
        unrelated_revenues=("unrelated_revenues", "sum"),
        total_revenues=("total_revenues", "sum"),
        profit_before_tax=("profit_before_tax", "sum"),
        employees_pc=("employees_pc", "sum"),
        tax_paid=("tax_paid", "sum"),
        tax_paid_pc=("tax_paid_pc", "sum"),
    )
    return df_selected_company_by_jur.reset_index()


# Viz 21 : evolution of tax havens use over time : % profit vs % employees in TH over time
def compute_tax_havens_use_evolution(df: pd.DataFrame, company: str) -> dict:
    """Compute the evolution of tax havens use by company over time.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name

    Returns:
        dict: tax havens percentage of profits and employees for each year.
    """

    # Filter rows with selected company and subset with necessary features
    features = ["jur_code", "year", "jur_tax_haven", "profit_before_tax", "employees"]
    df = df.loc[(df["mnc"] == company), features]

    # Keep jurisdictions with profitable or missing revenues
    df = df.loc[(df["profit_before_tax"] >= 0) | (df["profit_before_tax"].isna())]

    # For all sum calculations below :
    # - Result NA : all jurisdictions values were NA ;
    # - Result 0 : at least one jurisdiction was reported as 0.

    # Calculate total profit and employees by year and tax haven status
    df = df.groupby(["year", "jur_tax_haven"], as_index=False)[
        ["profit_before_tax", "employees"]
    ].sum(min_count=1)

    # Calculate total profits and employees for each year
    for year in df["year"].unique():
        df.loc[df["year"] == year, "total_profit"] = df.loc[
            df["year"] == year, "profit_before_tax"
        ].sum(min_count=1)
        df.loc[df["year"] == year, "total_employees"] = df.loc[
            df["year"] == year, "employees"
        ].sum(min_count=1)

    # Remove non tax haven jurisdictions
    df = df.loc[df["jur_tax_haven"] == True].reset_index()

    # Calculate percentages
    df["tax_havens_profit_%"] = df["profit_before_tax"] / df["total_profit"]
    df["tax_havens_employees_%"] = df["employees"] / df["total_employees"]

    # Convert necessary data to dictionnary
    data = df[["year", "tax_havens_profit_%", "tax_havens_employees_%"]].to_dict()

    return data


def display_tax_havens_use_evolution(df: pd.DataFrame, company: str):
    """Display the evolution of tax havens use by company over time.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name
    """

    # Compute data
    data = compute_tax_havens_use_evolution(df=df, company=company)

    # Create DataFrame
    df = pd.DataFrame.from_dict(data)

    # Rename columns
    df = df.rename(
        columns={
            "tax_havens_profit_%": "Percentage of profits in tax havens",
            "tax_havens_employees_%": "Percentage of employees in tax havens",
        }
    )

    # Create figure
    fig = px.bar(
        df,
        x="year",
        y=["Percentage of profits in tax havens", "Percentage of employees in tax havens"],
        barmode="group",
        text_auto=".1%",
    )

    # Update layout settings
    fig.update_layout(
        title="Tax havens use in profitables jurisdictions",
        xaxis_title=None,
        yaxis_title=None,
        yaxis_tickformat=".0%",
        legend=dict(title=dict(text=""), orientation="h"),
        plot_bgcolor="white",
        width=800,
        height=480,
    )

    # fig.show()
    return go.Figure(fig)


# Viz 22 : locations of profits booked vs. mean 3Y ETR
# TODO add code


# Viz 24 : mnc tracked
def mnc_tracked(df: pd.DataFrame) -> go.Figure:
    """"Compute and plot the list of company name in a word cloud where the size of the font depends of the number
    of reports available.

    Args:
        df (pd.DataFrame): CbCRs database.

    Returns:
        go.Figure: word cloud with company name  in a Plotly figure.
    """
    
    # Create dictionnary with company name as key and the number of reports as value
    data = df.groupby("mnc")["year"].nunique().to_dict()

    color_func = get_single_color_func("#B8BEDB")

    # Generate the word cloud using the report counts as weights
    wordcloud = WordCloud(
        width=1200, height=800, background_color="white", color_func=color_func
    ).generate_from_frequencies(data)

    # Display the word cloud
    fig = px.imshow(wordcloud)

    # Remove hover on image
    fig.update_traces(hoverinfo="skip", hovertemplate="")

    # Remove colorbar
    fig.update_layout(coloraxis_showscale=False)

    # Remove axis
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)

    # Remove margins
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))

    return go.Figure(fig)


# Viz 25 : company’s average transparency score

# List financial columns
financial_columns = [
    "total_revenues",
    "profit_before_tax",
    "tax_paid",
    "tax_accrued",
    "unrelated_revenues",
    "related_revenues",
    "stated_capital",
    "accumulated_earnings",
    "tangible_assets",
    "employees",
]


def compute_geographic_score(df: pd.DataFrame, company: str, year: int) -> float:
    """Compute component I of transparency score which is the geographic score.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name.
        year (int): fiscal year to filter the results with.

    Returns:
        float: value of the score.
    """

    # Filter rows with selected company and subset with financial columns
    df = df.loc[
        (df["mnc"] == company) & (df["year"] == year),
        ["mnc", "year", "upe_code", "jur_code", "jur_name", *financial_columns],
    ]

    # Remove columns where data are missing for all jurisdictions
    df = df.dropna(axis="columns", how="all")

    # List financial columns left after deleting columns with only missing values
    financial_columns_left = [col for col in df.columns if col in financial_columns]

    # Geographic score = 0 if no financial columns left
    if not financial_columns_left:
        return 0

    # Get absolute values of financial data to have only "positive" values
    df[financial_columns_left] = df[financial_columns_left].abs()

    # Calculate percentage of each financial value where jurisdiction is 'OTHER'
    # Percentage = 1. Total of 'OTHER' row(s) / 2. Total of all rows
    other_percentage = (
        df.loc[df["jur_code"] == "OTHER", financial_columns_left].sum()  # 1
        / df[financial_columns_left].sum()  # 2
    )

    # Calculate geographic score
    geographic_score = 100 - np.mean(other_percentage) * 100

    return geographic_score


def compute_completeness_score(df: pd.DataFrame, company: str, year: int) -> float:
    """Compute component II of transparency score which is the completeness score.


    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name.
        year (int): fiscal year to filter the results with.

    Returns:
        float: value of the score.
    """

    # Filter rows with selected company and subset with financial columns
    df = df.loc[
        (df["mnc"] == company) & (df["year"] == year),
        ["mnc", "year", "upe_code", "jur_code", "jur_name", *financial_columns],
    ]

    # Remove columns where data are missing for all jurisdictions
    df = df.dropna(axis="columns", how="all")

    # List financial columns left after deleting columns with only missing values
    financial_columns_left = [col for col in df.columns if col in financial_columns]

    # Completeness score = 0 if no financial columns left
    if not financial_columns_left:
        return 0

    # Calculate score with weighting :
    # * 1 pts per financial columns ;
    # * extra 1 pts for 'profit_before_tax' column if present ;
    # * extra 1 pts for 'tax paid' column if present.

    score = len(financial_columns_left)

    for variable in ["profit_before_tax", "tax_paid"]:
        if variable in df.columns:
            score += 1

    # Calculate completeness score
    completeness_score = score / 12 * 100

    return completeness_score


def compute_transparency_score(df: pd.DataFrame, company: str, year: int) -> float:
    """Compute transparency score.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name.
        year (int): fiscal year to filter the results with.

    Returns:
        float: value of the score.
    """

    # Filter rows with selected company and subset with financial columns
    df = df.loc[
        (df["mnc"] == company) & (df["year"] == year),
        ["mnc", "year", "upe_code", "jur_code", "jur_name", *financial_columns],
    ]

    # Remove columns where data are missing for all jurisdictions
    df = df.dropna(axis="columns", how="all")

    # List financial columns left after deleting columns with only missing values
    financial_columns_left = [col for col in df.columns if col in financial_columns]

    # Transparency score = 0 if no financial columns left
    if not financial_columns_left:
        return 0

    # Get absolute values of financial data to have only "positive" values
    df[financial_columns_left] = df[financial_columns_left].abs()

    # Calculate percentage of each financial value where jurisdiction is not 'OTHER'
    # Percentage = 1. Total of not 'OTHER' row(s) / 2. Total of all rows
    not_other_percentage = (
        df.loc[df["jur_code"] != "OTHER", financial_columns_left].sum()  # 1
        / df[financial_columns_left].sum()  # 2
    )

    # Calculate transparency score
    transparency_score = not_other_percentage.sum() / 10 * 100

    return transparency_score


def compute_all_scores(df: pd.DataFrame, company: str) -> dict:
    """Compute all scores (geographic, completeness, transparency).

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name.
        year (int): fiscal year to filter the results with.

    Returns:
        dict: value of the scores.
    """

    # List all years when the company as reported
    years_list = sorted(df.loc[df["mnc"] == company, "year"].unique())

    # Initialize an empty dictionary
    data = dict()

    # Calculate scores for each year and add them to the dictionary
    for year in years_list:
        # Calculate scores
        geographic_score = compute_geographic_score(df=df, company=company, year=year)
        completeness_score = compute_completeness_score(df=df, company=company, year=year)
        transparency_score = compute_transparency_score(df=df, company=company, year=year)

        data[year] = {
            "mnc": company,
            "geographic_score": geographic_score,
            "completeness_score": completeness_score,
            "transparency_score": transparency_score,
        }

    return data


def transparency_scores_to_csv(df: pd.DataFrame, csv_path: str = "./") -> pd.DataFrame:
    """Compute transparency score for all companies and all years into a
    DataFrame and export it to a csv file (optional).

    Args:
        df (pd.DataFrame): CbCRs database.
        csv_path (str, optional): Path of csv file. Defaults to './'.

    Returns:
        _type_: Scores for all companies and years.
    """

    # List all companies
    mnc_list = df["mnc"].unique()

    # Initialize an empty DataFrame
    mnc_df = pd.DataFrame()

    # Calculate transparency scores for all companies and add them to the DataFrame
    for mnc in mnc_list:
        temp_df = pd.DataFrame.from_dict(compute_all_scores(df=df, company=mnc), orient="index")

        mnc_df = pd.concat([mnc_df, temp_df])

    # Reset index and move 'mnc' columns in first position
    mnc_df = mnc_df.reset_index().rename(columns={"index": "year"})
    mnc_df.insert(0, "mnc", mnc_df.pop("mnc"))

    if csv_path:
        mnc_df.to_csv(csv_path + "transparency_scores.csv", index=False)

    return mnc_df


def transparency_score(df: pd.DataFrame, company: str, year: int = None):
    """Compute transparency score for specific company in a metric.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name.
        year (int): fiscal year to filter the results with.
    """

    # Compute data
    data = compute_all_scores(df=df, company=company)

    # Create DataFrame
    df = pd.DataFrame.from_dict(data, orient="index")

    # Reset index and move 'mnc' columns in first position
    df = df.reset_index().rename(columns={"index": "year"})

    # When data are not filtered by year, the score is the average of all years
    score = round(
        df.loc[df["year"] == year, "transparency_score"].iloc[0]
        if year
        else df["transparency_score"].mean(),
        0,
    )

    return score


# Viz 26 : company’s transparency score over time + details for each component of the score
# Functions below use the same computation function (compute_all_scores) as used for Viz 25.
def transparency_score_over_time(df: pd.DataFrame, company: str):
    """Display transparency scores over time for a specific company in a bar
    chart.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name.
    """

    # Compute data
    data = compute_all_scores(df=df, company=company)

    # Create DataFrame
    df = pd.DataFrame.from_dict(data, orient="index")

    # Reset index and move 'mnc' columns in first position
    df = df.reset_index().rename(columns={"index": "year"})

    # Create figure
    fig = px.bar(df, x="year", y="transparency_score", text_auto=".0f")

    # Update layout settings
    fig.update_layout(
        title="Transparency score over time",
        xaxis=dict(title=None, tickvals=df["year"].unique()),
        yaxis=dict(
            title=None,
            showline=True,
            ticks="outside",
            linecolor="grey",
            tickcolor="grey",
            range=[0, 101],
            tickvals=[0, 25, 50, 75, 100],
            ticktext=[0, "", "", "", 100],
        ),
        plot_bgcolor="white",
        width=800,
        height=480,
    )

    # Force position and color of bar values
    fig.update_traces(textposition="outside", textfont=dict(color=fig.data[0].marker.color))

    fig.show()


def transparency_scores_over_time_details(
    df: pd.DataFrame, company: str
) -> pd.DataFrame:
    """Compute all geographic, completeness and general transparency scores over time for a specific company in a table.

    Args:
        df (pd.DataFrame): CbCRs database.
        company (str): Company name.

    Returns:
        pd.DataFrame: Table with details of scores over years.
    """

    # Compute data
    data = compute_all_scores(df=df, company=company)

    # Create DataFrame
    df = pd.DataFrame.from_dict(data, orient="index")

    # Drop 'mnc' column
    df = df.drop(columns="mnc")

    # Round and convert percentage to string with '/100' annotation
    df = df.apply(lambda x: round(x).astype(int).astype("string") + "/100")

    # Reset index and rename 'year' column
    df = df.reset_index().rename(columns={"index": "Fiscal year"})

    # Move 'transparency_score' before other score columns
    df.insert(1, "transparency_score", df.pop("transparency_score"))

    # Rename columns
    df = df.rename(
        columns={
            "geographic_score": "Score on geographical disaggretion",
            "completeness_score": "Score on variable exhaustiveness",
            "transparency_score": "Transparency score",
        }
    )

    return df


# Viz 27 : average transparency score over time
# TODO add code
