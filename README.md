# twitterStocks
Scrape twitter for tweets relating to a public stock in order to gauge public opinion on it to predict upward or downward trends in stock price

## Tools:
Uses Python 2.7, python-twitter API (https://github.com/bear/python-twitter)


## Limitations:
1) Currently written to get tweets from the current day, could be changed to support week/month etc. but also limited by API
2) Runtime of up to 10 minutes during testing to get all tweets from current day
3) API call limits prevent running program in rapid succession, believe it works in 15 minute windows before you get more requests available to you
