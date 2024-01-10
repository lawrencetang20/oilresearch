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

The following is needed to run the python code:

Run the following in terminal:
- pip install mplcursors
- pip install investpy
- pip install requests
- pip install matplotlib
- pip install investpy
- pip install yahoofinancials

## Sources

Investing.com includes data from all over the world (countries including US, India, Spain, Russia, and many others). From their website, they "receive data from various sources, which include the biggest financial data providers as well as real-time market maker CFDs." It ranks similar to Fidelity and Yahoo Finance in reliability, being among the top three financial sites worldwide (ranked by SimilarWeb). Statista sources its oil data from Thomson Reuters. Reuters is regarded highly by those looking to source real time trusted data and services. Bloomberg sources its data from a number data centers throughout the world, obtaining feeds from exchanges and securities information processors. This historical data was obtained through the Bloomberg Terminal. Similar to Reuters, Bloomberg is trusted by many, with most large financial firms having subcriptions to Bloomberg Professional Services. While all three sources are trustworthy, there may be discrepanies which occur when collecting data which may explain the different Urals discounts for each source in the "three_series" plot. Thus, an average plot of all three sources should give us holistic view of the large oil data trends since 2022.

## Transformations

There were a few transformations made to each of the data sources. When collecting data from Bloomberg and 

## Analysis

