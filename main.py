import tweepy
from config import config
from datetime import datetime

auth = tweepy.OAuthHandler(config.get('consumer_key'), config.get('consumer_secret'))
auth.set_access_token(config.get('access_token'), config.get('access_token_secret'))

api = tweepy.API(auth)

# print(api.me().name)

status_text = "{}.\nПьют и воруют.".format(datetime.now().strftime('%d-%m-%Y'))
api.update_status(status=status_text)
