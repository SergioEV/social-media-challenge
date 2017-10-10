#!/usr/bin/python3

import tweepy
import os

## 15 CALLS EVERY 15 MINUTES. Running program too many times will give status code 429


# sets up auth and access keys
consumer_key = '858dJ9NBYSMgu2u7Onu6LBcbG'
consumer_secret = '66SlUxKVsqs3jovP8WStPeQ3w24TbRHa7vpjDIYI03jvHobCKs'

access_token_key = '916395702380408832-M38tYdjxdH0MiaolfupWL3juxFvKKAd'
access_token_secret = 'ms1fFRT1Ro41KsVjOKs0d9dbrYYBmVxFyfD3Z1qZG5oey'

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth1)




def searchUser():
	os.system('clear')
	user = input("Input user name to search: ")

	for names in api.search_users(q = user, perpage = 0):
		print("> {}".format(names.screen_name))

	input("\n---Press Enter to Continue---")

def listTrending():
	woeid = input("Insert WOEID, or 1 for global information: ")

	print("{}".format(api.trends_place(woeid)))

	input("\n---Press Enter to Continue---")



def listTweetsMatching():
	os.system('clear')
	#Setup file
	open('Output.txt', 'w').close()

	count  = 0
	handle = input("Input Twitter handle: ")
	keywrd = input("Input keyword: ")

	#Going over 3200 items may cause temporary blacklist from twitter
	for status in tweepy.Cursor(api.user_timeline, id = handle).items(100):

		#remove retweets
		if "RT" in status.text:
			continue

		#destructively edits tweet string, deletes garbage characters
		status.text = status.text.translate(str.maketrans('','', '.-?,!()"{}[]:#'  ))


		# If we encounter word, increase count by one, write edited tweet to text file.
		if keywrd in str.lower(status.text):
			count += 1
			with open("Output.txt", "a") as text_file:
		 		print("{}-- {}\n".format(status.created_at,str.lower(status.text)), file=text_file)

	if count > 0:
		print("\n{} hits found. Tweets written to Output.txt".format(count))
	else:
		print("\nNo hits found")

	input("\n---Press Enter to Continue---")		


def listRecentTweets():
	os.system('clear')

	handle = input("Input Twitter Handle: ")
	
	for status in tweepy.Cursor(api.user_timeline, id = handle).items(25):
		print("\n> {}".format(status.text))


	input("\n---Press Enter to Continue---")



def listUserInfo():
	os.system('clear')

	handle = input("Input Twitter handle: ")
	user = api.get_user(handle)

	print("\nName: {}".format(user.name))
	print("Description: '{}'".format(user.description))
	print("Language: {}".format(user.lang))
	print("Location: {}".format(user.location))
	print("Followers: {}".format(user.followers_count))
	print("Friends: {}".format(user.friends_count))
	print("URL: {}".format(user.url))
	print("Created: {}".format(user.created_at))

	input("\n---Press Enter to Continue---")


options = {'0' : searchUser,
				'1' : listUserInfo,
				'2' : listTweetsMatching,
				'3' : listRecentTweets,
				'4' : listTrending

}


while True:
	print("\n{}\n{}\n{}\n{}\n{}\n{}\n".format("0: Search for a user", 
		"1: List user info",
		"2: Retrieve tweets from a user that matches keyword", 
		"3: List users most recent tweets",
		"4: List top 10 trending topics by location",
		"5: Quit"))

	num = input("Enter a selection: ")

	if num == '5':
		exit()
	elif num > '5':
		continue	

	options[num]()



