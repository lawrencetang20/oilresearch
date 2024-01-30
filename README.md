# Oil Research for MIT Sloan

## Folder Overview

LOOK AT FINAL_DATA.XLSX for more information, tab final python output

- **excel_csv** holds all downloaded data (could not get API without paying for a subscription for a majority of data)
- **final_products** holds all the code for the final graphs, and other data points needed for blog posts and publications; saved figures go into the saved_pngs folder (to change things, go to setup.py)
- **news_articles_august_2022** holds some interesting articles used to figure out what happened in August
- **other** holds original graphs I remade
- **saved_pngs** holds the png files of all the plots created by graphs in final_graphs
- **test_apis** holds code for some options for APIs that work, but do not support Urals and Brent
- **test_graphs** holds code for old graphs

## Installation

The following is needed to run the Python code (if you want to run it yourself; if not you can look straight to the SAVED_PNG folder for graphs and FINAL_DATA.XLSX in excel_csv folder for data):

Run the following in terminal:
- pip install mplcursors
- pip install investpy
- pip install requests
- pip install matplotlib
- pip install investpy
- pip install yahoofinancials
- pip install pandas

## Graphs

**with extended dates as far as possible**
![alt text](https://github.com/lawrencetang20/oilresearch/blob/main/saved_pngs/series_extended_with_treasury.png)

![alt text](https://github.com/lawrencetang20/oilresearch/blob/main/saved_pngs/series_extended_no_treasury.png)

![alt text](https://github.com/lawrencetang20/oilresearch/blob/main/saved_pngs/average_extended_no_treasury.png)

**with only matching dates**
![alt text](https://github.com/lawrencetang20/oilresearch/blob/main/saved_pngs/series_matching.png)

![alt text](https://github.com/lawrencetang20/oilresearch/blob/main/saved_pngs/average_matching_no_treasury.png)
