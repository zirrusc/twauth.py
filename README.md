twauth.py
----
[zirrusc](http://zirrusc.net) 2013


Get Access Key and Access Secret of Twitter API using Tweepy, and write them at ordered file. You don't need authenticate over again.

#Requirement
* Python 2.7 (Python 3 family is not supported because of Tweepy requirement)
* [Tweepy 2.0](https://github.com/tweepy/tweepy)
* Twitter account
* Twitter application (Register at [dev.twitter.com](http://dev.twitter.com) )
* Encryption is not supported.

#Using
		python twauth.py help
	Show this help message.
	
		python twauth.py [consumer-key consumer-secret [path]]
	Get and save as path Access Key and Access Secret of Twitter API.
	consumer-key: A Consumer Key authenticating the application.
	consumer-secret: A consumer secret authenticating the application.
	path: A file name writing access token.
		   
#Functions
* def auth(path = '')
	Authenticate the application from storaged access token.
	path: A file name storaged access token.
	
* def get(consumerKey = '', consumerSecret = '', savePath = '')
	Get and storage Access Key and Access Secret of Twitter API.
	consumerKey: A Consumer Key authenticating the application.
	consumerSecret: A consumer secret authenticating the application.
	savePath: A file name writing access token.



twauth.python
---
Tweepy を使用して、Twitter API のアクセスキーとアクセスシークレットを取得して、指定したファイルに書き込みます。何度も認証する必要がなくなります。

#要件
* Python 2.7 (Python 3 ファミリはTweepyによりサポートされません)
* [Tweepy 2.0](https://github.com/tweepy/tweepy)
* Twitter アカウント
* Twitter アプリケーション( [dev.twitter.com](http://dev.twitter.com) で登録)

#使用方法
		python twauth.py help
	このヘルプを表示する.
	
		python twauth.py [consumer-key consumer-secret [path]]
	Twitter API のアクセスキーとアクセスシークレットを取得し、 path に保存します。
	consumer-key: A Consumer Key authenticating the application.
	consumer-secret: A consumer secret authenticating the application.
	path: A file name writing access token.
		   
#関数
* def auth(path = '')
	Authenticate the application from storaged access token.
	path: A file name storaged access token.
	
* def get(consumerKey = '', consumerSecret = '', savePath = '')
	Get and storage Access Key and Access Secret of Twitter API.
	consumerKey: A Consumer Key authenticating the application.
	consumerSecret: A consumer secret authenticating the application.
	savePath: A file name writing access token.
	
	
