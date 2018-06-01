import praw # Python Reddit API Wrapper
import random # Allows random number to be generated
import time # Contains sleep function - prevents bot spam

# Sign in function
reddit = praw.Reddit(client_id='CLIENT_ID',
					client_secret=’CLIENT_SECRET’, password='PASSWORD',
					user_agent='USERAGENT', username='USERNAME')

print 'logged in bois'

while 1 == 1: #Makes the bot work constantly

	reddit.subreddit('teenagers').submit(title="real sad boi hours", selftext='who's up?', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
	print "submitted What's your unpopular opinion?"
	time.sleep(86400)