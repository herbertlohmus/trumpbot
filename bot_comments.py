import praw
import random
import time
reddit = praw.Reddit('botthehamhottspurs')

for i in range(30):
    try:
        top = list(reddit.subreddit('TrumpCriticizesTrump').hot(limit=None))
        submission = random.choice(top)
        title = submission.title
        url = submission.url
        text = submission.selftext
        if url:
            reddit.subreddit('BotTown2').submit(title, url=url)
            print("submission ", i)
        else:
            reddit.subreddit('BotTown2').submit(title, selftext=text)
            print("submission ", i)
    except praw.exceptions.InvalidURL:
        print('The URL is not Valid')
        pass
    time.sleep(1)
