from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'zlLRknZGJ4tviE542miA'
csecret = 'XBpTd5FCd3wSmbEZLOVU8mvtxXACs90Upe9cWI5fds'
atoken = '1740685196-gdNLufueLAKUJkpGopk2WkqsxWUy4ELsttx7cGu'
asecret = 'W0EKYAYcXhya5klWkfedtjqMMmRxM2kNpJ4ZETYZGaz7p'

class listener(StreamListener):

    def on_data(self, data):
        try:
            print data
            saveFile = open('frozen2.txt','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'fail ondata,', str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["frozen"])
