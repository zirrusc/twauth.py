# coding: utf-8

import tweepy
import os.path
import sys
from twauth import twauth

class twauth_sample:

	tokenPath = os.getcwd() + '/sample-token'
	consumerKey = 'CONSUMER KEY HERE'
	consumerSecret = 'CONSUMER SECRET HERE'

	api = None

	def auth(self):
		try:
			if os.path.isfile(self.tokenPath) == False:
				# Get and storage Access Key and Access Secret of Twitter API.
				rget = twauth.get(self.consumerKey, self.consumerSecret, self.tokenPath)
				if rget != 0: 
					# Cancelled by user
					return rget
	
			# Read access token file and authenticate this application.
			auth = twauth.auth(self.tokenPath)
			# Initialize api
			self.api = tweepy.API(auth_handler=auth)
			return 0
		except:
			print 'An error occured when authenticating the application.'
			raise
	
	def post(self, text):
		self.api.update_status(text)
	
	def timeline(self):
		for item in self.api.home_timeline():
			print item.text
		
if '__main__' in __name__:
	print 'twauth.py sample'
	print 'initializing...'
	sample = twauth_sample()
	if sample.auth() != 0:
		sys.exit(1)
	print 'post()'
	sample.post('twauth.py sample')
	print 'timeline()'
	sample.timeline()
	
