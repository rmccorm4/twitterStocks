# This is to let you import without being in the same directory
# by inserting the location of python-twitter to the Python path at runtime
import sys
sys.path.insert(0, '/home/ryan/python-twitter')

# import this from python-twitter which was added to the Python path above
import twitter

api_key = "iQ4Rub4cKSodFhSPfjSlmJ8zN"
api_secret = "dPDMXWKLjZW0VHHwXgUyWjksvCcxqR58MhiCKfq98cPWfApNoo"
access_token_key = "2416693503-NPrjHTfcHQD0HE3TtTP24lkdPIsXzyvxE3zH2Fs"
access_token_secret = "qP2GTWoTu446o5wM2BB8KXkajvrQ74dBb9vRlcPEaHKH1"

api = twitter.Api(api_key, api_secret, access_token_key, access_token_secret)

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
results = api.GetSearch("car")
#print([r.text+'\n\n\n' for r in results])
for r in results:
    print r.text.encode('utf-8')
    print '\n'
