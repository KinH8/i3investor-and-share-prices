# i3investor-and-share-prices
We look into whether sentiment analysis of popular (Malaysian) stock market online forum i3investor is predictive of share prices.

We start by scrapping internet posts from popular Malaysian stock market online forum i3investor (link: https://klse.i3investor.com/web/index) for select stocks. A sample csv file of a randomly chosen stock is included, as the file size of a full compilation for even a single stock can run into 10+ MB. Note that you would need Scrapy to run the code.

![image](https://user-images.githubusercontent.com/105033135/185580858-8ef848d0-1ad0-4182-a24f-f50ea9701802.png)

Next we generate the sentiment score of each posts using the Loughran-McDonald dictionary. You can find more from its official site https://sraf.nd.edu/textual_analysis/code/; you can download a Python generic parser from the site. 

![image](https://user-images.githubusercontent.com/105033135/185584117-4c4a981b-c087-43bd-8332-ee22d7627ef1.png)

Our chosen stock here, glove manufacturer Top Glove, used to be a darling of retail investors during the 2020-2021 period before share price moderated along with ebbing Covid-19 cases. Figure below compares the net sentiment score vs. share price. The sentiment score does not seem predictive of share price. 

![image](https://user-images.githubusercontent.com/105033135/186604334-c3de38d1-2f02-49e9-aa5b-bf5c8f35b335.png)

Our small study suffers from 2 pitfalls. First, the LM dictionary may not fully capture the sentiment of the colloquial English used by everyday Malaysian. Second, the study should be expanded to more stocks.
