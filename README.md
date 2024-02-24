# Oil Research for MIT Sloan

Created the graphs for this [blog post](https://cepr.org/voxeu/columns/how-make-price-cap-russian-oil-most-effective).

## Overview

Recreating graphs in section 2 of the paper. In each folder, it is broken up by figure (beside test folders).

- **documentation** holds all documentation needed to understand figures and code
- **excel_csv** holds all downloaded data (could not get API without paying for a subscription for a majority of data)
- **final_products** holds all the code for the final graphs, and other data points needed for blog posts and publications; saved figures go into the saved_pngs folder
- **other** holds other original documents pertaining to figures
- **saved_pngs** holds the png files of all the plots created
- **test_apis** holds code for some options for APIs that work, but do not support Urals and Brent
- **test_graphs** holds code for old graphs
- **theory_of_price_cap_paper.pdf** is the overall paper

## Installation

The following is needed to run the Python code:

Run the following in terminal:
- pip install mplcursors
- pip install investpy
- pip install requests
- pip install matplotlib
- pip install investpy
- pip install yahoofinancials
- pip install pandas
- python -m pip install numpy scikit-learn statsmodels

## Graphs

### Figure 1 - Russia's oil production: annual and monthly

![](/saved_pngs/figure_1/figure_1_part_a.png)
![](/saved_pngs/figure_1/figure_1_part_b.png)

### Figure 2 - Russia's seaborne crude oil exports by destination
![](/saved_pngs/figure_2/figure_2.png)

### Figure 3 - Russia's oil product exports by destination
![](/saved_pngs/figure_3/figure_3.png)

### Figure 4 - Russian Urals price minus Brent price: average and series of 4 sources
![](/saved_pngs/figure_4/average_extended_no_treasury.png)
![](/saved_pngs/figure_4/series_extended_no_treasury.png)
Both displaying no treasury.gov data.

### Figure 5 - Russia's oil extration versus Urals price
![](/saved_pngs/figure_5/regression.png)

### Figure 6 - Monthly Brent crude oil prices vs. commodity basket

### Figure 7 - Russia's government tax revenue

