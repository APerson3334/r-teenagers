# Discussion Bot by u/Aperson3334
#Idea by u/Arukimedesu
#Thread ideas by u/timawesomeness
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

    post = randint(1,70) #Generates a random whole number between 1 and 70. Can be expanded for more threads.

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
		reddit.subreddit('teenagers').submit(title='Camera roll thread', selftext="Comment the number of images in your camera roll, then someone will reply with a number and you'll reply with the corresponding picture.", flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted Camera roll thread'
	else if post == 10:
		reddit.subreddit('teenagers').submit('teenagers', '2 truths and a lie thread', selftext='', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted 2 truths and a lie thread'
	else if post == 11:
		reddit.subreddit('teenagers').submit(title="What's something that a lot of people like but you don't care for?", selftext='', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's something that a lot of people like but you don't care for?"
	else if post == 12:
		reddit.subreddit('teenagers').submit(title='What was one good thing and one bad thing that happened today?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What was one good thing and one bad thing that happened today?'
	else if post == 13:
		reddit.subreddit('teenagers'),submit(title='Yay or nay thread', selftext="""Comment something and people will respond with yay or nay
		
		^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!'""", flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted Yay or nay thread'
	else if post == 14:
		reddit.subreddit('teenagers'),submit(title='What is your worst quality?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What is your worst quality?'
	else if post == 15:
		reddit.subreddit('teenagers').submit(title='Truth thread', selftext='Like truth or dare but without the dares since nobody ever chooses dare anyway', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted Truth thread'
	else if post == 16:
		reddit.subreddit('teenagers').submit(title='Sub dare thread', selftext='', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted Sub dare thread'
	else if post == 17:
		reddit.subreddit('teenagers').submit(title='Rice purity test scores', selftext='http://www.ricepuritytest.com', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted Rice purity test scores'
	else if post == 18:
		reddit.subreddit('teenagers').submit(title='Would you rather thread', selftext='', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted Would you rather thread
	else if post == 19:
		reddit.subreddit('teenagers').submit(title="What's your favorite thing you own?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite thing you own?"
	else if post == 20:
		reddit.subreddit('teenagers').submit(title='User appreciation thread', selftext="""Comment which users you appreciate

		Remember you can only mention three people per comment

		^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!""", flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
	else if post == 21:
		reddit.subreddit('teenagers').submit(title='Introduction thread', selftext="""Introduce yourself!

		^(especially if you're new or haven't used this sub frequently)

		^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!""", flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted Introduction thread'
	else if post == 22:
		reddit.subreddit('teenagers').submit(title='What is your greatest fear?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
	else if post == 23:
		reddit.subreddit('teenagers').submit(title='What was the best part of your day?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What was the best part of your day?'
	else if post == 24:
		reddit.subreddit('teenagers').submit(title='What do you think of a user thread', selftext ='Comment and people will tell you what they think about you', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted What dou you think of a user thread'
	else if post == 25:
		reddit.subreddit('teenagers').submit(title='General discussion thread', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted General discussion thread'
	else if post == 26:
		reddit.subreddit('teenagers').submit(title='Wyd hyd', selftext = '^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted Wyd hyd'
	else if post == 27:
		reddit.subreddit('teenagers').submit(title='Who is your favorite artist/band?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted Who is your favorite artist/band?'
	else if post == 28:
		reddit.subreddit('teenagers').submit(title='Why is your best friend your best friend?', selftex ='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted Why is your best friend your best friend?'
	else if post == 29:
		reddit.subreddit('teenagers').submit(title='Post your favorite image right now', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted Post your favorite image right now'
	else if post == 30:
		reddit.subreddit('teenagers').submit(title='What are you listening to?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What are you listening to?'
	else if post == 31:
		reddit.subreddit('teenagers').submit(title="What's your favorite song?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite song?"
	else if post == 32:
		reddit.subreddit('teenagers').submit(title="What's your favorite weather?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite weather?"
	else if post == 33:
		reddit.subreddit('teenagers').submit(title='What would be the best superpower to have?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What would be the best superpower to have?'
	else if post == 34:
		reddit.subreddit('teenagers').submit(title="What's your favorite subreddit?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite subreddit?"
	else if post == 35:
		reddit.subreddit('teenagers').submit(title='What temperature is it for you right now?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What temperature is it for you right now?'
	else if post == 36:
		reddit.subreddit('teenagers').submit(title='User simulator thread', selftext='+/u/User_Simulator username', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted User simulator thread'
	else if post == 37:
		reddit.subreddit('teenagers').submit(title='User stats thread', selftext='/u/user-stats username', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted User stats thread
	else if post == 38:
		reddit.subreddit('teenagers').submit(title='RES upvote thread', selftext="Comment and RES users will tell you how many times they've upvoted you", flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
		print 'submitted RES upvote thread'
	else if post == 39:
		reddit.subreddit('teenagers').submit(title='How many hours of sleep did you get last night?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted How many hours of sleep did you get last night?'
	else if post == 40:
		reddit.subreddit('teenagers').submit(title="What's your favorite soundtrack?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite soundtrack?"
	else if post == 41:
		reddit.subreddit('teenagers').submit(title="What's your favorite movie?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite movie?"
	else if post == 42:
		reddit.subreddit('teenagers').submit(title="What's your favorite movie?", '^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite movie?"
	else if post == 43:
		reddit.subreddit('teenagers').submit(title="What's your favorite TV show?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite TV show?"
	else if post == 44:
		reddit.subreddit('teenagers').submit(title='What was your favorite age of your life?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What was your favorite age of your life?'
	else if post == 45:
		reddit.subreddit('teenagers').submit(title="What's your favorite number?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite number?"
	else if post == 46:
		reddit.subreddit('teenagers').submit(title='What music artist/band do you want to see live?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What music artist/band do you want to see live?'
	else if post == 47:
		reddit.subreddit('teenagers').submit(title='What was the last thing you were angry about?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What was the last thing you were angry about?'
	else if post == 48:
		reddit.subreddit('teenagers').submit(title="What's the last dream you remember?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's the last dream you remember?"
	else if post == 49:
		reddit.subreddit('teenagers').submit(title="What's a weird thing you find attractive?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's a weird thing you find attractive?"
	else if post == 50:
		reddit.subreddit('teenagers').submit(title="What's your dream job?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your dream job?"
	else if post == 51:
		reddit.subreddit('teenagers').submit(title="When's the last time you genuinely felt happy?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted When's the last time you genuinely felt happy?"
	else if post == 52:
		reddit.subreddit('teenagers').submit(title="Would you rather know when you'll die or how you'll die?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted Would you rather know when you'll die or how you'll die?"
	else if post == 53:
		reddit.subreddit('teenagers').submit(title="What's your aesthetic?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your aesthetic?"
	else if post == 54:
		reddit.subreddit('teenagers').submit(title="What's your favorite song lyric?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite song lyric?"
	else if post == 55:
		reddit.subreddit('teenagers').submit(title="What's your first name?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your first name?"
	else if post == 56:
		reddit.subreddit('teenagers').submit(title='What, other than sleeping and school, do you spend most of your time doing?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What, other than sleeping and school, do you spend most of your time doing?'
	else if post == 57:
		reddit.subreddit('teenagers').submit(title="Do you like cheese? What's your favorite cheese?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted Do you like cheese? What's your favorite cheese?"
	else if post == 58:
		reddit.subreddit('teenagers').submit(title="What's the longest you've ever slept for?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's the longest you've ever slept for?"
	else if post == 59:
		reddit.subreddit('teenagers').submit(title="What's your favorite holiday?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite holiday?"
	else if post == 60:
		reddit.subreddit('teenagers').submit(title='Share a fun fact about yourself', selftext='', flair_id='6b01166e-6435-11e2-a77a-12313d051e91')
	else if post == 61:
		reddit.subreddit('teenagers').submit(title='Where are you from?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted Where are you from?'
	else if post == 62:
		reddit.subreddit('teenagers').submit(title="What's your favorite music genre?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite music genre?"
	else if post == 63:
		reddit.subreddit('teenagers').submit(title="What's your least favorite music genre?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite music genre?"
	else if post == 64:
		reddit.subreddit('teenagers').submit(title='What was the last compliment someone gave you?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What was the last compliment someone gave you?'
	else if post == 65:
		reddit.subreddit('teenagers').submit(title="What's your favorite food?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's your favorite food?"
	else if post == 66:
		reddit.subreddit('teenagers').submit(title='What does your bedroom look like?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What does your bedroom look like?'
	else if post == 67:
		reddit.subreddit('teenagers').submit(title="What's the oldest thing you own?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What's the oldest thing you own?"
	else if post == 68:
		reddit.subreddit('teenagers').submit(title='What song is stuck in your head right now?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted What song is stuck in your head right now?'
	else if post == 69:
		reddit.subreddit('teenagers').submit(title="What is the most illegal thing you've ever done?", selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print "submitted What is the most illegal thing you've ever done?"
	else if post == 70:
		reddit.subreddit('teenagers').submit(title='Would you pay $125 to know who has a crush on you?', selftext='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!', flair_id='1b713a20-845f-11e3-a1ce-12313d224170')
		print 'submitted Would you pay $125 to know who has a crush on you?'
	# Continue for the rest of the threads in timawesomeness' wiki
    time.sleep(3600) # Wait 3600 seconds (1 hour) before posting again