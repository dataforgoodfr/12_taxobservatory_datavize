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

<|card|
<|part|class_name=cpb12|
<|{viz_1.title}|text|class_name=viz_title|>
<br/>
<|{viz_2.sub_title}|text|class_name=viz_sub_title text-transparent|>
|>
<|part|class_name=text-blue text-weight700 text-center round3|
<|{viz_1.data}|>
|>
|>

<|card|
<|part|class_name=cpb12|
<|{viz_2.title}|text|class_name=viz_title|>
<br/>
<|{viz_2.sub_title}|text|class_name=viz_sub_title text-transparent|>
|>
<|part|class_name=text-blue text-weight700 text-center round3|
<|{viz_2.data}|>
|>
|>

<|card|
<|part|class_name=cpb8|
<|{viz_3.title}|text|class_name=viz_title|>
<br/>
<|{viz_3.sub_title}|text|class_name=viz_sub_title text-transparent|>
|>
<|part|class_name=text-blue text-weight700 text-center round2|
<|{viz_3.data}|>
|>
|>

<|card|
<|part|class_name=cpb8|
<|{viz_4.title}|text|class_name=viz_title|>
<br/>
<|{viz_4.sub_title}|text|class_name=viz_sub_title|>
|>
<|part|class_name=text-blue text-weight700 text-center round2|
<|{viz_4.data}|><|/100|text|>
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

<|card|
<|part|class_name=cpb8|
<|{viz_5.title}|text|class_name=viz_title|>
<br/>
<|{viz_5.sub_title}|text|class_name=viz_sub_title|>
|>
<|part|class_name=text-blue text-weight700 text-center round2|
<|{viz_5.data}|><|/100|text|>
|>
|>

<|card|
<|part|class_name=cpb8|
<|{viz_26.title}|text|class_name=viz_title|>
<br/>
<|{viz_26.sub_title}|text|class_name=viz_sub_title|>
|>
<|part|
<|{viz_26.data}|table|show_all|sortable=False|style=table-cell|class_name=rows-similar|>
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

<|card|
<|part|
<|{viz_13.title}|text|class_name=viz_title|>
<br/>
<|{viz_13.sub_title}|text|class_name=viz_sub_title|>
<br/>
|>
<|{viz_13.data}|table|show_all|sortable=False|dynamic=True|style=table-cell|class_name=rows-similar|>
|>

<|card|
<|part|
<|{viz_14.title}|text|class_name=viz_title|>
<br/>
<|{viz_14.sub_title}|text|class_name=viz_sub_title|>
<br/>
|>
<|chart|figure={viz_14.fig}|class_name=plot-overflow|>
|>

|>

|profile>

<distribution|part|class_name=cpb1 cpt2|
Distribution of profits vs employees
{: .h2 .text-blue .cpb2 .text-weight500 }

<|layout|columns=1fr 1fr|gap=1rem|

<|card|
<|part|
<|{viz_15.title}|text|class_name=viz_title|>
<br/>
<|{viz_15.sub_title}|text|class_name=viz_sub_title|>
<br/>
|>
<|chart|figure={viz_15.fig}|height=400px|class_name=plot-overflow|>
|>

<|card|
<|part|
<|{viz_16.title}|text|class_name=viz_title|>
<br/>
<|{viz_16.sub_title}|text|class_name=viz_sub_title|>
<br/>
|>
<|chart|figure={viz_16.fig}|height=400px|class_name=plot-overflow|>
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
