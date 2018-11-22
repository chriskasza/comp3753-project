import logging
import json
import pprint
from elasticsearch import Elasticsearch
from textblob import TextBlob
from twython import TwythonStreamer

logging.basicConfig(filename='sentiment_all_tweet_keys.log',level=logging.WARNING)

es = Elasticsearch()
es.indices.create(index='tweets-allkeys', ignore=400, body={'settings': {'index.mapping.total_fields.limit': 2000}})

# Create a class that inherits TwythonStreamer
class MyStreamer(TwythonStreamer):

    # Received data
    def on_success(self, data):

        # pass tweet into TextBlob
        tweet = TextBlob(data["text"])
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(tweet)
        #data['sentiment'] = tweet

        # output sentiment polarity
        #print(tweet.sentiment.polarity)

        # determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            data['sentiment'] = "negative"
        elif tweet.sentiment.polarity == 0:
            data['sentiment'] = "neutral"
        else:
            data['sentiment'] = "positive"

        data['polarity'] = tweet.sentiment.polarity
        data['subjectivity'] = tweet.sentiment.subjectivity

        # output sentiment
        #print(sentiment)

        try:
            # add text and sentiment info to elasticsearch
            es.index(index="tweets-allkeys",
                     doc_type="tweet",
                     body=data)
        except Exception as e:
            logging.warning('\nException: ' + str(e) + '\n' + str(data))

        return True

    # Problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)


with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)
    
stream = MyStreamer(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],
                    creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

# Start the stream
stream.statuses.filter(track=['midterms', '2018midterms', 'midtermelections'])    
