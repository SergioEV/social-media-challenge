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

handle = input("Input Twitter Handle: ")
keywrd = input("Please enter a search term: ")
user = api.get_user(handle)

count = 0
for status in tweepy.Cursor(api.user_timeline, id = handle).items(100):
	if "RT" in status.text:
		continue

	#Use below to print to text file
	#with open("Output.txt", "a") as text_file:
		#print("{}\n".format(str.lower(status.text)), file=text_file)	

	if keywrd in str.lower(status.text):
		count+=1

print("\nName: {}".format(user.name))
print("Description: {}".format(user.description))
print("Followers: {}".format(user.followers_count))
print("Friends: {}".format(user.friends_count))
print("# of hits for {}: {}".format(keywrd,count))
	


	
