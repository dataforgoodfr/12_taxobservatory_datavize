<main|container main-bg|

<|part|class_name=cpt4 cpb4 cpl8 cpr8|

Methodology
{: .h1 .text-blue .cpb2}

<introduction|part|class_name=text-justify cpb1|
Taxplorer was created to collect, aggregate and analyze data from country-by-country reports published by multinationals.  
Our approach is based on three pillars :

* Open source : The code is available
<a href="https://github.com/dataforgoodfr/12_taxobservatory/" target="_blank">
 here 
</a>
and our database can be downloaded [here](/Download).
* Collaborative : [Reach out](/Contact) to contribute or suggest improvements.
* Dynamic : Our database is regularly updated to incorporate new insights and to enhance its accuracy.
|introduction>

<collection|part|class_name=cpb2|
How is the data collected ?
{: .h2 .text-blue .cpb2 .text-weight500 }

The key steps of the database construction are the following. We start by collecting sustainability and other reports, 
usually published as PDFs. We extract from these the CbCR tables and convert them into text. Tables are rearranged and 
standardised to obtain a uniform dataset. Finally, we enrich the dataset with additional information on the sector and 
headquarter country from financial accounts.<br/><br/>
{: .text-justify }

<|part|class_name=text-justify|
Report Collection
{: .h6 }

The public CbCR data were all hand-collected using publicly available online corporate reports, such as annual reports 
or sustainability reports. We proceeded by using several different key words on google that effectively identify public 
CbCR data. Key words used are: "207-4", "Public country-by-country-report", "Tax contribution report", all GRI variable 
names and all OECD variable names.  We used these key words directly on all companies within the Eurostoxx and the MSCI 
SRI list. We focused on Eurostoxx as reporting is higher in Europe. We used the MSCI Socially Responsible Investing 
(SRI) list because multinationals with good ESG ratings should have a higher probability of reporting. We then used 
these key words more generally on google without using any particular company list. We sometimes indicate to display 
only pdf-files and vary time horizons and locations to attempt to capture a maximum of companies.
|>

|collection>

<process|part|class_name=cpb2|
How is data processed ?
{: .h2 .text-blue .cpb2 .text-weight500 }

<|part|class_name=text-justify|
Table formatting
{: .h6 }

CbCRs are published by multinationals in different formats. The most common for a given multinational and fiscal year 
has each row corresponding to a given jurisdiction and each column to different variables. A smaller number of companies 
used different formats, for example spreading data across multiple tables in the document (e.g. data for profit before 
tax and tax paid might be on two different pages), reporting multiple fiscal years in the same table or transposing the 
table. The tables were converted into the standard format in order to merge them.
<br/><br/>

Cell-level issues
{: .h6 }

Several within-cell issues have been addressed : ranging from the notation used to denote a negative value, to the use 
of characters to ease readability (3000 is often presented as "3,000", "3.000" or "3 000"), to the removal of sub- and 
superscripts and of other characters present in the cells.
<br/><br/>

Standardization of variable names and country names
{: .h6 }

We have collected country-by-country reports published in multiple languages (e.g. Spanish, Italian), to translate 
variables and country names into English we resorted to dictionaries in the corresponding languages.

In addition, across the reports collected, the names used to refer to the standard variables vary widely. For example, 
"Unrelated party revenues" can be referred to as  "Third-party revenue", "Revenues from unrelated parties", "Revenues 
from third-party sales" or "Income from sales to third parties". To have uniform column names, whenever a new variable 
name is encountered, correspondence with the standard name is made, and the rule is then either applied globally or 
just once.
<br/><br/>

Similarly, jurisdiction names might differ across reports, for example, the United States of America can be either 
referred to as "The US", "USA" or "United States", "United Stated of America". Jurisdiction names were made uniform 
and standardised to a 3-letter code.
<br/><br/>

Finally, some companies, instead of publishing data on a strict country-by-country basis, aggregate multiple 
jurisdictions together (e.g."Ireland and the Netherlands" or "other europe"). In these cases, we set the jurisdiction 
name to "other" or "other" followed by additional information e.g  "other apac" or "other europe".
<br/><br/>

Units, currency and variables' signs
{: .h6 }

Multinationals published their CbCRs using different currencies and units (e.g. thousands, billions, millions). In 
order to have a consistent database, the units and the currencies are manually collected for each report. This 
information is then used to transform all financial figures into euros units. The conversion rates used have been 
computed by averaging the daily rates found on XE.com for each year.
<br/><br/>
  
Another source of inconsistency is due to the sign attributed to some variables, in particular tax paid and accrued. 
As they are recorded as expenses, multinationals sometimes record the tax paid on profits as a negative value. To 
ensure that the tax variables have a homogeneous sign across all reports included in the database, we manually collect 
information on the appropriate sign and invert them when necessary to have tax paid as positive values and 
reimbursements by the government as negative ones.
<br/><br/>

Additional information
{: .h6 }

We have enriched the database by adding the following information for each multinational : the country in which it is 
headquartered and the industry classification. This information was sourced from ORBIS, Bloomberg.com and financial 
accounts. It should be noted that an effort was made to attribute the sector to the whole multinational, this is 
sometimes challenging as certain structures (such as conglomerates) might operate in different sectors.
<br/><br/>

Data limitations
{: .h6 }

The current version of the database covers public CbCRs relative to the fiscal years 2016 to 2021. Companies publish 
CbCRs on a voluntary basis, resulting in an unbalanced panel with heterogeneity across the different disclosures. 
Companies apply some discretion when choosing which set of variables to disclose, apply different geographical 
disaggregations and sometimes deviate from the standard definition of the reported variables.

|>
|process>

<calculations|part|class_name=cpb2|
Calculations ?
{: .h2 .text-blue .cpb2 .text-weight500 }

Transparency score
{: .h5 .text-blue .cpb2 }

Multinationals, except banks, report on a voluntary basis. The disclosed information varies a lot in terms of detail. 
Multinational enterprises can limit the financial variables they disclose. They can also add geographic categories, 
instead of giving detailed figures for each country.
<br/><br/>

To evaluate the comprehensiveness and transparency of country-by-country reports, we have developed a transparency 
score specifically tailored for this purpose. Building upon previous literature, this score measures the extent to 
which multinational enterprises disclose financial information across different countries and variables.
<br/><br/>

The transparency score is calculated based on the disclosure of the set of 10 variables included in the standard CbCR 
designed by the OECD (
<a href="https://www.oecd.org/tax/transfer-pricing-documentation-and-country-by-country-reporting-action-13-2015-final-report-9789264241480-en.htm" target="_blank">
link
</a>
) across different jurisdictions with higher scores indicating greater transparency (0 is the lowest score and 100 is 
the highest). The transparency score calculation follows the general formula :
<br/><br/>

[//]: # (Taipy is not able to render the below LaTex expression so an image is used instead to display the equation)

[//]: # ($$\text{Transparency Score} = \sum_{i=1}^{n} w_i \times \frac{\sum_{j\in J_i} | x_{ij} |}{\sum_{j} | x_{ij} |} \times 100\$$)

<|part|class_name=text-center|
<img class="test" src="./assets/images/transparency-score-equation.svg" height="40px"/>
|>
<br/><br/>

Where :

* *n* is the number of financial variables ;
* *w<sub>i</sub>* is the weight assigned to the *i*-th financial variable (in this case, all variables are equally 
weighted, with *w<sub>i</sub> = 1/n*) ;
* *J<sub>i</sub>* is the set of jurisdictions for which the *i*-th financial variable is disclosed (excluding the 
aggregated categories) ;
* *x<sub>ij</sub>* is the value of the *i*-th financial variable for jurisdiction *j*.

We also created two additional metrics :
<br/><br/>

Geographical level of reporting
{: .h6 }

<br/>

**Context** : Usually the CBCR has to publish figures country by country (or jurisdiction by jurisdiction). Some 
multinationals comply with this requirement, but others publish figures by large region, such as Asia or Africa. 
Some multinationals may also group a certain number of countries together in an "Other" category, in which the 
multinationals aggregate several countries and may or may not give details of these countries. We wanted here to 
calculate a score that evaluates the quantity of data reported at a jurisdiction level and would penalize data reported 
at a more aggregated level than the jurisdiction.
<br/><br/>

**Calculation** : For each financial variable available in the report (transformed into absolute values), we calculate the % attributed 
to a jurisdiction and then calculate the average of those scores (e.g., if 70 % of a company's profits and 50% of this 
company's employees are attributed to a jurisdiction, its geographical score for this report will be 60 %).
<br/><br/>

Completeness of the financial data provided
{: .h6 }

<br/>

**Context** : A full CbCR report should include the following 10 financial data :

1. Revenue by Region = Total_Revenue dans le dataset actuel
2. Related Party transactions ou related Party Revenue by region = Related party revenue
3. Pre-tax income by region = Profit before Tax
4. Income Tax expense by region = Income Tax accrued
5. Cash Taxes paid by region = Tax paid
6. Assets or property, plant, and equipment by region = Tangible assets
7. Accumulated earnings
8. Tangible assets
9. Stated capital
10. Number of employees by region = Employees

Yet, some companies do not disclose all variables. We wanted to reflect this in the transparency score.
<br/><br/>

**Calculation** : We calculate the score based on the weighted share of variables available in 
the report (i.e., for which the company provides at least 1 datapoint).
|calculations>

|>

|main>
