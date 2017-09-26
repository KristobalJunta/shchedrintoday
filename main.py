import tweepy
from config import config

auth = tweepy.OAuthHandler(config.get('consumer_key'), config.get('consumer_secret'))
auth.set_access_token(config.get('access_token'), config.get('access_token_secret'))

api = tweepy.API(auth)

# print(api.me().name)

status_text = "Пьют и воруют."
api.update_status(status=status_text)
