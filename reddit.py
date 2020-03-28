import praw
import requests
import pandas as pd
reddit = praw.Reddit(client_id = ' ',
                    client_secret = ' ',
                    username = ' ',
                    password = ' ',
                    user_agent = 'sbuxAssignment')

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}

subreddit = reddit.subreddit('Popular')

#Original Content
    #for loop looking at top 100 submissions in r/popular/hot
    # check to see if the current submission is an Original
    #True --> append data to topics_dict
    #False --> nothing
for submission in subreddit.hot(limit = 100):   #looking at top 100 posts
    if(submission.original):                     #returns a true or false as to whether the submission is original
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)


topics_data = pd.DataFrame(topics_dict)
topics_data.to_csv('FILENAME.csv', index = False)


#Over 1000 comments
    #for loop looking at top 100 submissions in r/popular/hot
    #check to see if the number of comments of current submission > 1000
    #True --> append data to topics_dict
    #False --> nothing
for submission in subreddit.hot(limit = 100):   #looking at top 100 posts
    if(submission.num_comments > 1000):
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
topics_data.to_csv('FILENAME.csv', index = False)


#Top 10 posts
    #for loop looking at top 10 submissions in r/popular/hot
    #check to see if there is a submission after the current one
    #True --> if statement checks to see if current submission's score is greater than the next submission's score
        #True --> append data to topics_dict
        #False --> nothing
    #False --> nothing
for submission in subreddit.hot(limit = 10):    #looking at top 10 posts
    while submission.hasNext:
        if(submission.score > submission.score.next):
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            topics_dict["url"].append(submission.url)
            topics_dict["comms_num"].append(submission.num_comments)
            topics_dict["created"].append(submission.created)
            topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

topics_data.to_csv('FILENAME.csv', index = False)

#Unique subreddits
    #for loop looking at top 100 submissions in r/popular/hot
    #check to see the number of occurrences of subreddit in r/popular/hot
        #If == 1 --> append data to topics_dict
        #Else --> nothing
for submission in subreddit.hot(limit = 10):
    if(submission.occurrences == 1):
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

topics_data.to_csv('FILENAME.csv', index = False)


#Multireddit
    #for loop looking at top 100 submissions in r/popular/hot
    #Check to see the number of occurrences of subreddit in r/popular/hot
        # If >= 2 --> append data to topics_dict
        # Else --> nothing
for submission in subreddit.hot(limit = 10):
    if(submission.occurrences >= 2):
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["id"].append(submission.id)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created"].append(submission.created)
        topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

topics_data.to_csv('FILENAME.csv', index = False)
