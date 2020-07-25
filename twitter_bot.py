# Twitter Bot created by Alakesh Bora. Email: alokesh985@gmail.com

import tweepy
import time

# Connecting to Twitter API and authenticating
authorization = tweepy.OAuthHandler("s7OF7PAZJ2PwExWE1mX9Ea76X", "rBmjdGuvnE9zo2S6ayi2R8T6tKcR8cqSVQjmSWVI7wwA1jrt52")
authorization.set_access_token('1287031918274310149-MFffuN2gCevoy55jGT7JaQd87oA6Ll', 'PlAjfWA1ZOm46bHN3xW41pvesa8dvsXV46T54iqVXgGhd')

# Using Twitter API to get access. Putting the limits so Twitter doesn't ban the bot
api = tweepy.API(authorization, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

print("Connected!")

choice = int(input("Press 0 to like tweets according to some term.\nPress 1 to like tweets according to someone's username\n(0/1): "))

# For Liking Tweets according to some hashtag or any term
if choice == 0:
    # NOTE: For example, to like a hashtag called XYZ, write #XYZ
    term = input("Enter Term You want to like: ")
    number = int(input("Enter Number of Tweets to like: "))

    for tweet in tweepy.Cursor(api.search, term).items(number):
        try:
            tweet.favorite()
            print(f"Tweet by {tweet.author.name} Liked!")
            # Sleeping 3 seconds before every like to prevent banning of account
            time.sleep(3)

        except tweepy.TweepError as error:
            print(error.reason)

# For liking Tweets according to a person's username
else:
    user_name = input("Enter User Name of the Person whose Tweet you want to like: ")
    number = int(input("Enter Number of Tweets you want to like: "))

    for tweet in tweepy.Cursor(api.user_timeline, user_name).items(number):
        try:
            tweet.favorite()
            print(f"Tweet by {tweet.author.name} Liked!")
            # Sleeping every 3 seconds to prevent ban
            time.sleep(3)

        except tweepy.TweepError as error:
            print(error.reason)

print("\n\nThanks for using my bot!\nCreated by Alakesh Bora\nPh No: +917002608973\nEmail: alokesh985@gmail.com")