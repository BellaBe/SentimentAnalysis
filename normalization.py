import re
import emoji

tweet = "RT @AIOutsider I love this! 👍 https://AIOutsider.com #NLP #Fun"

def replace_retweet(tweet, default_replace=""):
    tweet = re.sub("RT\s+",default_replace, tweet)
    return tweet


print("Processed tweet: {}".format(replace_retweet(tweet)))

def replace_user(tweet, default_replace="twitteruser"):
    tweet = re.sub("\B@\w+", default_replace, tweet)
    return tweet

print("Processed tweet: {}".format(replace_user(tweet)))

def demojize(tweet):
    tweet = emoji.demojize(tweet)
    return tweet

print("Processed tweet: {}".format(demojize(tweet)))

def replace_url(tweet, default_replace=""):
    tweet = re.sub("(http|https):\/\/\S+", default_replace, tweet)
    return tweet

print("Processed tweet: {}".format(replace_url(tweet)))

def replace_hashtag(tweet, default_replace=""):
    tweet = re.sub("#+", default_replace, tweet)
    return tweet

print("Processed tweet: {}".format(replace_hashtag(tweet)))

tweet2 = "LOOOOOOOOK at this ... I'd like it so much!"

def to_lowercase(tweet):
    tweet = tweet.lower()
    return tweet

print("Processed tweet: {}".format(to_lowercase(tweet2)))

def word_repetition(tweet):
    tweet = re.sub(r"(.)\1+", r"\1\1", tweet)
    return tweet

print("Processed tweet: {}".format(word_repetition(tweet2)))

def punct_repetition(tweet, default_replace = ""):
   tweet = re.sub(r"[\?\.\!]+(?=[\?\.\!])", default_replace, tweet)
   return tweet
print("Processed tweet: {}".format(punct_repetition(tweet2)))


