![Your Repository's Stats](https://github-readme-stats.vercel.app/api?username=teresahanak&show_icons=true)  
![Profile View Counter](https://komarev.com/ghpvc/?username=teresahanak) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/teresahanak/wikipedia-life-expectancy) ![GitHub contributors](https://img.shields.io/github/contributors/teresahanak/wikipedia-life-expectancy) ![GitHub language count](https://img.shields.io/github/languages/count/teresahanak/wikipedia-life-expectancy) ![GitHub top language](https://img.shields.io/github/languages/top/teresahanak/wikipedia-life-expectancy) ![GitHub last commit](https://img.shields.io/github/last-commit/teresahanak/wikipedia-life-expectancy)  [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
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
- [Other Credits](#credit)
- [Contributions](#contributions)
- [Licenses](#license)

<a id=intro a></a>
## Introduction
***If a person makes the [Wikipedia Notable Deaths](https://en.wikipedia.org/wiki/Deaths_in_2022) list,[<sup>1</sup>](#ref1) is there information there that can be used to model and predict that person's life span?***


In addition to demonstrating of a wide range of data science [skills](#skills), I had three portfolio project criteria: (1) to scrape the data from the Web, (2) to perform extensive data cleaning (i.e., messy data), and (3) to solve a regression problem.  Enter an exploration of life expectancy for Wikipedia notables, in the social sciences domain, and we're off and running\![<sup>2</sup>](#ref1)

<a id=back a></a>
## Background
"[Wikipedia](https://en.wikipedia.org/wiki/Wikipedia) is a multilingual free online encyclopedia written and maintained by a community of volunteers through open collaboration and a wiki-based editing system."[<sup>3</sup>](#ref1)  The English-language version contains a [List of deaths by year](https://en.wikipedia.org/wiki/Lists_of_deaths_by_year) of notable individuals, with links to pages for each year, by month, from 1987 to present.[<sup>4</sup>](#ref1)  The current page format is consistent as far back as January, 1994, with the following Wikipedia-defined fields for each entry:
> Name, age, country of citizenship at birth, subsequent country of citizenship (if applicable), reason for notability, cause of death (if known), and reference.[<sup>5</sup>](#ref1)  
> 
Year, month, and day of death are also readily available, as seen in the sample in [Image 1a](#img1a),[<sup>6</sup>](#ref1) from [Wikipedia Deaths in 2022, January](https://en.wikipedia.org/wiki/Deaths_in_January_2022).[<sup>7</sup>](#ref1)


At the bottom of an indvidual's page (following the Name link), is a References section for that individual's page.  [Image 1b](#img1b)[<sup>8</sup>](#ref1) contains a sample from [Ramiz Abutalibov's](https://en.wikipedia.org/wiki/Ramiz_Abutalibov) page[<sup>9</sup>](#ref1).
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

The link at the end of the main content of each notebook opens the next notebook.  [Return to README](https://github.com/teresahanak/wikipedia-life-expectancy#explore-the-project) links are also available at start and end of the main content of each notebook, to return to these instructions.

[References](#refs) for the entire project are on this page.  Individual notebooks and README have self-contained footnotes.    

  ![images/refresh_snippet.jpg](images/refresh_snippet.jpg)


<a id=insights a></a>
## Insights



<a id=ref1 a></a>
##
1. "Deaths in 2022," Wikipedia, last modified October 24, 2022, https://en.wikipedia.org/wiki/Deaths_in_2022.
2. "Lists of deaths by year," Wikipedia, last modified October 1, 2022, https://en.wikipedia.org/wiki/Lists_of_deaths_by_year.
3. "Wikipedia," Wikipedia, last modified October 20, 2022, https://en.wikipedia.org/wiki/Wikipedia.
4. See note 3 above.
5. See note 1 above.
6. "File:Wikipedia Deaths Jan 2022 snippet.png," Wikimedia Commons, last modified October 23, 2022, https://commons.wikimedia.org/wiki/File:Wikipedia_Deaths_Jan_2022_snippet.png.
7. "Deaths in January 2022," Wikipedia, last modified October 24, 2022, https://en.wikipedia.org/wiki/Deaths_in_January_2022.
8. "File:Screenshot snippet of Wikipedia Ramiz Abutalibov References.png," Wikimedia Commons, last modified October 23, 2022, https://commons.wikimedia.org/wiki/File:Screenshot_snippet_of_Wikipedia_Ramiz_Abutalibov_References.png.
9. "Ramiz Abutalibov," Wikipedia, last modified May 14, 2022, 2022, https://en.wikipedia.org/wiki/Ramiz_Abutalibov.

<a id=skills a></a>
## Skills Demonstrated
- Virtual Environments
  - Anaconda Navigator
- Coding and Documentation
    - Python
    - PyCharm
    - Jupyter Notebook
    - Markdown
    - HTML
    - LaTeX
- Version Control
    - Git
    - GitHub
    - [ReviewNB](https://www.reviewnb.com/) (tool used without reproduction)
- Web scraping
    - Scrapy
- Relational Database Management
    - SQLite
    - [SQLite Viewer](https://inloop.github.io/sqlite-viewer/) (tool used without reproduction)
- Data Cleaning
    - Python Built-in String Methods
    - regular expressions
    - pandas
- Exploratory Data Analysis
    - NumPy
    - pandas
    - Matplotlib
    - Seaborn
- Data Preprocessing
    - Feature Extraction
    - Transformations
- Linear Regression Modeling--Interpretation Emphasis
    - Assumptions
    - Coefficient Interpretation
- Regressor Algorithms--Prediction Emphasis
    - scikit-learn Regressors
    - XGBoost
    - Hyperparamter Tuning
    - Cross validation
- Model Performance Evaluation
    - RMSE
    - MAE
    - $R^2$
    - Adjusted $R^2$
    - MAPE
- Pipelines
    - Custom Transformers
    - Production Pipeline
- User Interface for Predictions
<a id=versions a></a>
## Application and Package Versions
- [Anaconda Navigator](https://docs.anaconda.com/navigator/index.html) 2.2.0 virtual environment
- [chime 0.5.3](https://pypi.org/project/chime/)
- [Jupyter Notebook](https://jupyter.org/) 6.4.8
- [Matplotlib](https://matplotlib.org/) 3.5.1
- [nb_black](https://pypi.org/project/nb-black/)
- [NumPy](https://numpy.org/) 1.223
- [pandas](https://pandas.pydata.org/) 1.4.2
- [pip](https://pypi.org/project/pip/) 21.2.4
- [Protego](https://github.com/scrapy/protego) (0.2.1)  
- [PyCharm](https://www.jetbrains.com/pycharm/) Professional 2021.1.2
- [PyLab](https://scipy.github.io/old-wiki/pages/PyLab)
- [Python](https://www.python.org/) 3.9.12
- [ReviewNB](https://www.reviewnb.com/) (tool used without reproduction)
- [scikit-learn](https://scikit-learn.org/stable/) 1.0.2
- [SciPy](https://scipy.org/) 1.7.3
- [Scrapy](https://scrapy.org/) (2.6.1)
- [seaborn](https://seaborn.pydata.org/) 0.11.2
- [SQLite](https://www.sqlite.org/index.html) 3.38.3
- [SQLite Viewer](https://inloop.github.io/sqlite-viewer/) (tool used without reproduction)
- [statsmodels](https://www.statsmodels.org/stable/index.html) 0.13.2
- [XGBoost](https://xgboost.readthedocs.io/en/stable/) 1.6.1


<a id=refs a></a>
## References
Andrade, Frank. "Python Scrapy for Beginners — A Complete Web Scraping Project [Web Scraping with Python]." 2021 YouTube video, 34:17. Posted by Frank Andrade. November 9, 2021. https://www.youtube.com/watch?v=ooNngLWhTC4.

Andrade, Frank. "Web Scraping in Python BeautifulSoup, Selenium & Scrapy 2022 (Scrapy modules)." 2022 Udemy course, 98 minutes. Posted by Frank Andrade. Last modified June, 2022. https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/.

DePaul University. "Linear Correlation." Accessed November 1, 2022, https://condor.depaul.edu/sjost/it223/documents/correlation.htm.

Huizendveld, Marjin. *List of nationalities*. GitHub. Accessed June 17, 2022. https://gist.github.com/marijn/274449#file-nationalities-txt.

Kiprop, Victor. "A List of Nationalities." WorldAtlas. Last modified May 14, 2018. https://www.worldatlas.com/articles/what-is-a-demonym-a-list-of-nationalities.html.

Krishna and Ethan. "How to download a Jupyter Notebook from GitHub?" *Stack Exchange, Data Science* (blog).  Last modified 21 September 2021. 
https://datascience.stackexchange.com/questions/35555/how-to-download-a-jupyter-notebook-from-GitHub.

Lewinson, Eryk. "Coding a custom imputer in scikit-learn." Towards Data Science. May 21, 2020. https://towardsdatascience.com/coding-a-custom-imputer-in-scikit-learn-31bd68e541de.

Nations Online Project. "Map of the World's Continents and Regions."  Accessed June 29, 2022, https://www.nationsonline.org/oneworld/small_continents_map.htm.

Wikimedia Commons. "File:Screenshot snippet of Wikipedia Ramiz Abutalibov References.png." Last modified October 23, 2022. https://commons.wikimedia.org/wiki/File:Screenshot_snippet_of_Wikipedia_Ramiz_Abutalibov_References.png.

Wikimedia Commons. "File:Wikipedia Deaths Jan 2022 snippet.png." Last modified October 23,2022. https://commons.wikimedia.org/wiki/File:Wikipedia_Deaths_Jan_2022_snippet.png.

Wikipedia. "Deaths in 2022." Last modified October 24, 2022. https://en.wikipedia.org/wiki/Deaths_in_2022. 

Wikipedia. "Deaths in January 1994" through "Deaths in June 2022" (through June 9, 2022) and each listed individual's page. Accessed (scraped) June 9-10, 2022, https://en.wikipedia.org/wiki/Deaths_in_January_1994.

Wikipedia. "Deaths in January 2022."  Last modified October 24, 2022. https://en.wikipedia.org/wiki/Deaths_in_January_2022.

Wikipedia. "Lists of deaths by year." Last modified October 1, 2022. https://en.wikipedia.org/wiki/Lists_of_deaths_by_year.

Wikipedia. "Ramiz Abutalibov."  Last modified May 14, 2022. https://en.wikipedia.org/wiki/Ramiz_Abutalibov.

Wikipedia. "Sudhakar Chaturvedi." Last modified October, 24, 2022.  https://en.wikipedia.org/wiki/Sudhakar_Chaturvedi.

Wikipedia. "Wikipedia." Last modified October 20, 2022. https://en.wikipedia.org/wiki/Wikipedia.

<a id=credit a></a>
## Other Credits
The overall approach to coding in Python, analysis and modeling, and a majority of the plots (Notebooks 10, 11, 12, and 13, and Project Overview images above) are adapted from examples learned in [The University of Texas McCombs School of Business Post Graduate Program in Data Science and Business Analytics in partnership with Great Learning](https://www.mygreatlearning.com/ut-austin-data-science-business-analytics-program?&utm_source=google&utm_medium=search&utm_campaign=BA_Int_Search_Brand_Broad_US&adgroup_id=124131117771&campaign_id=12451747881&Keyword=ut%20austin%20data%20science&placement=&gclid=Cj0KCQjwteOaBhDuARIsADBqRegPrwBrU9zW94FIAU9pNhR1pKb_iM1R52yPuee33gKlc6Aa4O-YzmYaAhoKEALw_wcB).

Git and GitHub implementation were acquired from Anna Skoulikari, through the Udemy course, [Git Learning Journey - Guide to Learn Git (Version Control)](https://www.udemy.com/share/102FUK3@gXOY8-8NIGjJAqOsTNhyO2n7DZU_PXlQaXytDb055i6wsiLN0PYjXXLc5CgsBGWE/).

Review of Jupyter Notebooks for pull requests on GitHub was entirely dependent on ReviewNB, following Amit Rathi's instructions in the Towards Data Science article, ["How to use Git / GitHub with Jupyter Notebook"](https://towardsdatascience.com/how-to-use-git-github-with-jupyter-notebook-7144d6577b44).

Web scraping with Scrapy was learned from Frank Andrade, through the Udemy course, [Web Scraping in Python BeautifulSoup, Selenium & Scrapy 2022](https://www.udemy.com/share/1050RC3@OPQBrWla1wb5dcRcMS85QPUjfv5L0Oh_D2zoekwqDPKrFKWCzRD1NlqRzdEWUzNo/).

Though not extensively used in this project, SQL implementation was acquired from Jose Portilla, through the Udemy course, [The Complete SQL Bootcamp 2022: Go from Zero to Hero](https://www.udemy.com/share/101Whk3@9gWCE0SdPuKlezaUcy_GNhWrQ8ZkhLvMl7_AjRoovgr6p8O6dJVtd5TGmF4OKBWb/).

Custom imputer coding steps are from Eryk Lewinson's Towards Data Science article, ["Coding a custom imputer in scikit-learn"](https://towardsdatascience.com/coding-a-custom-imputer-in-scikit-learn-31bd68e541de), with the addition of a strategy for mode.

<a id=contributions a></a>
## Contributions
This project serves as an end-to-end portfolio project for its author, as sole contributor.
<a id=license a></a>
## [Licenses](https://github.com/teresahanak/wikipedia-life-expectancy/blob/main/Licenses.txt)
#### Text and Wikipedia Data (excludes images and scraped and downloaded data for nationality/country/demonyms--see original sources):
wikipedia-life-expectancy (Text and Data) © 2022 by Teresa Hanak is licensed under CC BY-SA 4.0 

#### Code (excludes data and plots):
wikipedia-life-expectancy (Code) released under MIT License  
Copyright 2022 Teresa Hanak
