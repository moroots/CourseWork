# README
--- 
#### Author: M. Roots
#### Created: 12/13/2021
#### Last Modified: 12/14/2021

##### **This is LARGELY a passion project and will continue to be updated periodically........whenever I find the time** 
##### Link to Youtube Video: https://youtu.be/1hSgBiDsS_E
---

## This file is designed to give a brief introduction to the contents of this folder and their purpose. 

---

### Motivation

#### I am a budding investor. I have been engagement in the stock market since 2018, where I started with a simple investment account through Robinhood. I have since been on a fun journey to understand finances and money. I'd like to turn this project into an ML account manager for one of my investment accounts and see what it can do. Hopefully great things!

---

### Experiment 

#### Hypothesis: An ensemble model trained on handpicked momentum indicators from selective stocks, indicies, and commodities futures will yield sufficient results in predicting S&P 500 futures. 

#### Data Methods: Price is too noisy to attempt to predict. Some say it is quite literally a fools errand. So **instead of predicting price directly** I have decided to use a smoothed proxy with built in error. The target I have constructed is a 3 class system. I used the S&P500 index (^GSPC) difference in future 30 day expotential moving average (EMA) subtracted by the current EMA-30, divided by the current EMA-30. If the value was within plus or minus 10% change it was labeled as 0, if the value was greater that 10% change if was labeled 1, and if it was negative 10% change it was labeled as -1. This is too insure that the model will perform with in reason. For input data I've contructed a list of several handpicked stocks, indicies, and commodities that can easily be retrieved from yahoo finance and have persisted for over 20 years. These chosen symbols seem relavant to the S&P 500 as it is close too a wholistic view of the U.S.A markets. 

#### Overall: A Soft Voting Ensemble Classification model comprised of an SVM, KNN, and RF was created to generate S&P 500 futures using handpicked! 62% of last few years. 
- Better than a coin toss!
- Simple Implementation!
- Excellent Learning Experience!

#### Next Steps!!!
- Needs more tuning on Dataset & Models...
- Needs another thorough look through...
- Conversion into something deployable
- Train for 14-Day and 7-Day forecasts

---

### Contents

- ChooseModels.ipynb
    - A model evaluation file run on a smaller dataset for simplicity and speed.
    - Here the reader will find an EDA and the evaluations of each model tested. KNN, RF, SVM, NB, and DT. 
    - The best estimators from this experiment where then used on the larger dataset for full ensemble
    - There is a pdf version of this notebook as: Choosemodels - Jupyter Notebook.pdf

- CreatDataset.ipynb
    - A notebook file outlining the creation of the large dataset of which the ensemble will use to train, test, and predict.
    - There is a pdf version of this notebook as: CreateDataset - Jupyter Notebook.pdf
    
- ProjectNotebook.ipynb
    - This file is the final version of the ensemble model complete with evaluations of its performance.
    - The data from CreateDataset was used as test-data, training-data, and prediction-data.
    - There is a pdf version of this notebook as: ProjectNotebook - Jupyter Notebook.pdf

- BriefOverview.pptx
    - This is the full powerpoint slide deck for the presentation I gave in the linked youtube video and inside DATA602_TermProject.7z
    - There is a pdf version of this notebook as: BriefOverview.pdf
    
- data (Folder)
    - This folder contains the data that was created by CreateDataset.ipynb and saved as a csv file
    
- figures (Folder)
    - This folder contains some of the figures I wanted to save and use for the powerpoint
    
- reference (folder)
    - This folder contains some of the reference I used that were not linking directly in the notebooks
    
- ScratchPaper (folder)
    - This folder contains some files that I used to help create the repo that you see now. There are analogous to using scratch paper when solving a problem. They were a necessary portion of the brainstorming process and thus I did not want to delete them, perhaps there is something useful still inside. 
    
---
### Need Packages

#### Data Handling & Helpers
- import pandas as pd
- import numpy as np
- import pandas_ta as ta
- import yfinance as yf

#### Plotting
- import seaborn as sns
- import matplotlib.pyplot as plt
- from matplotlib.ticker import PercentFormatter

#### Processing
- from sklearn.decomposition import PCA
- from sklearn.pipeline import Pipeline
- from sklearn.preprocessing import StandardScaler
- from sklearn.model_selection import GridSearchCV
- from sklearn.model_selection import train_test_split

#### Models
- from sklearn.svm import SVC
- from sklearn.ensemble import VotingClassifier
- from sklearn.neighbors import KNeighborsClassifier
- from sklearn.ensemble import RandomForestClassifier

#### Model Evaluation
- from sklearn.metrics import confusion_matrix
- from sklearn.metrics import ConfusionMatrixDisplay
- from sklearn.model_selection import cross_val_score