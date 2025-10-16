### Assignment 03 Read-Me

This builds on the exploratory analysis you did for assignment #3. You will be submitting a link to your GitHub repository.

Using the same repository you created for assignment #3:

Add the cleaned up version of your data (if you needed to do pre-cleaning) to your data folder
Create a new notebook in the main folder that will be used for your regression analysis


Perform regression analysis on your dataset. You'll do this from two (2) different angles:

Interpretation
- Using the full dataset, create an OLS regression model using statsmodels.
- Which variables are significant and which are insignificant? What is the overall explanatory power of the model? Are there concerns about the residual distribution? Explain what you are seeing and provide any supporting charts.

Prediction
- Using a simple training and test split, split your data into two groups - one for modeling and another for evaluation.
- Run an OLS regression and comment on the predictive performance.
- Run a Ridge or Lasso regression with a few different levels of regularization strength. Does this help or hurt performance? What happens as you increase the regularization strength? How do the coefficients compare with OLS? Explain what you are seeing and provide any supporting charts.


Rubric:
- (10%) Data and notebook are included in the GitHub repository
- (10%) Jupyter Notebook
	- Markdown cells properly formatted. Major steps in the analysis should be described in the markdown and results should be discussed immediately after the code block.
	- All code blocks have output below - no errors or cells that weren’t executed.
	- Narratives are properly formatted, with correct grammar and punctuation.
- (10%) Output of professional quality
	- Charts properly labeled (axis labels, titles, …)
- (70%) Completeness of regression analysis
- (5%) Discussion of business question / objective that is being analyzed (variable you are running the regression on and why)
- (15%) Interpretation model - ran the regression model, print output, discussion of results
- (50%) Predictive models - ran the OLS model (10%), ran the Ridge or Lasso on multiple alpha (15%), commented on results (5%), compared coefficients (10%), explanation of findings (10%)


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