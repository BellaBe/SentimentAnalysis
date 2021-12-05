import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("tweet_data.csv")
sample = df.sample(20)
print(sample)
print("Number of tweet: {}".format(len(df)))

tweet_id = 4870
tweet = df.iloc[tweet_id]

print("Tweet: {}".format(tweet["tweet_text"]))
print("Sentiment: {}".format(tweet["sentiment"]))

# sentiment_count = df["sentiment"].value_counts()
# plt.pie(sentiment_count, labels=sentiment_count.index, auotpct="%1.1f%%", shadow=True, startangle=140)
# plt.show()

print("Number of +tweets: {}".format(df[df["sentiment"]=="positive"].count()[0]))
print("Number of -tweets: {}".format(df[df["sentiment"]=="negative"].count()[0]))

pos_tweets = df[df["sentiment"] == "positive"]
txt = " ".join(tweet.lower() for tweet in pos_tweets["tweet_text"])
wordcloud = WordCloud().generate(txt)
print(wordcloud)
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()

neg_tweets = df[df["sentiment"] == "negative"]
txt = " ".join(tweet.lower() for tweet in pos_tweets["tweet_text"])
wordcloud = WordCloud().generate(txt)
print(wordcloud)
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()