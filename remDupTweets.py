'''
removing duplicate tweets from gathered
'''

import csv

alltweets = csv.reader(open("metoo.csv", 'r'))

noDup = csv.writer(open("uniqueTweets.csv", "w")) # store unique tweets

tweets = set()
i = 0;
for row in alltweets:
    i = i + 1
    # print(row[1])
    # print i
    if row[1] not in tweets:
        t = row[1].lower()
        t = t.replace('\n', '')
        noDup.writerow([row[0], row[1], t])
        # print "writing row.."
        tweets.add( row[1] )