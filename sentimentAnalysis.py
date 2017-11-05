import csv
from textblob import TextBlob

alltweets = csv.reader(open("uniqueTweets.csv", 'r'))
sntTweets = csv.writer(open("sentiment-analysis-metoo.csv", "w"))

for row in alltweets:
    blob = TextBlob(row[1])
    if blob.sentiment.polarity > 0:
        sntTweets.writerow([row[0], row[1], blob.sentiment.polarity, "positive"])
    elif blob.sentiment.polarity < 0:
        sntTweets.writerow([row[0], row[1], blob.sentiment.polarity, "negative"])
    elif blob.sentiment.polarity == 0.0:
        sntTweets.writerow([row[0], row[1], blob.sentiment.polarity, "neutral"])


