# Oil Research for MIT Sloan under Professor Catherine Wolfram by Lawrence Tang

## Folder Overview

-- **excel_csv** holds all downloaded data (could not get API without paying for subscription for majority of data)

-- **final_products** holds all the code for the finals graphs, and other data points ne
eded for blog posts and publications for Catherine Wolfram, plots are interactive using matplotlib, saved figures go into the saved_pngs folder (to change things, go to setup.py)

-- **other** holds original graphs I remade

-- **saved_pngs** holds the png files of all the plots created by graphs in final_graphs

-- **test_apis** holds code for some options for APIs that work, but do not support Urals and Brent

-- **test_graphs** holds code for old graphs

## Installments

The following is needed to run the python code (if you want to run it yourself; if not you can look straight to SAVED_PNG folder for graphs):

Run the following in terminal:
- pip install mplcursors
- pip install investpy
- pip install requests
- pip install matplotlib
- pip install investpy
- pip install yahoofinancials

## Sources

Investing.com includes data from all over the world (countries including US, India, Spain, Russia, and many others). From their website, they "receive data from various sources, which include the biggest financial data providers as well as real-time market maker CFDs." It ranks similar to Fidelity and Yahoo Finance in reliability, being among the top three financial sites worldwide (ranked by SimilarWeb). Statista sources its oil data from Thomson Reuters. Reuters is regarded highly by those looking to source real time trusted data and services. Bloomberg sources its data from a number data centers throughout the world, obtaining feeds from exchanges and securities information processors. This historical data was obtained through the Bloomberg Terminal. Similar to Reuters, Bloomberg is trusted by many, with most large financial firms having subcriptions to Bloomberg Professional Services. While all three sources are trustworthy, there may be discrepanies which occur when collecting data which may explain the different Urals discounts for each source in the three_series.py plot. Thus, an average plot of all three sources should give a holistic view of the large oil data trends since 2022.

## Transformations

There were a few transformations made to each of the data sources. When collecting data from Bloomberg and Investing.com, the value returned for each date was the last price of the commodity on that day (for both Brent and Urals). The discount was calculated manually. If the last price was plotted, there would be lots of shifts and volatility, and thus these graphs opted to use a last five days rolling average; this change was made to accommodate the data from Statista. The Statista data was already using a last five days rolling average, and thus to match all three sources in order to compare and take the average of all three, all three source data use a last five days rolling average.

Furthermore, some data sources had incomplete dates. For example, Bloomberg may have reported data on date A while Investing.com did not. Thus, in order to make sure that all three data sources had all the same dates, the code filters through all the dates and only kept the matching dates and their corresponding prices. This same idea was implemented in finding the averages for the thee periods in period_averages.py. If the start date was not in the reported dates for a data source, we started at the next available date after the start date. Mirroring this for the end date, if the end date was not in the reported dates for a data source, we ended at the last available date before the end date.

## Period Averages (from running final_products/period_averages.py)

Period 1:

In the order of Investing, Statista, Bloomberg

-10.14 -15.72 -16.04


Period 2:

In the order of Investing, Statista, Bloomberg

-8.35 -15.02 -12.85


Period 3

In the order of Investing, Statista, Bloomberg

-12.16 -18.14 -12.07

## News Analysis Summary

The next step was to see if there were any explanations for the large upspikes in urals discount in (as seen in the three_average.py plot).

