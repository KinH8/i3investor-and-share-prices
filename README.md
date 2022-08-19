# i3investor-and-share-prices
We look into whether sentiment analysis of popular (Malaysian) stock market online forum i3investor is predictive of share prices.

We start by scrapping internet posts from popular Malaysian stock market online forum i3investor (link: https://klse.i3investor.com/web/index) for select stocks. A sample csv file of a randomly chosen stock is included, as the file size of a full compilation for even a single stock can run into 10+ MB. Note that you would need Scrapy to run the code.

![image](https://user-images.githubusercontent.com/105033135/185580858-8ef848d0-1ad0-4182-a24f-f50ea9701802.png)

Next we generate the sentiment score of each posts using the Loughran-McDonald dictionary. You can find more from its official site https://sraf.nd.edu/textual_analysis/code/; you can download a Python generic parser from the site. Our chosen stock here, glove manufacturer Top Glove, used to be a darling of retail investors during the 2020-2021 period before share price moderated along with ebbing Covid-19 cases. Figure below compares the sentiment score vs. share price. The sentiment score does not seem predictive of share price. 

![Pos sentiment](https://user-images.githubusercontent.com/105033135/185582113-d1840f9c-e3bd-4897-b924-7395c4f031cb.png)

![Neg sentiment](https://user-images.githubusercontent.com/105033135/185582199-a57d2d69-aa06-4f8d-b938-04428ca8dd8a.png)

Our small study suffers from 2 pitfalls. First, the LM dictionary may not fully capture the sentiment of the colloquial English used by everyday Malaysian. Second, the study should be expanded to more stocks.
