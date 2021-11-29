import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "Thank you to [LEADER] for noticing my [GREAT] [ACHIEVEMENTS]. This is only the [BEGINNING] and we will [FIGHT] on to drain the [SWAP]",
    "It is time to fight [TYRANNY] through the means of [FORCE]! There is no [COUNTRY] that comes even close to [CHALLENGING] the [MIGHT] of the Unites State of America",
    "What is the meaning of this [CONFERENCE]? All I see is a [BUNCH] of [WEAKLINGS] with no sense of [DIRECTION] and capacity for [ACTION]",
    "[LOVE],[POWER] and [PERSEVERENCE] - that is my [MOTTO]. If you have a problem with that, I suggest you visit a [DOCTOR]",
    "No one can [CONTEMPLATE] [CURRENT] conditions without finding much that is satisfying and still more that is encouraging. Our own [COUNTRY]\
         is leading the world in the general readjustment to the results of the great conflict. Many of its [BURDENS] will bear heavily upon us for [YEARS],\
              and the secondary and indirect effects we must expect to experience for some time.",
    "There is something that I must say to my people, who stand on the warm threshold which leads into the palace of [JUSTICE]: In the process of gaining our [RIGHTFUL] place, \
        we must not be guilty of [WRONGFUL] deeds. Let us not seek to satisfy our [THIRST] for [FREEDOM] by drinking from the cup of bitterness and hatred.\
             We must forever conduct our struggle on the high plane of dignity and discipline. We must not allow our creative protest to degenerate into physical violence.\
                  Again and again, we must rise to the [MAJESTIC] heights of meeting physical force with [SOUL] force."
]

replacements = {
    'LEADER': ['Nancy Pelosi', 'Chuck Schumer', 'Vladimir Putin', 'Fidel Castro', 'Kim Jong-Un', 'Angela Merkel'],
    'GREAT': ['great', 'magnificent', 'fantastic', 'wonderful', 'blinding'],
    'ACHIEVEMENTS': ['war efforts', 'public speaking skills', 'commitment to this country', 'hair'],
    'BEGINNING': ['beginning', 'start', 'genesis', 'dawn', 'emergence'],
    'FIGHT': ['fight', 'grapple', 'brawl', 'struggle', 'duel'],
    'SWAP': ['swamp', 'marsh', 'bog', 'bayou', 'moor', 'wetland'],
    'TYRANNY': ['tyranny', 'communism', 'Russia', 'China'],
    'FORCE': ['depriving them from my excellence', 'force', 'blitzkrieg', 'overthrowing their weak and meager governemnt'],
    'CHALLENGING': ['challenging', 'testing', 'meeting', 'stretching', 'taxing'],
    'MIGHT': ['might', 'power', 'force', 'strength', 'energy', 'stamina', 'stoutness'],
    'CONFERENCE': ['conference', 'meeting', 'pointless debate', 'substandard political discussion thread'],
    'BUNCH': ['bunch', 'group', 'gathering', 'collective', 'mass'],
    'WEAKLINGS': ['weaklings', 'sissies', 'namby-pambys', 'cowards', 'pushovers', 'commies', 'softies', 'ninnies', 'doormats', 'chickens'],
    'DIRECTION': ['direction', 'determination', 'courage', 'guidance', 'leadership'],
    'ACTION': ['action', 'anything worth anything', 'deliberation', 'success'],
    'LOVE': ['Love', 'Kill', 'Adore', 'Learn', 'power'],
    'POWER': ['power', 'domination', 'weak central government', 'corporate interests', 'leader of the people'],
    'PERSEVERENCE': ['perseverence', 'power', 'greatness', 'force', ],
    'MOTTO': ['motto', 'decree', 'insigia', 'insight', 'maxim'],
    'DOCTOR': ['doctor', 'psychiatrist', 'Chairman Mao', 'Democratic Party', 'AA meeting'],
    'CONTEMPLATE': ['contemplate', 'ponder', 'consider', 'envisage', 'deliberate on'],
    'CURRENT': ['current', 'present', 'prevailing', 'existing', 'ongoing'],
    'COUNTRY': ['country', 'homeland', 'state', 'nation', 'community'],
    'BURDENS': ['burdens', 'problems', 'concerns', 'difficulties', 'hardship'],
    'YEARS': ['years', 'weeks', 'months' 'decades', 'centuries', 'millenia'],
    'JUSTICE': ['justice', 'righteousness', 'piousness', 'rectitude', 'truth'],
    'RIGHTFUL': ['rightful', 'promised', 'destined', 'just', 'true'],
    'WRONGFUL': ['wrongful', 'illegitimate', 'immoral', 'unfair', 'unlawful'],
    'THIRST': ['Thirst', 'desires', 'longing', 'appetite', 'hunger'],
    'FREEDOM': ['freedom', 'liberty', 'justice', 'opportunity', 'power'],
    'MAJESTIC': ['majestic', 'great', 'unimaginable', 'wholesome', 'immaculate'],
    'SOUL': ['soul', 'spiritual', 'justice', 'though', 'cause']


}


# function to generate comments from madlibs

def generate_comment():

    m = random.choice(madlibs)
    for k in replacements.keys():
        m = m.replace('['+k+']', random.choice(replacements[k]))
    return m


# connect to reddit
reddit = praw.Reddit('botthehamhottspurs')


# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r2yref/green_thread/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code,
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print('new iteration at:', datetime.datetime.now())
    print('submission.title=', submission.title)
    print('submission.url=', submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    submission.comments.replace_more(limit=None, threshold=0)
    all_comments = submission.comments.list()

    # HINT:
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information
    # about the results of that task,
    # and manually inspect that information to ensure it is correct;
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=', len(all_comments))

    # (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT:
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'botthehamhottspurs':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know
    # how many comments there should be.
    print('len(not_my_comments)=', len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not

    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has not commented = ', has_not_commented)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        submission.reply(generate_comment())

    else:
        # (task 3): filter the not_my_comments list to also remove comments that
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []

        for comment in not_my_comments:
            comment_reply_author = []
            for reply in comment.replies:
                comment_reply_author.append(str(reply.author))
            if 'botthehamhottspurs' in comment_reply_author:
                pass
            else:
                comments_without_replies.append(comment)

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=', len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        try:
            comment = random.choice(comments_without_replies)
            try:
                comment.reply(generate_comment())

            except praw.exceptions.APIException:
                print("not replying to a deleted comment")
                pass
        except IndexError:
            print("my comments")
            pass

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    submission = random.choice(
        list(reddit.subreddit("BotTown2").hot(limit=5)))

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(1)
