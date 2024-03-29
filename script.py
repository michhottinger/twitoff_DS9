import requests
from urllib3.exceptions import InsecureRequestWarning
from TWITOFF.models import *
from TWITOFF.twitter import *

requests.packages.urllib3.disable_warnings()

# DB.drop_all()
# DB.create_all()
# u1 = User(name='austen', id=89181)
# t1 = Tweet(text='jajajaj', id=189199)
# u1.tweets.append(t1)
# DB.session.add(u1)
# DB.session.add(t1)
# DB.session.commit()

twitter_user=TWITTER.get_user('elonmusk')
tweets=twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, tweet_mode='extended')
db_user = User(id=twitter_user.id, name=twitter_user.screen_name, newest_tweet_id=tweets[0].id)
for tweet in tweets:
     embedding=BASILICA.embed_sentence(tweet.full_text,model='twitter')
     db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:500], embedding=embedding)
     DB.session.add(db_tweet)
     db_user.tweets.append(db_tweet)

DB.session.add(db_user)
DB.session.commit()
