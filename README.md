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

## Sources

Investing.com includes data from all over the world (countries including the US, India, Spain, Russia, and many others). From their website, they "receive data from various sources, which include the biggest financial data providers as well as real-time market maker CFDs." It ranks similar to Fidelity and Yahoo Finance in reliability, being among the top three financial sites worldwide (ranked by SimilarWeb). Statista sources its oil data from Thomson Reuters. Reuters is regarded highly by those looking to source real-time trusted data and services. Bloomberg sources its data from several data centers throughout the world, obtaining feeds from exchanges and securities information processors. This historical data was obtained through the Bloomberg Terminal. Similar to Reuters, Bloomberg is trusted by many, with most large financial firms having subscriptions to Bloomberg Professional Services. While all three sources are trustworthy, there may be discrepancies that occur when collecting data which may explain the different Urals discounts for each source in the three_series.py plot. Thus, an average plot of all three sources should give a holistic view of the large oil data trends since 2022.

UPDATE: added fourth source from treasury.gov, added fifth source from datastream

## Data Transformations

There were a few transformations made to each of the data sources. When collecting data from Bloomberg and Investing.com, the value returned for each date was the last price of the commodity on that day (for both Brent and Urals). The discount was calculated manually in some cases (Urals price minus Brent price). If the last price was plotted, there would be lots of shifts and volatility, and thus these graphs opted to use a last five days rolling average; this change was made to accommodate the data from Statista. The Statista data was already using a last five days rolling average, and thus to match all three sources to compare and take the average of all three, all three source data use a last five days rolling average.

Furthermore, some data sources had incomplete dates. For example, Bloomberg may have reported data on date A while Investing.com did not have date A. Thus, to make sure that all three data sources had the same dates, the code filters through all the dates and only kept the matching dates and their corresponding prices. This same idea was implemented in finding the averages for the three periods in period_averages.py. If the start date was not in the reported dates for a data source, we started at the next available date after the start date. Mirroring this for the end date, if the end date was not in the reported dates for a data source, we ended at the last available date before the end date.

UPDATE: added fourth source from treasury.gov, added fifth source from datastream -- did same transformations

## Graphs

** with extended dates as far as possible **


** with only matching dates **
![alt text](https://github.com/lawrencetang20/oilresearch/blob/main/saved_pngs/series_matching.png)

![alt text](https://github.com/lawrencetang20/oilresearch/blob/main/saved_pngs/average_matching.png)

## News Analysis Summary

The next step was to see if there were any explanations for the large up spikes in the Urals discount (as seen in the average.py plots), particularly in August of 2022 and February of 2023.

After parsing through the data, it showed that the jump in Urals discount in August started mainly on 08/18/22. At this point in Russia, there were a couple of developments in the war. Russia replaced the commander of the Black Sea Fleet (the fleet of the Russian Navy) with Vice Admiral Viktor N. Sokolov. Russian villages Timonova and Soloti nineteen miles from the Ukranian border were also evacuated. Furthermore, a trilateral meeting happened in Lviv with the Turkish president, UN secretary-general, and Ukrainian president to discuss the war. Lastly, Wagner, a private military company came into play as well. Russian troops were reported to be struggling in Ukraine, and thus Wagner mercenaries started to enter the spotlight. The Wagner owner was awarded the Hero of Russia, Russia's highest merit. The heroic exploits of the company flowed throughout Russian official media. Overall, there was unexpected resilience in Russian oil output, as Russia pumped less oil on the eve of the impending invasion.

Now, for more on the the causes for the oil shift for August. Originally, Novak had stated that Russia would voluntarily reduce its oil supply in August on July 3rd, planning to cut oil exports by 500,000 barrels per day. However, Moscow did not really fulfill its pledge to cut exports in August, having higher crude oil loadings compared to July. Also, Russia had the highest oil export duty in August in the year 2022. Hungary’s main oil conglomerate said on August 10th that it would pay an outstanding bill that Russia’s oil pipeline operator owed to Ukrainian authorities, meaning Russian oil deliveries would resume to three Central European countries (Hungary, Slovakia, Czech Republic). They had been stopped for a week. The war in Ukraine was a major variable in the oil supply outlook: since the invasion, daily exports have declined by 580,000 barrels, and are declining even more recently as the war has been picking up. Russia is also tightening the grip on natural gas sales to Europe, thus making them more reliant on oil.

The jump in the Urals discount in February started slowly on 02/28/23. At this point in the war, Russia has started to launch more and more attacks on the Bilohorivka and Kreminna areas in the eastern Luhansk region of Ukraine. Furthermore, there was a Russian missile strike that hit a critical infrastructure in central Ukraine. Bakhmut also has been surrounded by Russian forces rushing to the front line on three sides. Russian officials also accused Ukraine of deploying attack drones over Russian territory. Russia also claimed that there was a Ukranian drone carrying explosives. In response, Russia's pro-invasion military bloggers propagated to the public that the drone attacks on Russian territory would be an indicator of more Ukranian counteroffensives to create Russian panic, despite there being no casualty. Lastly, Russia gave the US an official diplomatic note on withdrawal from the New START, a key nuclear arms reduction agreement.

Now, for more on the the causes for the oil shift for February. Russia originally announced on February 10th that they would cut production in March, as a first response to a wave of recently imposed sanctions. Russia has blunted the impact of western measures by redirecting exports to China, India, and Turkey. Exports to India have grown 16x since the start of the war and is increasing more recently (as in Feb 10th). As China is the biggest crude importer in the world and India is the second biggest oil importer in Asia, there is a rising flow of Russian oil products to those countries. Russia also halted crude oil to Poland and started to ump oil to Germany on the 27th.

## Other (housekeeping notes)

All data was downloaded into a CSV file from each corresponding website/source besides the Brent price from Investing.com. An API call was used for the Brent price. The data remains the same.

UPDATE: added fourth source treasury.gov
