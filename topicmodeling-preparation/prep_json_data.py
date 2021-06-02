#!/usr/bin/env python3
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import json
import nltk
import re
import emoji
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')
words = set(nltk.corpus.words.words())
# Create set of stop words
manual_set = {"amp", "u", "nt"git , "s", "get", "nt", "s"}
stop = set(stopwords.words('english')).union(manual_set)
# Create a set of punctuation words 
punctuation = set(string.punctuation) 

def cleaner(tweet):
    tweet = tweet.lower()
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
    # tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet) \
    #      if w.lower() in words or not w.isalpha())
    tweet = word_tokenize(tweet)
    tweet = " ".join([i for i in tweet if i not in stop])
    tweet = "".join([i for i in tweet if i not in punctuation])
    tweet = "".join(c for c in tweet if c not in emoji.UNICODE_EMOJI) #Remove Emojis
    return tweet

if __name__ == "__main__":
    f = open('geotagged_tweets_20160812-0912.jsons', "r")
    content = f.read()
    content_list = content.splitlines()    
    f.close()
    
    json_list = [json.loads(line) for line in content_list]
    simple_dict = {}
    count = 0

    for entry in json_list:
        if entry["lang"] == "en" and count < 50000:
            simple_dict[entry["id"]] = cleaner(entry["text"])
            # simple_dict[entry["id"]] = entry["text"]
            count += 1
            

    with open('data_50k.json', 'w', encoding='utf-8') as f:
        json.dump(simple_dict, f, ensure_ascii=False, indent=4)
