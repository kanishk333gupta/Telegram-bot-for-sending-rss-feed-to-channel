from time import sleep
import requests
import feedparser
from datetime import timedelta, datetime
from dateutil import parser

BOT_TOKEN = '1451344756:AAHT2BkIOE-BE44kRpTD1X5alz_gfG2oml0'
CHANNEL_ID = '-1001526730174' # https://t.me/c/1526730174/17
FEED_URL = 'https://www.hindustantimes.com/feeds/rss/business/rssfeed.xml' # https://something.com/feeds/rss.xml # https://www.youtube.com/aashiqui2/

def send_message(message):
    requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&text={message}')
		
def main():
   rss_feed = feedparser.parse(FEED_URL)
   for entry in rss_feed.entries:
       parsed_date = parser.parse (entry.published)
       parsed_date = (parsed_date - timedelta (hours=8)).replace (tzinfo=None)  # remove timezone offset
       now_date = datetime.utcnow ()
       published_10_minutes_ago = now_date - parsed_date < timedelta (minutes=1000)
       feed_title = entry.title
       feed_link = entry.link
       ytlink = f'{feed_title} \n {feed_link}'
       if published_10_minutes_ago:
           print (ytlink)
           send_message (ytlink)

if __name__ == "__main__":
    while(True):
        main()
        sleep(12*60*60)
        