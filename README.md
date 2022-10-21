# wikipedia-life-expectancy
#### An End-to-end Supervised Machine Learning Project




## Introduction
*If a person makes the [Wikipedia Notable Deaths](https://en.wikipedia.org/wiki/Deaths_in_2022) list, is there information there that can be used to model and predict that person's life span?*[<sup>[1]</sup>](#ref1)

In addition to demonstrating of a wide range of data science [skills](#skills), I had three portfolio project criteria: (1) to scrape the data from the Web, (2) to perform extensive data cleaning (i.e., messy data), and (3) to solve a regression problem.  Enter a social-sciences-based exploration of life expectancy for Wikipedia notables and we're off and running!


## Background
"[Wikipedia](https://en.wikipedia.org/wiki/Wikipedia) is a multilingual free online encyclopedia written and maintained by a community of volunteers through open collaboration and a wiki-based editing system."[<sup>[2]</sup>](#ref2)  The English-language version contains a [List of deaths by year](https://en.wikipedia.org/wiki/Lists_of_deaths_by_year) of notable individuals, with links to pages for each year, by month, from 1987 to present.[<sup>[3]</sup>](#ref3)  The current page format is consistent as far back as January, 1994, with the following Wikipedia-defined fields for each entry:
> Name, age, country of citizenship at birth, subsequent country of citizenship (if applicable), reason for notability, cause of death (if known), and reference.[<sup>[1]</sup>](#ref1)  
> 
Year, month, and day of death are also readily available, as seen in the sample in [Image 1a](#img1a), from [Wikipedia Deaths in 2022](https://en.wikipedia.org/wiki/Deaths_in_2022).[<sup>[1]</sup>](#ref1)


At the bottom of an indvidual's page (following the Name link), is a References section for that individual's page.  [Image 1b](#img1b) contains a sample from [Ramiz Abutalibov's](https://en.wikipedia.org/wiki/Ramiz_Abutalibov) page.[<sup>[4]</sup>](#ref4)
The number of references is easily scraped and can represent the individual's notability, quantified.  With this proxy for notability added, the above elements provide a framework for collecting the data.

## Project Overview
### Scrape.
<a id=img1a a></a>
<a id=img1b a></a>
![wp_snippet.jpg](wp_snippet.jpg)
### Combine.
![data_to_df_snippet.jpg](data_to_df_snippet.jpg)
### Clean.
![clean_snippet.jpg](clean_snippet.jpg)
### Explore and analyze.
![EDA_snippet.jpg](EDA_snippet.jpg)
### Preprocess.
![data_preproc_snippet.jpg](data_preproc_snippet.jpg)
### Model.  
![models_snippet.jpg](models_snippet.jpg)
### Interpret.
![interp_snippet.jpg](interp_snippet.jpg)
### Predict.
![predict_snnippet.jpg](predict_snippet.jpg)
  
  
<a id=#read a></a>
## Explore the Project
13 Jupyter notebooks encompass the project:
- [Notebook 1: Data Collection](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wp_life_expect_data_collect_thanak_2022_06_10.ipynb)
- [Notebooks 2 - 9: Data Cleaning](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wp_life_expect_data_clean1_thanak_2022_06_13.ipynb)
- [Notebook 10: Exploratory Data Analysis](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wp_life_expect_EDA_thanak_2022_09_30.ipynb)
- [Notebook 11: Data Preprocessing](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wp_life_expect_data_preproc_thanak_2022_10_06.ipynb)
- [Notebook 12: Linear Regression -- Interpetation Emphasis](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wp_life_expect_olsmodel_thanak_2022_10_9.ipynb)
- [Notebook 13: Modeling for Regression -- Prediction Emphasis](http://localhost:8888/notebooks/anaconda3/envs/wikipedia-life-expectancy/wp_life_expect_models_thanak_2022_10_14.ipynb)  

Standalone contents and instructions introduce each notebook, including a data description for the dataset, in its current form, as it is loaded into the notebook. 

Notebook 1 contains Web-scraping instructions, including details of the PyCharm project folder and links to its contents.  

**Observations** appear throughout each notebook, documenting immediate context.  Exploratory Data Analysis, Linear Regression, and Modeling for Regression notebooks (10, 12, and 13) have additional "Summary", "Insights", or "Conclusion" sections at the end of their main content.

The link at the end of each notebook opens the subsequent notebook.  [Return to README](https://github.com/teresahanak/wikipedia-life-expectancy#read-the-project) links are available at the top and bottom of each notebook, to return to these insructions.  

The [References](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/README.md#references) section, on this page, is inclusive for all notebooks and files within the project.

## Run It
See individual notebooks for standalone instructions to run that phase of the project.
  - Anaconda Navigator 2.2.0
  - Jupyter Notebook 6.4.8
  - Python 3.9.12
  - NumPy 1.223
  - pandas 1.4.2
  - pip 21.2.4
  - sqlite 3.38.3
  - sklearn 1.0.2
  - [nb_black](https://pypi.org/project/nb-black/)



The [Web-scraping step](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wp_life_expect_data_collect_thanak_2022_06_10.ipynb) is reproducible, with the following caveats:
1. Wikipedia evolves with contribution and editing, so scraping even the identical dates will likely result in at least some minor variation in the raw dataset.
2. Converting the raw data for what an individual was known, into a predictive categorical feature, is a programmatically-driven manual process.  Though faster than manual entry, and arguably more accurate, it has the same specificity to the dataset.  If new data is scraped, particularly for a different time period, it will need this cleaning step recoded to match the new data (no small feat!).
3. The [pipelines.py](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/wikipedia_life_expectancy/pipelines.py) file is reused for all [spiders](https://github.com/teresahanak/wikipedia-life-expectancy/tree/main/wikipedia_life_expectancy/spiders) within the [Scrapy project folder](https://github.com/teresahanak/wikipedia-life-expectancy/tree/main/wikipedia_life_expectancy), so requires updating to match the spider that will be crawled.  [Frank Andrade's course](https://www.udemy.com/share/1050RC3@hQ2ccLlpcvivy0WcwxoyY-pTDZW1ATRujXa3_csxIPkk6f4MV3Ogh20gLzy_BSAf/) instructions for Scrapy were followed.
4. Due to 1-3, reproducing the scraping steps as an exercise in Web scraping with Scrapy is recommended, over aiming to duplicate the results here from start to finish.  For comparitive results, choosing any entry point after scraping is the better option.

Follow [these instructions](https://www.youtube.com/watch?v=ooNngLWhTC4) from Frank Andrade, to set up Anaconda virtual environment and Scrapy.
1. Create virtual environment with Anaconda Navigator (2.2.0)
2. Install Scrapy (2.6.1) in the virtual environment
3. Synch PyCharm (Professional 2021.1.2) to the Anaconda virtual environment
4. Install protego (0.2.1)



## Insights and Hindsights

<a id=skills a></a>
## Skills Demonstrated
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




## References
