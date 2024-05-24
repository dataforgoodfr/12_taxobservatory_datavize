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
<|{viz1.title}|text|class_name=viz_title|>
<br/>
<|{viz1.sub_title}|text|class_name=viz_sub_title|>
|>
<|part|class_name=round|
<|{viz1.data}|>
|>
|>
|>

[//]: # (Viz 3)
<|part|class_name=home_viz_3|
<|card|
<|part|
<|{viz3.title}|text|class_name=viz_title|>
<br/>
<|{viz3.sub_title}|text|class_name=viz_sub_title|>
|>
<|part|class_name=round|
<|{viz3.data}|>
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
<|part|
<|{viz_2.data}|chart|type=bar|x=year|y[1]=mnc|line[1]=dash|height=300px|>
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
<|chart|figure={data_viz_24_fig}|height=300px|>
|>
|>
|>
|>
|viz>

[//]: # (Main content : stories)
<stories|part|
<|part|class_name=title_button_container mb3|
And there are a lot of stories to tell
{: .title_blue}

<|button|label=More key stories &#8594;|on_action=goto_keystories|>
|>

<|layout|columns=1 1|gap=6rem|class_name=align-columns-center|
<|card|id=blue_card|
European banks love tax havens
{: .blue_card_title .mb1 .pr2}

Analysing 7 years of country-by-country data published by European banks, we show that EU banks have been consistently 
present in tax havens with around 14% of their profits booked in tax havens annually. Implementing a 15% minimum tax 
rate could generate EUR 3-5 billion annually for European countries.
{: .blue_card_text .mb2 }

Read more &#8594;
{: .blue_card_link }
|>

<|card|id=blue_card|
Tracking CbCR's Fragmented Uptake
{: .blue_card_title .mb1 .pr2}

Overall CbCR publishing rates are low (97 reports for 2020), but increasing rapidly. CbCR publishing is concentrated in 
European countries and in the extractive sector. Last, there remains significant room for progress on the completion of 
the information provided and the accessibility of these reports: 55% of the reports do not include all the recommended 
variables and reports are published in a wide variety of documents.
{: .blue_card_text .mb2 }

Read more &#8594;
{: .blue_card_link }
|>
|>
|stories>
|>
|main_content>