[//]: # (The root file handles sections in common for all pages like header and footer)
[//]: # (It also contains the <|content|> variable which will display the content of selected page)

[//]: # (Header)
<header|part|class_name=header_bg|
<|layout|columns=auto 1fr auto 1fr|class_name=align-columns-center|
<|part|class_name=align-item-center|
<|{taxplorer_logo_path}|image|width="48px"|>
|>

<|part|class_name=align-item-center|
<|Taxplorer|text|class_name=logotitle|>
|>

<|part|class_name=align-item-stretch|
<|navbar|class_name=fullheight|>
|>

<|part|class_name=text-right align-item-center|
<|button|label=Download data|>
|>
|>

<hr class="header_hr"/>
|header>

[//]: # (Add active page content)
<|content|>

[//]: # (Footer)
<footer|part|height=380px|class_name=footer_bg|
<|layout|columns=1fr auto 1fr|class_name=align-columns-center|

[//]: # (Left section of footer)
<|layout|columns=1fr 1fr|class_name=align-columns-center|
<|part|class_name=text-center align-item-center|
<|{data4good_logo_path}|image|height=6rem|class_name=d-block m-auto mb1|>
DATA FOR GOOD<br/>
{: .footer_title }

<|layout|columns=1fr 1fr|class_name=align-columns-center mt1 ml6 mr6|
<|part|class_name=text-left align-item-center ml1|
Website<br/>
Twitter<br/>
LinkedIn<br/>
{: .footer_text }
|>

<|part|class_name=text-center align-item-center|
<|{website_logo_path}|image|width=1rem|class_name=d-block m-auto|>
<|{twitter_logo_path}|image|width=1rem|class_name=d-block m-auto|>
<|{linkedin_logo_path}|image|width=1rem|class_name=d-block m-auto|>
|>
|>
|>

<|part|class_name=text-center align-item-center|
<|{eutax_logo_path}|image|height=6rem|class_name=d-block m-auto mb1|>
EU TAX OBSERVATORY<br/>
{: .footer_title }

<|layout|columns=1fr 1fr|class_name=align-columns-center mt1 ml6 mr6|
<|part|class_name=text-left align-item-center ml1|
Website<br/>
Twitter<br/>
LinkedIn<br/>
{: .footer_text }
|>

<|part|class_name=text-center align-item-center|
<|{website_logo_path}|image|width=1rem|class_name=d-block m-auto|>
<|{twitter_logo_path}|image|width=1rem|class_name=d-block m-auto|>
<|{linkedin_logo_path}|image|width=1rem|class_name=d-block m-auto|>
|>
|>
|>

<|part|class_name=lign-item-center ml3 mt2|
&#169; 2024 Privacy &#8210; Terms
{: .footer_privacy_text }
|>
|>

[//]: # (Add vertical line)
<div class="footer_vl"></div>

[//]: # (Right section of footer)
<|part|class_name=ml6 mr6 pr4 mt3|
A project led by the EU tax observatory and Data for Good
{: .footer_title }

<br/>
The EU Tax Observatory conducts innovative research on taxation, contributes to a democratic and inclusive debate on the 
future of taxation, and fosters a dialogue between the scientific community, civil society, and policymakers in the 
European Union and worldwide.  
Data for Good is a community of 4 000 tech experts volunteering for general interest projects.
{: .footer_text_justified }

<|layout|columns=2fr 1fr|class_name=pt1|
<|button|label=Discover our methodology|>
<|part|class_name=text-right|
<|button|label=Contact|>
|>
|>
|>
|>
|footer>