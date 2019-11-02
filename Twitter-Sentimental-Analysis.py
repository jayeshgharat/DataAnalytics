import tweepy
from textblob import TextBlob
import os

# setting global variables



# Step 1 - Authenticate
consumer_key= '4KWwsyBMdDvSuu2siZSXHQkGE'
consumer_secret= 'ASx2coH47U8GF0gVcgcyv1c9aibUGACo521GusLfDcZG3mpS6b'

access_token='357403667-RvTsjRYbw04PTQysGoykg0mC0lqO4fURuKBZaKbb'
access_token_secret='o2tWK2rrVmiA2PSqPkjXDbwMTGtsyxrYngvQPTwPfvfBp'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

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


 #Save the tweets in csv
	#with open('%s_tweets.csv' % tweets, 'wb') as this_tweets_file:
		#this_tweets_file.write('tweet,sentiment_label\n')

		    
            # recording the sentiment score
            #sentiment_score.insert(0, analysis.sentiment.polarity)
            # opening csv file to write the input along with tag and score
            with open("tweet_sheet.csv", "a") as sheet:
                W = csv.writer(sheet, delimiter=',')
                W.writerow([tweet.text,analysis.sentiment])
