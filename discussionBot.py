# Discussion Bot by u/Aperson3334
# todo: finish adding threads from timawesomeness' wiki, add number to list to avoid repeat posts but find a way to clear it occasionally

import praw # Python Reddit API Wrapper
import random # Allows random number to be generated
import time # Contains sleep function - prevents bot spam

# Sign in function
reddit = praw.Reddit(client_id='CLIENT_ID',
                     client_secret=’CLIENT_SECRET’, password='PASSWORD',
                     user_agent='USERAGENT', username='USERNAME')

print ‘logged in bois’

while 1 == 1: #Makes the bot work constantly

    post = randint(1,18) #Generates a random whole number between 1 and 18. Can be expanded for more threads.

    if post == 1:
        reddit.subreddit('teenagers').submit(title="What's your unpopular opinion?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your unpopular opinion?"
    else if post == 2:
        reddit.subreddit('teenagers').submit(title='Controversial opinion thread', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted Controversial opinion thread'
    else if post == 3:
        reddit.subreddit('teenagers').submit(title='Guys ask girls, girls ask guys' selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted Guts ask girls, girls ask guys' 
    else if post == 4:
        reddit.subreddit('teenagers'.submit(title='Selfie thread', selftext='', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted Selfie thread'
    else if post == 5:
        reddit.subreddit('teenagers').submit(title='Selfie thread but you have to take a new selfie for it', selftext='', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted Selfie thread but you have to take a new selfie for it'
    else if post == 6:
        reddit.subreddit('teenagers').submit(title='User recognition thread', selftext='Comment and people will tell you how well they recognize you on a scale of 1-10.', flair_id='1b713a20-845f-11e3-a1ce-12313d2241706b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted User recognition thread'
    else if post == 7:
        reddit.subreddit('teenagers').submit(title='Truth or dare thread' selftext='', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted Truth or dare thread'
    else if post == 8:
       	   reddit.subreddit('teenagers').submit(title='How tall are you?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		   print 'submitted How tall are you?'
	else if post == 9:
		reddit.subreddit('teenagers').submit(title='How much do you weigh?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted How much do you weigh?'
	else if post == 10:
		reddit.subreddit('teenagers').submit(title='Camera roll thread', selftext="Comment the number of images in your camera roll, then someone will reply with a number and you'll reply with the corresponding picture.", flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted Camera roll thread'
	else if post == 11:
		reddit.subreddit('teenagers').submit('teenagers', '2 truths and a lie thread', selftext='', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted 2 truths and a lie thread'
	else if post == 12:
		reddit.subreddit('teenagers').submit(title="What's something that a lot of people like but you don't care for?", selftext='', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's something that a lot of people like but you don't care for?"
	else if post == 13:
		r.subreddit('teenagers').submit(title='What was one good thing and one bad thing that happened today?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What was one good thing and one bad thing that happened today?'
	else if post == 14:
		r.subreddit('teenagers'),submit(title='Yay or nay thread', selftext="""Comment something and people will respond with yay or nay
		
		^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!'""", flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted Yay or nay thread'
	else if post == 15:
		r.subreddit('teenagers'),submit(title='What is your worst quality?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What is your worst quality?'
	else if post == 16:
		r.subreddit('teenagers').submit(title='Truth thread', selftext='Like truth or dare but without the dares since nobody ever chooses dare anyway', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted Truth thread'
	else if post == 17:
		r.subreddit('teenagers').submit(title='Sub dare thread', selftext='', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted Sub dare thread'
	else if post == 18:
		r.subreddit('teenagers').submit(title='Rice purity test scores', selftext="""http://www.ricepuritytest.com

		^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!""", flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
    # Continue for the rest of the threads in timawesomeness' wiki
    time.sleep(900) # Wait 900 seconds (15 minutes) before posting again