[//]: # (Layout of the home page)

[//]: # (Main section)
<main_content|part|class_name=main-page-style|

[//]: # (World map section)
<world_map|part|class_name=world_map_container|

[//]: # (World map : background image)
<|{world_map_path}|image|width=100%|>

[//]: # (World map : text and cards)
<|part|class_name=world_map_content ml6 mr6 pl2 pr2|

[//]: # (World map : text)
Multinationals under the spotlight
{: .world_map_title .mt4 .mb3 }

This platform provides unprecedented insights into  how large corporations approach taxes across borders. Explore 
country-by-country financial reports published by multinationals to see where they declare profits and revenues, 
identify potential uses of tax havens or loopholes and analyze tax payments versus actual operations.<br/><br/>
While some multinationals now publish detailed country data, the reports remain scattered and difficult to analyze 
collectively. Our tool compiles this information into an accessible, user-friendly format. Start exploring the tax 
footprints of major multinationals today and unlock key insights into an often opaque aspect of global business.
{: .world_map_text .mb3 }

[//]: # (World map : cards)
<|layout|columns=1fr 1fr 1fr|gap=1rem|class_name=align-columns-center|
<|card|id=white_card|
Explore companies
{: .white_card_title .mr2 }

<|part|class_name=d-flex|
Search and filter to find reports for specific multinationals. Review their declared profits, taxes paid, employee 
counts and more for each country over multiple years.
{: .white_card_text }

&#8599;
{: .white_card_arrow .ml2}
|>
|>

<|card|id=white_card|
Spot reporting trends
{: .white_card_title .mr2 }

<|part|class_name=d-flex|
Visualize how tax reporting practices from the world's largest corporations are evolving across industries, regions 
and over time through interactive charts and analysis.
{: .white_card_text }

&#8599;
{: .white_card_arrow .ml2}
|>
|>

<|card|id=white_card|
Gain Expert Insights
{: .white_card_title .mr2 }

<|part|class_name=d-flex|
Access our ongoing research examining multinational tax behavior based on this country-by-country data, including case 
studies, risk scoring and more.
{: .white_card_text }

&#8599;
{: .white_card_arrow .ml2}
|>
|>
|>
|>
|world_map>

[//]: # (Main content : viz)
<|part|class_name=main-content|
<viz|part|class_name=mb4|
<|part|class_name=title_button_container mb3|
Our database is growing
{: .title_blue}

[//]: # (<|button|label=More on reporting trends &#8594;|>)
|>

<|part|class_name=home_viz_grid|

[//]: # (Viz 1)
<|part|class_name=home_viz_1|
<|card|
<|part|
<|{viz_1.title}|text|class_name=viz_title|>
<br/>
<|{viz_1.sub_title}|text|class_name=viz_sub_title|>
|>
<|part|class_name=round|
<|{viz_1.data}|>
|>
|>
|>

[//]: # (Viz 3)
<|part|class_name=home_viz_3|
<|card|
<|part|
<|{viz_3.title}|text|class_name=viz_title|>
<br/>
<|{viz_3.sub_title}|text|class_name=viz_sub_title|>
|>
<|part|class_name=round|
<|{viz_3.data}|>
|>
|>
|>

[//]: # (Viz 2)
<|part|class_name=home_viz_2|
<|card|
<|part|
<|{viz_2.title}|text|class_name=viz_title|>
<br/>
<|{viz_2.sub_title}|text|class_name=viz_sub_title|>
|>

<|layout|columns=1fr|
<|chart|figure={viz_2.fig}|>
|>
|>
|>

[//]: # (Viz 24)
<|part|class_name=home_viz_24|
<|card|
<|part|
<|{viz_24.title}|text|class_name=viz_title|>
<br/>
<|{viz_24.sub_title}|text|class_name=viz_sub_title|>
|>
<|part|
<|chart|figure={viz_24.fig}|height=300px|>
|>
|>
|>
|>
|viz>

[//]: # (Main content : stories)
<stories|part|
<|part|class_name=title_button_container mb3|
Why this project ?
{: .title_blue}

<|button|label=More key stories &#8594;|on_action=goto_keystories|>
|>

<|layout|columns=1fr 1fr 1fr|gap=1rem|class_name=align-columns-center|
<|card|id=blue_card|
The Great Tax Escape
{: .blue_card_title .mb1 .pr2}

Exploiting loopholes, multinationals funneled over $1 trillion in profits to tax havens in 2022 alone. This 
industrial-scale tax avoidance costs countries 10% of their corporate tax base annually undermining their ability to 
fund vital public services for citizens.
{: .blue_card_text .mb2 }

<a class="blue_card_link" href="https://www.taxobservatory.eu/publication/global-tax-evasion-report-2024/" target="_blank">Read more &#8594;</a>
{: .blue_card_link }
|>

<|card|id=blue_card|
The Call for Tax Transparency
{: .blue_card_title .mb1 .pr2}

Investors, activists, and governments demand transparency - are corporations paying their fair share? But too often, 
the data trail goes cold. Country-by-Country Reporting makes corporate tax strategies more transparent, one company at 
a time.
{: .blue_card_text .mb2 }

|>

<|card|id=blue_card|
Tracking the Tax Trail
{: .blue_card_title .mb1 .pr2}

While more companies voluntarily publish their country-by-country tax reports, an incoming EU directive will force 
thousands of multinationals to disclose their global tax footprints.<br/>
The catch? No central database is mandated, making monitoring difficult. This site aims to be that missing public 
repository.
{: .blue_card_text .mb2 }

|>
|>
|stories>
|>
|main_content>