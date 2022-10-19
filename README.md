# wikipedia-life-expectancy
#### An End-to-end Supervised Machine Learning Project




## Introduction
*If a person makes the [Wikipedia Notable Deaths](https://en.wikipedia.org/wiki/Deaths_in_2022) list, is there information there that can be used to model and predict that person's life span?*[<sup>[1]</sup>](#ref1)

The above problem question answers its predecessor: "What should I do for a portfolio project?"  In addition to allowing the demonstration of a wide range of data science [skills](#skills), I had three
 portfolio project criteria: (1) to scrape the data from the Web, (2) to perform extensive data cleaning (i.e., messy data), and (3) to solve a regression problem.  Enter Wikipedia Notable Deaths and we're off!


## Background
"[Wikipedia](https://en.wikipedia.org/wiki/Wikipedia) is a multilingual free online encyclopedia written and maintained by a community of volunteers through open collaboration and a wiki-based editing system."[<sup>[2]</sup>](#ref2)  The Enlish-language version contains a [List of deaths by year](https://en.wikipedia.org/wiki/Lists_of_deaths_by_year) of notable individuals, with links to pages for each year, by month, from 1987 to present (2022).[<sup>[3]</sup>](#ref3)  The fields for each entry are defined by Wikipedia as:
> Name, age, country of citizenship at birth, subsequent country of citizenship (if applicable), reason for notability, cause of death (if known), and reference.[<sup>[4]</sup>](#ref4)  Image 1 contains a sample from [Deaths in 2022](https://en.wikipedia.org/wiki/Deaths_in_2022) for the month of January.[<sup>[4]</sup>](#ref4)
![wp_snippet.jpg](wp_snippet.jpg)  

  
So, the list itself contains the following information for each individual:
- Year, month, and day of death
- Name (linked to the individual's page)
- Place of residency at birth
- Subsequent place of residency (if the person relocated)
- What the person was known for
- Cause of death (if known)  

At the bottom of an indvidual's page (after following the Name link), there is a References section for that individual's page.  Image 2 contains a sample from [Ramiz Abutalibov's](https://en.wikipedia.org/wiki/Ramiz_Abutalibov) page.[<sup>[5]</sup>](#ref5)





![sqlite_snippet1.jpg](sqlite_snippet1.jpg)

![refs_snippet.jpg](refs_snippet.jpg)

![sqlite_snippet2.jpg](sqlite_snippet2.jpg)

## Table of Contents



<a id=skills a></a>
#### Skills Demonstrated
- Coding in Python
    - PyCharm
    - Jupyter Notebooks
- Version control
    - Git
    - GitHub
    - ReviewNB
- Web scraping
    - Scrapy
- Relational database management
    - SQLite
    - [SQLite Viewer](https://inloop.github.io/sqlite-viewer/)
- Data cleaning
    - Python built-in string methods
    - regular expressions
    - pandas
- Exploratory Data Analysis
    - NumPy
    - pandas
    - Matplotlib
    - Seaborn
- Data preprocessing
    - Feature extraction
    - Transformations
- Linear Regression Modeling for Interpretation
    - Assumptions of Linear Regression
- Modeling Algorithms for Prediction
    - scikit-learn regressors
    - XGBoost
    - Hyperparamter Tuning
    - Cross Validation
- Model Performance Evaluation
    - RMSE
    - MAE
    - R<sup>2</sup>
    - Adjusted R<sup>2</sup>
    - MAPE
- Pipelines
    - Custom transformers
    - Production pipeline
- User interface for predictions

## Data Dictionary
Variable: Description




## References
