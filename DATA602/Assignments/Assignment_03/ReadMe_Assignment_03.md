### Assignment 03 Read-Me

Assignment Content
- Configure a GitHub account w/ your UMBC email (if you don't have one).

- Create repository to warehouse homeworks and projects for the first of the class.

- Pick a dataset (not in the book or a common toy example) that you'll eventually want to use for a regression problem.

- Perform EDA on that dataset in a Jupyter Notebook and post to Github. It should include information on the dataset, what question you eventually want to answer. Graphs and tables should be well labeled and "professional" quality. It should fully explore the dataset and provide the reader with all the high points regarding potential predictors and patterns in the data.

- In addition to code and output, include written descriptions of what you can see. This should be clear, considering, and use proper grammar.

**You will be submitting a link to your GitHub repository.**

Rubric:
- (10%) GitHub repository for DATA602 created and folder for assignment 3 created Within assignment 3 folder there should be a folder for the data used (with the data included therein), an executed Jupyter Notebook, and a readme file with the data and project description.
- (10%) Jupyter Notebook Markdown cells properly formatted. Major steps in the analysis should be described in the markdown and results should be discussed immediately after the code block. All code blocks have output below - no errors or cells that weren’t executed. Narratives are properly formatted, with correct grammar and punctuation.
- (10%) Output of professional quality Charts properly labeled (axis labels, titles, …)
- (70%) Completeness of exploratory analysis
- (5%) Discussion of business question / objective that is being analyzed
- (5%) Profiling of data (observations, missing values, data types)
- (10%) Relevant categorical variables analyzed, and cleaned, if necessary.
- (10%) Numerical variables analyzed (distributions, five number summary, …)
- (30%) Exploration of relationships between key categorical and numerical variables
- (10%) Discussion of what you have observed throughout your analysis

I should be able to walk away with a through outstanding of the dataset you’ve chosen

--------------------------
### Description

The data used in this assignment was sourced from: https://data.baltimorecity.gov/datasets/real-property-information/explore\

The overall goal of this data analysis is for real estate property investing in Baltimore city. I have personal interest in investing in the Baltimor real estate and decided this would be an excellent dual use of time and skill. 

Ultimate goal is to develop a list of properties to look at and cross reference with other available datasets in from https://data.baltimorecity.gov/datasets to narrow down some properties of interest.

The Data Contains:
- PropertyID: A combination of Block number and Lot number
- Block: The identification number for each city block in Baltimore
- Lot: The identification number for each lot on each block
- Ward: The identification number for the city ward that each property is located
- Sect: The identification number for the section of each city where the property is located 
- PropertyAddress: The street address where each property is located
- LotSize: The size of each property measured in square feet or acres
- CityTax: The US dollar amount of taxes owed to the city of Baltimore by each property
- StateTax: The US dollar amount of taxes owed to the state of Maryland by each property 
- ResCode: Either "PRINCIPAL RESIDENCE" or "NOT A PRINCIPAL RESIDENCE", meaning whether or not the owner resides at the property
- AmountDue: Total amount of taxes in US dollars owed by each property
- Neighborhood: The name of the neighborhood in which each property resides
- PoliceDistrict: The name of each policing district in which teach property resides
- CouncilDistrict: The identifier for each city council district that each property resides
- Location: The latitude and longitude or each property 
- ESRI-OID: Mapping identifier for esri arcgis visualization


------
The goals of this work are quite ambitious and will be ongoing for sometime. 


