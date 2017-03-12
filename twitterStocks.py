import datetime

# This is to let you import without being in the same directory
# by inserting the location of python-twitter to the Python path at runtime
import sys
#need to change path to where you locally downloaded python-twitter from github
sys.path.insert(0, '/home/ryan/codeFun/twitterStocks/python-twitter')

# import this from python-twitter which was added to the Python path above
import twitter

api_key = "iQ4Rub4cKSodFhSPfjSlmJ8zN"
api_secret = "dPDMXWKLjZW0VHHwXgUyWjksvCcxqR58MhiCKfq98cPWfApNoo"
access_token_key = "2416693503-NPrjHTfcHQD0HE3TtTP24lkdPIsXzyvxE3zH2Fs"
access_token_secret = "qP2GTWoTu446o5wM2BB8KXkajvrQ74dBb9vRlcPEaHKH1"

api = twitter.Api(api_key, api_secret, access_token_key, access_token_secret)

#returns list of all tweets 
def getStockTweets(stockName):
    results = api.GetSearch("$nvda", count=100, result_type="recent", lang='en', since="2017-03-11")

    stockTweets = [tweet.text.encode('utf-8') for tweet in results]
    datestamps = [tweet.created_at for tweet in results]
    timestamps = []
    #get only the times Hour:Min:Sec from the dates
    for time in datestamps:
        colonIndex = time.find(':')
        time = time[colonIndex-2:colonIndex+6]
        timestamps.append(time)

#prints a bunch of info regarding my account
#=====================================
#print(api.VerifyCredentials())
#print('\n')

#Gets all of my tweets
#=====================================
#statuses=api.GetUserTimeline(screen_name='soccerplayermc')
#print([s.text for s in statuses])

#Gets all of the people that I follow (I think)
#=====================================
#users = api.GetFriends()
#print([u.name for u in users])

#this tweets from my account
#======================================
#status = api.PostUpdate('Testing python-twitter module')
#print(status.text)

#default returns up to 15 tweets but can go up to 100 by passing count=100
#use all times 'since' and 'until' to go through entire day to get all tweets
#if there are more than 100?#
#======================================

"""pseudocode

    find id of last tweet from previous night or first tweet of day (previous night probably
    easier with the getsearch parameters

    getSearch 100 tweets for nvda from that tweet id 

    Keep searching from the last id of the 100 tweets you just got until the day is over

"""

results = api.GetSearch("$nvda", count=100, result_type="recent", lang='en', include_entities=False)
#print([r.text+'\n\n\n' for r in results])

for r in results:
    print r.text.encode('utf-8')
    print r.created_at
    print '\n'

stockTweets = [tweet.text.encode('utf-8') for tweet in results]
datestamps = [tweet.created_at for tweet in results]

timestamps = []
for time in datestamps:
    colonIndex = time.find(':')
    time = time[colonIndex-2:colonIndex+6]
    timestamps.append(time)


