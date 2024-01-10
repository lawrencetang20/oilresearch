# Oil Research for MIT Sloan under Professor Catherine Wolfram

## Folder Overview

-- **excel_csv** holds all downloaded data (could not get API without paying for a subscription for a majority of data)

-- **final_products** holds all the code for the final graphs, and other data points needed for blog posts and publications for Catherine Wolfram, plots are interactive using matplotlib, and saved figures go into the saved_pngs folder (to change things, go to setup.py)

-- **other** holds original graphs I remade

-- **saved_pngs** holds the png files of all the plots created by graphs in final_graphs

-- **test_apis** holds code for some options for APIs that work, but do not support Urals and Brent

-- **test_graphs** holds code for old graphs

## Installation

The following is needed to run the Python code (if you want to run it yourself; if not you can look straight to the SAVED_PNG folder for graphs):

Run the following in terminal:
- pip install mplcursors
- pip install investpy
- pip install requests
- pip install matplotlib
- pip install investpy
- pip install yahoofinancials

## Sources

Investing.com includes data from all over the world (countries including the US, India, Spain, Russia, and many others). From their website, they "receive data from various sources, which include the biggest financial data providers as well as real-time market maker CFDs." It ranks similar to Fidelity and Yahoo Finance in reliability, being among the top three financial sites worldwide (ranked by SimilarWeb). Statista sources its oil data from Thomson Reuters. Reuters is regarded highly by those looking to source real-time trusted data and services. Bloomberg sources its data from several data centers throughout the world, obtaining feeds from exchanges and securities information processors. This historical data was obtained through the Bloomberg Terminal. Similar to Reuters, Bloomberg is trusted by many, with most large financial firms having subscriptions to Bloomberg Professional Services. While all three sources are trustworthy, there may be discrepancies that occur when collecting data which may explain the different Urals discounts for each source in the three_series.py plot. Thus, an average plot of all three sources should give a holistic view of the large oil data trends since 2022.

## Data Transformations

There were a few transformations made to each of the data sources. When collecting data from Bloomberg and Investing.com, the value returned for each date was the last price of the commodity on that day (for both Brent and Urals). The discount was calculated manually (Urals price minus Brent price). If the last price was plotted, there would be lots of shifts and volatility, and thus these graphs opted to use a last five days rolling average; this change was made to accommodate the data from Statista. The Statista data was already using a last five days rolling average, and thus to match all three sources to compare and take the average of all three, all three source data use a last five days rolling average.

Furthermore, some data sources had incomplete dates. For example, Bloomberg may have reported data on date A while Investing.com did not have date A. Thus, to make sure that all three data sources had the same dates, the code filters through all the dates and only kept the matching dates and their corresponding prices. This same idea was implemented in finding the averages for the three periods in period_averages.py. If the start date was not in the reported dates for a data source, we started at the next available date after the start date. Mirroring this for the end date, if the end date was not in the reported dates for a data source, we ended at the last available date before the end date.

## Period Averages (from running final_products/period_averages.py)

**Period 1 from 09/14/23 to 10/12/23:**

In the order of Investing, Statista, Bloomberg

-10.14 -15.72 -16.04


**Period 2 from 10/13/23 to 11/16/23:**

In the order of Investing, Statista, Bloomberg

-8.35 -15.02 -12.85


**Period 3 from 11/17/23 to 01/10/24:**

In the order of Investing, Statista, Bloomberg

-12.16 -18.14 -12.07

## News Analysis Summary

The next step was to see if there were any explanations for the large up spikes in the Urals discount (as seen in the three_average.py plot), particularly in August of 2022 and February of 2023.

After parsing through the data, it showed that the jump in Urals discount in August started mainly on 08/18/22. At this point in Russia, there were a couple of developments in the war. Russia replaced the commander of the Black Sea Fleet (the fleet of the Russian Navy) with Vice Admiral Viktor N. Sokolov. Russian villages Timonova and Soloti nineteen miles from the Ukranian border were also evacuated. Furthermore, a trilateral meeting happened in Lviv with the Turkish president, UN secretary-general, and Ukrainian president to discuss the war. Lastly, Wagner, a private military company came into play as well. Russian troops were reported to be struggling in Ukraine, and thus Wagner mercenaries started to enter the spotlight. The Wagner owner was awarded the Hero of Russia, Russia's highest merit. The heroic exploits of the company flowed throughout Russian official media. Overall, there was unexpected resilience in Russian oil output, as Russia pumped less oil on the eve of the impending invasion.

The jump in the Urals discount in February started slowly on 02/28/23. At this point in the war, Russia has started to launch more and more attacks on the Bilohorivka and Kreminna areas in the eastern Luhansk region of Ukraine. Furthermore, there was a Russian missile strike that hit a critical infrastructure in central Ukraine. Bakhmut also has been surrounded by Russian forces rushing to the front line on three sides. Russian officials also accused Ukraine of deploying attack drones over Russian territory. Russia also claimed that there was a Ukranian drone carrying explosives. In response, Russia's pro-invasion military bloggers propagated to the public that the drone attacks on Russian territory would be an indicator of more Ukranian counteroffensives to create Russian panic, despite there being no casualty. Lastly, Russia gave the US an official diplomatic note on withdrawal from the New START, a key nuclear arms reduction agreement.

## Other (housekeeping notes)

All data was downloaded into a CSV file from each corresponding website besides the Brent price from Investing.com. An API call was used for the Brent price. The data remains the same.