# wikipedia-life-expectancy
### An End-to-end Supervised Machine Learning Project

## Table of Contents
- [Introduction](#intro)
- [Background](#back)
- [Project Overview](#over)
- [Explore the Project](#explore)
- [Insights](#insights)
- [Skills Demonstrated](#skills)
- [Application and Package Versions](#versions)
- [References](#refs)

<a id=intro a></a>
## Introduction
*If a person makes the [Wikipedia Notable Deaths](https://en.wikipedia.org/wiki/Deaths_in_2022) list,[<sup>1</sup>](#ref1) is there information there that can be used to model and predict that person's life span?*

In addition to demonstrating of a wide range of data science [skills](#skills), I had three portfolio project criteria: (1) to scrape the data from the Web, (2) to perform extensive data cleaning (i.e., messy data), and (3) to solve a regression problem.  Enter an exploration of life expectancy for Wikipedia notables, in the social sciences domain, and we're off and running\![<sup>2</sup>](#ref2)

<a id=back a></a>
## Background
"[Wikipedia](https://en.wikipedia.org/wiki/Wikipedia) is a multilingual free online encyclopedia written and maintained by a community of volunteers through open collaboration and a wiki-based editing system."[<sup>3</sup>](#ref3)  The English-language version contains a [List of deaths by year](https://en.wikipedia.org/wiki/Lists_of_deaths_by_year) of notable individuals, with links to pages for each year, by month, from 1987 to present.[<sup>4</sup>](#ref4)  The current page format is consistent as far back as January, 1994, with the following Wikipedia-defined fields for each entry:
> Name, age, country of citizenship at birth, subsequent country of citizenship (if applicable), reason for notability, cause of death (if known), and reference.[<sup>5</sup>](#ref5)  
> 
Year, month, and day of death are also readily available, as seen in the sample in [Image 1a](#img1a),[<sup>6</sup>](#ref6) from [Wikipedia Deaths in 2022, January](https://en.wikipedia.org/wiki/Deaths_in_January_2022).[<sup>7</sup>](#ref7)


At the bottom of an indvidual's page (following the Name link), is a References section for that individual's page.  [Image 1b](#img1b)[<sup>8</sup>](#ref8) contains a sample from [Ramiz Abutalibov's](https://en.wikipedia.org/wiki/Ramiz_Abutalibov) page[<sup>9</sup>](#ref9).
The number of references is easily scraped and can represent the individual's notability, quantified.  With this proxy for notability added, the above elements provide a framework for collecting the data.

<a id=over a></a>
## Project Overview
### Scrape.
<a id=img1a a></a>
<a id=img1b a></a>
![images/wp_snippet.jpg](images/wp_snippet.jpg)
### Combine.
![images/data_to_df_snippet.jpg](images/data_to_df_snippet.jpg)
### Clean.
![images/clean_snippet.jpg](images/clean_snippet.jpg)
### Explore and analyze.
![images/EDA_snippet.jpg](images/EDA_snippet.jpg)
### Preprocess.
![images/data_preproc_snippet.jpg](images/data_preproc_snippet.jpg)
### Model.  
![images/models_snippet.jpg](images/models_snippet.jpg)
### Interpret.
![images/interp_snippet.jpg](images/interp_snippet.jpg)
### Predict.
![images/predict_snnippet.jpg](images/predict_snippet.jpg)
  
  
<a id=explore a></a>
## Explore the Project
The links below access the Jupyter Notebooks that encompass the project.  Standalone contents and install/run instructions introduce each notebook, with a description of its corresponding version of the dataset.
- [Notebook 1: Data Collection](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wp_life_expect_data_collect_thanak_2022_06_10.ipynb)
- [Notebooks 2 - 9: Data Cleaning](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wp_life_expect_data_clean1_thanak_2022_06_13.ipynb)
- [Notebook 10: Exploratory Data Analysis](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wp_life_expect_EDA_thanak_2022_09_30.ipynb)
- [Notebook 11: Data Preprocessing](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wp_life_expect_data_preproc_thanak_2022_10_06.ipynb)
- [Notebook 12: Linear Regression -- Interpretation Emphasis](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wp_life_expect_olsmodel_thanak_2022_10_9.ipynb)
- [Notebook 13: Modeling for Regression -- Prediction Emphasis](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wp_life_expect_models_thanak_2022_10_14.ipynb)  

Web scraping steps are in Notebook 1, including details of the PyCharm project folder and links to its contents.

**Observations** appear throughout each notebook, documenting immediate context.  Exploratory Data Analysis, Linear Regression, and Modeling for Regression (Notebooks 10, 12, and 13) have additional **Summary**, **Insights**, or **Conclusion** sections at the end of their main content.

The link at the end of each notebook opens the next notebook.  [Return to README](https://github.com/teresahanak/wikipedia-life-expectancy#explore-the-project) links are available at the top and bottom of each notebook, to return to these insructions.  

[References](#refs) for the entire project are on this page.  Individual notebooks have self-contained footnotes.

<a id=insights a></a>
## Insights

<a id=skills a></a>
## Skills Demonstrated
- Virtual Environments
  - Anaconda Navigator
- Coding in Python
    - PyCharm
    - Jupyter Notebooks
- Version control
    - Git
    - GitHub
    - [ReviewNB](https://www.reviewnb.com/)
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
- Linear regression modeling--interpretation emphasis
    - Assumptions of linear regression
    - Interpretation of coefficients
- Regressor algorithms--prediction emphasis
    - scikit-learn regressors
    - XGBoost
    - Hyperparamter tuning
    - Cross validation
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

<a id=versions a></a>
## Application and Package Versions
- Anaconda Navigator 2.2.0 virtual environment
- Python 3.9.12
- Scrapy (2.6.1)
- PyCharm Professional 2021.1.2
- Protego (0.2.1)  
- Jupyter Notebook 6.4.8
- NumPy 1.223
- pandas 1.4.2
- pip 21.2.4
- SQLite 3.38.3
- [nb_black](https://pypi.org/project/nb-black/)
- [chime 0.5.3](https://pypi.org/project/chime/)
- Matplotlib 3.5.1
- scikit-learn 1.0.2
- seaborn 0.11.2
- statsmodels 0.13.2
- PyLab
- SciPy 1.7.3
- XGBoost 1.6.1
##
<a id=ref1 a></a>.
1. "Deaths in 2022," Wikipedia, accessed October 23, 2022, https://en.wikipedia.org/wiki/Deaths_in_2022.
<a id=ref2 a></a>
2. "Lists of deaths by year," Wikipedia, accessed October 23, 2022, https://en.wikipedia.org/wiki/Lists_of_deaths_by_year.
<a id=ref3 a></a>
3. "Wikipedia," Wikipedia, accessed October 23, 2022, https://en.wikipedia.org/wiki/Wikipedia.
<a id=ref4 a></a>
4. See note 3 above.
<a id=ref5 a></a>
5. See note 1 above.
<a id=ref6 a></a>
6. "File:Wikipedia Deaths Jan 2022 snippet.png," Wikimedia Commons, accessed October 23, 2022, https://commons.wikimedia.org/wiki/File:Wikipedia_Deaths_Jan_2022_snippet.png.
<a id=ref7 a></a>
7. "Deaths in January 2022," Wikipedia, accessed October 23, 2022, https://en.wikipedia.org/wiki/Deaths_in_January_2022.
<a id=ref8 a></a>
8. "File:Screenshot snippet of Wikipedia Ramiz Abutalibov References.png," Wikimedia Commons, accessed October 23, 2022, https://commons.wikimedia.org/wiki/File:Screenshot_snippet_of_Wikipedia_Ramiz_Abutalibov_References.png.
<a id=ref9 a></a>
9. "Ramiz Abutalibov," Wikipedia, accessed October 23, 2022, https://en.wikipedia.org/wiki/Ramiz_Abutalibov.

<a id=refs a></a>
## References
