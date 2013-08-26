# coding: utf-8

import tweepy
import os
import sys

# Get Access Key and Access Secret of Twitter API using tweepy, and write them at ordered file.
class twauth:

	defaultPath = 'access-token'
	
	# Show this help message.
	@classmethod
	def help(self):
		try:
			for line in open(os.getcwd() + '/help.txt', 'r'):
				print line,
		except:
			print 'Error: Cannot open help.txt.'
		return 2

	# Authenticate the application.
	@classmethod
	def auth(self, path = ''):
		if path == '':
			path = 'access-token'
		if os.file.exists(path):
			f = open(path, 'r')
			r = { 'consumer-key': f[0], 'consumer-secret': f[1], 'access-key': f[2], 'access-secret': f[3] }
			f.close()
		
			auth = tweepy.OAuthHandler(r['consumer-key'], r['consumer-secret'])
			auth.set_access_token(r['access-key'], r['access-secret'])
			return auth
		else:
			print '\'%s\': file not found.' % path
		
	# Get and storage Access Key and Access Secret of Twitter API.
	@classmethod
	def get(self, consumerKey = '', consumerSecret = '', savePath = ''):
		if (consumerKey == ''):
			conKey = raw_input('consumer key: ')
		else:
			conKey = consumerKey
		if (consumerSecret == ''):
			conSecret = raw_input('consumer secret: ')
		else:
			conSecret = consumerSecret
		
		auth = tweepy.OAuthHandler(conKey, conSecret)
		authUrl = auth.get_authorization_url()

		print 'go to: ' + authUrl
		pin = raw_input('pin: ').strip()

		auth.get_access_token(pin)
		accessKey = auth.access_token.key
		accessSecret = auth.access_token.secret

		print 'access key: %s' % accessKey
		print 'access secret: %s' % accessSecret

		path = self.detectPath(savePath)
		if path == '':
			return 1
	
		# Open file
		f = open(path, 'w')
		f.write(conKey + '\n')
		f.write(conSecret + '\n')
		f.write(accessKey + '\n')
		f.write(accessSecret + '\n')
		f.close()
		return 0
	
	@classmethod
	def detectPath(self, savePath):
		if (savePath == ''):
			path = raw_input('save to [%s](\'c\' to cancel): ' % self.defaultPath)
		else:
			path = savePath
	
		if path == '':
			path = self.defaultPath
		if path == 'c':
			return 1
		if os.path.exists(path):
			r = ''
			while True:
				r = raw_input('%s has been exists. overwritten? (Y[es]/n[o]): ' % path)
				isow = r.lower()
				if isow == 'n' or isow == 'no':
					return ''
				if isow == 'y' or isow == 'yes' or isow == '':
					return path
		return path

if '__main__' in __name__:
	arguments_missing = '\
Arguments missing\n\
Type \'python twauth.py help\' for more infomation.'

	v = sys.argv
	c = len(v)
	if c == 1:
		twauth.get()
	if c == 2:
		if v[1] == 'help':
			twauth.help()
		else:
			print(arguments_missing)
	if c == 3:
		twauth.get(v[1], v[2])
	if c == 4:
		twauth.get(v[1], v[2], v[3])
	if c >= 5:
		print(arguments_missing)
	
	
