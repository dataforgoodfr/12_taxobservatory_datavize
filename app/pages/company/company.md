<main|container main-bg|

<selection|part|class_name=cpt4 cpl8 cpr8|

<|layout|columns=2*1fr|class_name=cpb6|

<|part|
Pick a company to dive into the report
{: .h1 .text-blue .cpb4 .cpr14 }

<|{selected_company}|selector|lov={selector_company}|on_change=on_change_company|dropdown|class_name=fullwidth mb2|width=65%|>

Can't find a company ?<br/>
We might have missed out in its report.<br/>
[Reach out](/Contact) if you found it.
{ .text-blue .text-weight300 .cpt12}
|>

<|{company_image_path}|image|width=100%|>

|>

|selection>

<hr class="header-hr20"/>

<company|part|class_name=cpt4 cpl8 cpr8|

<|{selected_company}|text|class_name=h1 text-blue cpb4|>

<|layout|columns=4*1fr|gap=1rem|

<|part|class_name=viz-container|
<|{viz["company_sector"].title}|text|class_name=text-weight400|>
<br/>
<|{viz["company_sector"].sub_title}|text|class_name=text-small text-weight300 text-transparent|>
<|part|class_name=metric-container cpt6 cpt6|
<|{viz["company_sector"].data}|text|class_name=text-metric|>
|>
|>

<|part|class_name=viz-container|
<|{viz["company_upe_name"].title}|text|class_name=text-weight400|>
<br/>
<|{viz["company_upe_name"].sub_title}|text|class_name=text-small text-weight300 text-transparent|>
<|part|class_name=metric-container cpt6 cpt6|
<|{viz["company_upe_name"].data}|text|class_name=text-metric|>
|>
|>

<|part|class_name=viz-container|
<|{viz["company_nb_reports"].title}|text|class_name=text-weight400|>
<br/>
<|{viz["company_nb_reports"].sub_title}|text|class_name=text-small text-weight300 text-transparent|>
<|part|class_name=metric-container cpt6 cpt6|
<|{viz["company_nb_reports"].data}|text|class_name=round-metric|>
|>
|>

<|part|class_name=viz-container|
<|{viz["company_transparency_score"].title}|text|class_name=text-weight400|>
<br/>
<|{viz["company_transparency_score"].sub_title}|text|class_name=text-small text-weight300|>
<|part|class_name=metric-container cpt6 cpt6|
<|part|class_name=round-metric|
<|{viz["company_transparency_score"].data}|><|/100|text|>
|>
|>
|>

|>

|company>

<financial|part|class_name=cpt4 cpb6 cpl8 cpr8|

<|layout|columns=85% 15%|
Financial Reporting Overview
{: .h1 .text-blue .cpb4 }

<|{selected_year}|selector|lov={selector_year}|on_change=on_change_year|dropdown|class_name=fullwidth|>
|>

<transparency|part|class_name=cpb1|
Tax Transparency
{: .h2 .text-blue .cpb2 .text-weight500 }

<|layout|columns=1fr 3fr|gap=1rem|

<|part|class_name=viz-container|
<|{viz["fin_transparency_score"].title}|text|class_name=text-weight400|>
<br/>
<|{viz["fin_transparency_score"].sub_title}|text|class_name=text-small text-weight300|>
<|part|class_name=metric-container cpt8 cpt8|
<|part|class_name=round-metric|
<|{viz["fin_transparency_score"].data}|><|/100|text|>
|>
|>
|>

<|part|class_name=viz-container|
<|{viz["fin_transparency_score_over_time_details"].title}|text|class_name=text-weight400|>
<br/>
<|{viz["fin_transparency_score_over_time_details"].sub_title}|text|class_name=text-small text-weight300 text-transparent|>
<|part|
<|{viz["fin_transparency_score_over_time_details"].data}|table|show_all|sortable=False|style=table-cell|class_name=rows-similar table-top|>
|> 
|>

|>

<|part|class_name=text-justify text-small cpt2|
* We evaluate the reports transparency considering two features: the geographical disaggregation and the presence of 
the different recommended variables. The more detailed the geographical disaggregation and the higher the number of 
variables published the higher the transparency score. Find more on our [methodology page](/Methodology).
<br/><br/>
* It is important to note that the availability of different variables will be essential to calculate the indicators 
below. When the variables are not available it will not be possible to calculate all indicators.
|>

|transparency>

<profile|part|class_name=cpb1|
Financial profile
{: .h2 .text-blue .cpb2 .text-weight500 }

<|layout|columns=1fr 1fr|gap=1rem|

<|part|class_name=viz-container|
<|{viz["fin_key_financials_kpis"].title}|text|class_name=text-weight400|>
<br/>
<|{viz["fin_key_financials_kpis"].sub_title}|text|class_name=text-small text-weight300|>
<|{viz["fin_key_financials_kpis"].data}|table|show_all|sortable=False|dynamic=True|style=table-cell|class_name=rows-similar table-top|>
|>

<|part|class_name=viz-container|
<|{viz["fin_top_jurisdictions_revenue"].title}|text|class_name=text-weight400|>
<br/>
<|{viz["fin_top_jurisdictions_revenue"].sub_title}|text|class_name=text-small text-weight300|>
<|chart|figure={viz["fin_top_jurisdictions_revenue"].fig}|>
|>

|>

|profile>

<distribution|part|class_name=cpb1 cpt2|
Distribution of profits vs employees
{: .h2 .text-blue .cpb2 .text-weight500 }

<|layout|columns=1fr 1fr|gap=1rem|

<|part|class_name=viz-container|
<|{viz["fin_pretax_profit_and_employees_rank"].title}|text|class_name=text-weight400|>
<br/>
<|{viz["fin_pretax_profit_and_employees_rank"].sub_title}|text|class_name=text-small text-weight300|>
<|chart|figure={viz["fin_pretax_profit_and_employees_rank"].fig}|>
|>

<|part|class_name=viz-container|
<|{viz["fin_pretax_profit_and_profit_per_employee"].title}|text|class_name=text-weight400|>
<br/>
<|{viz["fin_pretax_profit_and_profit_per_employee"].sub_title}|text|class_name=text-small text-weight300|>
<|chart|figure={viz["fin_pretax_profit_and_profit_per_employee"].fig}|>
|>

|>

<|part|class_name=text-justify text-small cpt2|
This chart plots the percentage of total positive profits and the percentage of total employees reported in each 
country where the multinational is active. Comparing the amount of physical production factors like employees with 
the amount of profit can give an indication of profit shifting activities where strong misalignment are observed
|>

|distribution>

|financial>

|main>
