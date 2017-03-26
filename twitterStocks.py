import datetime
import time

# This is to let you import without being in the same directory
# by inserting the location of python-twitter to the Python path at runtime
import sys
#need to change path to where you locally downloaded python-twitter from github
sys.path.insert(0, '/home/ryan/projects/twitterStocks/python-twitter')

# import this from python-twitter which was added to the Python path above
import twitter

api_key = "iQ4Rub4cKSodFhSPfjSlmJ8zN"
api_secret = "dPDMXWKLjZW0VHHwXgUyWjksvCcxqR58MhiCKfq98cPWfApNoo"
access_token_key = "2416693503-NPrjHTfcHQD0HE3TtTP24lkdPIsXzyvxE3zH2Fs"
access_token_secret = "qP2GTWoTu446o5wM2BB8KXkajvrQ74dBb9vRlcPEaHKH1"

api = twitter.Api(api_key, api_secret, access_token_key, access_token_secret)

"""
PSEUDOCODE

    find id of last tweet from previous night or first tweet of day (previous night probably
    easier with the getsearch parameters

    getSearch 100 tweets for stockname from that tweet id 

    Keep searching from the last id of the 100 tweets you just got until the day is over

"""

"""
GETTING TIMESTAMPS

    stockTweets = [tweet.text.encode('utf-8') for tweet in totalTweets]
    datestamps = [tweet.created_at for tweet in totalTweets]
    timestamps = []
    #get only the times Hour:Min:Sec from the dates
    for time in datestamps:
        colonIndex = time.find(':')
        time = time[colonIndex-2:colonIndex+6]
        timestamps.append(time)
"""


#returns list of all tweets 
def getStockTweets(stockName):
    stockName = "$"+stockName
    now = datetime.datetime.now()
    today = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    yesterday = now - datetime.timedelta(days=1)
    yesterday = str(yesterday.year) + "-" + str(yesterday.month) + "-" + str(yesterday.day)

    yesterdaysTweetID = api.GetSearch(stockName, count=1, result_type="recent", lang='en', since=yesterday, until=today)[0].id

    lastTweetID = yesterdaysTweetID

    firstTweets = api.GetSearch(stockName, count=100, lang='en', since_id=lastTweetID)
    lastTweetID = firstTweets[-1].id

    
    nextTweets = []
    totalTweets = []
    prevLastTweetID = -1
    while(prevLastTweetID != lastTweetID):
        prevLastTweetID = lastTweetID
        nextTweets = api.GetSearch(stockName, count=100, lang='en', since_id=lastTweetID)
        #last id of the 100 previous 100 tweets
        if(len(nextTweets)>0):
            lastTweetID = nextTweets[-1].id
        #add all tweets to one list
        totalTweets += nextTweets
        #give Twitter servers a break
        time.sleep(1)
    return totalTweets
    
def getSentiments(totalTweets):
    positiveWords = ["good", "buy", "great", "bull", "up"]
    negativeWords = ["bad", "sell", "terrible", "bear", "down"]
    positive = 0
    negative = 0

    i=1
    for tweet in totalTweets:
        for word in positiveWords:
            if word in tweet.text.encode('utf-8'):
                positive += 1
                print i, tweet.text.encode('utf-8')
                print tweet.created_at
        for word in negativeWords:
            if word in tweet.text.encode('utf-8'):
                negative += 1
                print i, tweet.text.encode('utf-8')
                print tweet.created_at
        i+=1

    print "POSITIVE TWEETS: " + str(positive)
    print "NEGATIVE TWEETS: " + str(negative)
   
def main():
    stockName = raw_input("Please enter the ticker name for the desired stock (Example: For Nvidia type NVDA): ") 
    totalTweets = getStockTweets(stockName)
    getSentiments(totalTweets)

main()

