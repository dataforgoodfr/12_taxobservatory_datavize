[//]: # (The root file handles sections in common for all pages like header and footer)
[//]: # (It also contains the <|content|> variable which will display the content of selected page)

[//]: # (Header)
<header|container header sticky|

<|layout|columns=1fr 1fr 1fr|class_name= pt-half pb-half|

<|part|class_name=d-flex|
<|{taxplorer_logo_path}|image|width=3rem|>
Taxplorer
{: .h1}
|>

<|navbar|lov={navbar_items}|>

<|part|class_name=text-right|
<|button|label=Download|on_action=goto_download|>
|>

|>

<hr class="header-hr35"/>

|header>

[//]: # (Add active page content)
<|content|>

[//]: # (Footer)

<footer|container footer-bg|

<|part|class_name=cpt3 cpb3 cpl6 cpr6|

<|layout|columns=2*1fr|gap=2rem|

[//]: # (Left section of footer)

<left|layout|columns=2*1fr|

[//]: # (Data For Good section)

<dataforgood|part|

<|part|class_name=text-center|

 <img class="cpb14" src="./images/data4good-logo.svg" height="130px"/> 

DATA FOR GOOD
{: .h4 .text-blue .text-footer .cpb6 }

<|layout|columns=2*1fr|columns[mobile]=1 1|class_name=text-small text-footer cpl24 cpr24|
Website
{: .text-left }

<a class="text-center" href="https://dataforgood.fr/" target="_blank">
    <img src="./images/website-logo.svg"/>
</a>
|>

<|layout|columns=2*1fr|columns[mobile]=1 1|class_name=text-small text-footer cpl24 cpr24|
Twitter
{: .text-left }

<a class="text-center" href="https://twitter.com/dataforgood_fr" target="_blank">
    <img src="./images/twitter-logo.svg"/>
</a>
|>

<|layout|columns=2*1fr||columns[mobile]=1 1|class_name=text-small text-footer cpl24 cpr24|
LinkedIn
{: .text-left }

<a class="text-center" href="https://www.linkedin.com/company/dataforgood" target="_blank">
    <img src="./images/linkedin-logo.svg"/>
</a>
|>

|>

|dataforgood>

[//]: # (Tax Observatory section)

<taxobservatory|part|

<|part|class_name=text-center|

 <img class="cpb14" src="./images/eutax-logo.svg" height="130px"/> 

EU TAX OBSERVATORY
{: .h4 .text-blue .text-footer .cpb6 }

<|layout|columns=2*1fr|columns[mobile]=1 1|class_name=text-small text-footer cpl24 cpr24|
Website
{: .text-left }

<a class="text-center" href="https://www.taxobservatory.eu/" target="_blank">
    <img src="./images/website-logo.svg"/>
</a>
|>

<|layout|columns=2*1fr|columns[mobile]=1 1|class_name=text-small text-footer cpl24 cpr24|
Twitter
{: .text-left }

<a class="text-center" href="https://twitter.com/taxobservatory" target="_blank">
    <img src="./images/twitter-logo.svg"/>
</a>
|>

<|layout|columns=2*1fr||columns[mobile]=1 1|class_name=text-small text-footer cpl24 cpr24|
LinkedIn
{: .text-left }

<a class="text-center" href="https://www.linkedin.com/company/70917369/" target="_blank">
    <img src="./images/linkedin-logo.svg"/>
</a>
|>

|>

|taxobservatory>

&#169; 2024 Privacy &#8210; Terms
{: .text-footer .text-blue .text-small .cpt14 }

|left>

[//]: # (Right section of footer)

<right|part|class_name=cpl14 cpr14 cpt6|

A project led by the EU Tax Observatory and Data for Good
{ .h4 .text-footer .text-blue }

<br/>
The EU Tax Observatory conducts innovative research on taxation, contributes to a democratic and inclusive debate on the 
future of taxation, and fosters a dialogue between the scientific community, civil society, and policymakers in the 
European Union and worldwide.<br/>
Data for Good is a community of 4 000 tech experts volunteering for general interest projects.
{ .text-footer .text-justify .text-small }

<|layout|columns=2fr 1fr|columns[mobile]=1 1|class_name=cpt6|

<|part|class_name=text-left|
<|button|label=Discover our methodology|on_action=goto_methodology|>
|>

<|part|class_name=text-right|
<|button|label=Contact|on_action=goto_contact|>
|>

|>

|right>

|>

|>

|footer>
