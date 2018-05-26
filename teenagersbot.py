import praw
import pdb
import re
import os
import time

reddit=praw.Reddit('bot1')
print "Logged in bois"

time.sleep(1) # Cleans up the output

while 1+1==2:

#Create and maintain a file to store posts already replied to, ensuring the bot doesn't double-reply
	if not os.path.isfile("posts_replied_to.txt"):
		posts_replied_to=[]

	else:
		with open("posts_replied_to.txt", "r") as f:
			posts_replied_to = f.read()
			posts_replied_to = posts_replied_to.split("\n")
			posts_replied_to = list(filter(None, posts_replied_to))

#The actual commenting function
			
	subreddit = reddit.subreddit('teenagers')
	for submission in subreddit.new(limit=5):
		if submission.id not in posts_replied_to:
			if re.search("selfie.+thread", submission.title, re.IGNORECASE): # Thanks timawesomeness
				submission.reply("[Comment made by SelfieBot.](http://imgur.com/a/kFy98)")
				print("Bot replying to : ", submission.title)
				posts_replied_to.append(submission.id)
	
#Going back to the .txt file
	
	with open("posts_replied_to.txt", "w") as f:
		for post_id in posts_replied_to:
			f.write(post_id + "\n")
			time.sleep(2)