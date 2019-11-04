import tweepy
from textblob import TextBlob
import os
import csv

# setting global variables



# Step 1 - Authenticate
consumer_key= '4KWwsyBMdDvSuu2siZSXHQkGE'
consumer_secret= 'ASx2coH47U8GF0gVcgcyv1c9aibUGACo521GusLfDcZG3mpS6b'

access_token='357403667-RvTsjRYbw04PTQysGoykg0mC0lqO4fURuKBZaKbb'
access_token_secret='o2tWK2rrVmiA2PSqPkjXDbwMTGtsyxrYngvQPTwPfvfBp'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 2 - File
# Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')


#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

    csvWriter.writerow([tweet.created_at, analysis, analysis.sentiment])
    print (tweet.created_at, analysis, analysis.sentiment)

csvFile.close()

    #Save the tweets in csv
    #with open('tweets.csv', 'wb') as this_tweets_file:
         #this_tweets_file.write('analysis,analysis.sentiment\n')

            # recording the sentiment score
            #sentiment_score.insert(0, analysis.sentiment.polarity)
            # opening csv file to write the input along with tag and score
    #with open("tweet_sheet.csv", "a") as sheet:
         #W = csv.writer(sheet, delimiter=',')
         #W.writerow([tweet.text,analysis.sentiment])
