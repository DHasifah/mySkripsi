import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import Cursor
import string

class Crawling:
	CONSUMER_TOKEN	= 'EZ9ISOuWJSVPwENZ9K4nNPhXU'
	CONSUMER_SECRET = '5a3DV0Wd1Xw797Xdq7lDzCrKUHHPV1shkEtJ2TK8ZmkNvc6t1H'
	ACCESS_TOKEN	= '513971143-c1EdUt7ClJ0x5OsjKSnQ5XBMtH9eGWwGQHK3SSOZ'
	ACCESS_SECRET	= '9yeguf59StCjteXIG4SOuHuyZY94cYCJjhXKvgDlQPInZ' 

	def __init__(self):
		self.auth = tweepy.OAuthHandler(self.CONSUMER_TOKEN, self.CONSUMER_SECRET)
		self.api = tweepy.API(self.auth)

	def run(self, query, lang, limit):
		return tweepy.Cursor(self.api.search, q=query, lang=lang).items(limit)
