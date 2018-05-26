# Discussion Bot by u/Aperson3334
# todo: make bot flair posts, finish adding threads from timawesomeness' wiki, add number to list to avoid repeat posts but find a way to clear it occasionally

import praw # Python Reddit API Wrapper
import random # Allows random number to be generated
import time # Contains sleep function - prevents bot spam

# Sign in function
reddit = praw.Reddit(client_id='CLIENT_ID',
                     client_secret=’CLIENT_SECRET’, password='PASSWORD',
                     user_agent='USERAGENT', username='USERNAME')

print ‘logged in bois’

while 1 == 1: #Makes the bot work constantly

    post = randint(1,8) #Generates a random whole number between 1 and 8. Can be expanded for more threads.

    if post == 1:
        r.submit('teenagers', "What's your unpopular opinion?", text='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!')
		print "submitted What's your unpopular opinion?"
    else if post == 2:
        r.submit('teenagers', 'Controversial opinion thread', text='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!')
		print 'submitted Controversial opinion thread'
    else if post == 3:
        r.submit('teenagers', 'Guys ask girls, girls ask guys' text='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!')
		print 'submitted Guts ask girls, girls ask guys' 
    else if post == 4:
        r.submit('teenagers', 'Selfie thread' text='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!')
		print 'submitted Selfie thread'
    else if post == 5:
        r.submit('teenagers', 'Selfie thread but you have to take a new selfie for it' text='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!')
		print 'submitted Selfie thread but you have to take a new selfie for it'
    else if post == 6:
        r.submit('teenagers', 'User recognition thread' text="""Comment and people will tell you how well they recognize you on a scale of 1-10.
    
        ^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!""")
		print 'submitted User recognition thread'
    else if post == 7:
        r.submit('teenagers', 'Truth or dare thread' text='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!')
		print 'submitted Truth or dare thread'
    else if post == 8:
       	   r.submit('teenagers', 'How tall are you?' text='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!')
		   print 'submitted How tall are you?'
	else if post == 9:
		r.submit('teenagers', 'How much do you weigh?' text='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!')
		print 'submitted How much do you weigh?'
	else if post == 10:
		r.submit('teenagers', 'Camera roll thread', """Comment the number of images in your camera roll, then someone will reply with a number and you'll reply with the corresponding picture.

		^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!""")
		print 'submitted Camera roll thread'
	else if post == 11:
		r.submit('teenagers', '2 truths and a lie thread', text='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!')
		print 'submitted 2 truths and a lie thread'
	else if post == 12:
		r.submit('teenagers', "What's something that a lot of people like but you don't care for?", text='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!')
		print 'submitted What's something that a lot of people like but you don't care for?'
	else if post == 13:
		r.submit('teenagers', 'What was one good thing and one bad thing that happened today?' text='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!')
		print 'submitted What was one good thing and one bad thing that happened today?'
	else if post == 14:
		r.submit('teenagers', 'Yay or nay thread', text="""Comment something and people will respond with yay or nay
		
		^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!'""")
		print 'submitted Yay or nay thread'
	else if post == 15:
		r.submit('teenagers', 'What is your worst quality?', text='^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!')
		print 'submitted What is your worst quality?'
	else if post == 16:
		

^^remember ^^to ^^sort ^^/r/teenagers ^^by ^^new ^^to ^^engage ^^in ^^new ^^discussion ^^posts!"""
    # Continue for the rest of the threads in timawesomeness' wiki
    time.sleep(900) # Wait 900 seconds (15 minutes) before posting again