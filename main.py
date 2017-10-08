#!/usr/bin/python3

import tweepy

## 15 CALLS EVERY 15 MINUTES. Running program too many times will give status code 429


# sets up auth and access keys
consumer_key = '858dJ9NBYSMgu2u7Onu6LBcbG'
consumer_secret = '66SlUxKVsqs3jovP8WStPeQ3w24TbRHa7vpjDIYI03jvHobCKs'

access_token_key = '916395702380408832-M38tYdjxdH0MiaolfupWL3juxFvKKAd'
access_token_secret = 'ms1fFRT1Ro41KsVjOKs0d9dbrYYBmVxFyfD3Z1qZG5oey'

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token_key, access_token_secret)


api = tweepy.API(auth1)

#Clear file
open('Output.txt', 'w').close()

handle = input("Input Twitter Handle: ")
keywrd = input("Enter A Search Term: ")
#add spaces around string, prevents false-positives
keywrd = " " + keywrd + " "
user = api.get_user(handle)

count = 0

#Going over 3200 items may cause temporary blacklist from twitter
for status in tweepy.Cursor(api.user_timeline, id = handle).items(3200):

	tweet = status.text

	#remove retweets
	if "RT" in tweet:
		continue

	#destructively edits tweet string, deletes garbage characters
	tweet = tweet.translate(str.maketrans('','', '.-?,!()"{}[]:'  ))

	# If we encounter word, increase count by one, write edited tweet to text file.
	if keywrd in str.lower(tweet):
		count += 1
		with open("Output.txt", "a") as text_file:
		 print("{}\n".format(str.lower(tweet)), file=text_file)


print("\nName: {}".format(user.name))
print("Description: {}".format(user.description))
print("Followers: {}".format(user.followers_count))
print("Friends: {}".format(user.friends_count))
print("# of hits for '{}': {}".format(keywrd,count))