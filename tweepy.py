import tweepy
import csv
import re

####input your credentials here

consumer_key = 'sbtp5EozRxvhylhFGywz8h74a'
consumer_secret = 'PPvjpBjAORBNecXWqPQzZShWNQv0cwTgXVcmPwKmlTIJ3NHW2f'
access_token = '177730701-yTDNgRiI02oEtyRtLpXS3LGCb1BklAinMC9gCdsV'
access_token_secret = 'E9dO4Zd3mpSUygMpF5kN0eGqNluLGhXwvsb643GbYQUdT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('all_no_i5_tweets.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

# NoI5RQX hashtag
for tweet in tweepy.Cursor(api.search,q="#NOI5RQX",count=100,
                           lang="en",
                           since="2019-02-01").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.entities['urls'][0]['expanded_url'], tweet.user.screen_name, tweet.text.encode('utf-8')])

# Joe cortright and ODOT
for tweet in tweepy.Cursor(api.search,q="@joe_cortright",count=100,
                           lang="en",
                           since="2019-02-01").items():
    if re.search('@OregonDOT', tweet.text):
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.entities['urls'][0]['expanded_url'], tweet.user.screen_name, tweet.text.encode('utf-8')])

# rose quarter & @OregonDOT
for tweet in tweepy.Cursor(api.search,q="rose quarter",count=100,
                           lang="en",
                           since="2019-02-01").items():
    if re.search('@OregonDOT', tweet.text):
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.entities['urls'][0]['expanded_url'], tweet.user.screen_name, tweet.text.encode('utf-8')])


# freeway expansion & @OregonDOT
for tweet in tweepy.Cursor(api.search,q="freeway expansion",count=100,
                           lang="en",
                           since="2019-02-01").items():
    if re.search('@OregonDOT', tweet.text):
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.entities['urls'][0]['expanded_url'], tweet.user.screen_name, tweet.text.encode('utf-8')])

# portland & freeway expansion
for tweet in tweepy.Cursor(api.search,q="freeway expansion",count=100,
                           lang="en",
                           since="2019-02-01").items():
    if re.search('portland', tweet.text):
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.entities['urls'][0]['expanded_url'], tweet.user.screen_name, tweet.text.encode('utf-8')])

# freeway widening & portland
for tweet in tweepy.Cursor(api.search,q="freeway widening",count=100,
                           lang="en",
                           since="2019-02-01").items():
    if re.search('portland', tweet.text):
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.entities['urls'][0]['expanded_url'], tweet.user.screen_name, tweet.text.encode('utf-8')])

# freeway ted hashtag
for tweet in tweepy.Cursor(api.search,q="#freewayted",count=100,
                           lang="en",
                           since="2019-02-01").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.entities['urls'][0]['expanded_url'], tweet.user.screen_name, tweet.text.encode('utf-8')])
