##from gnewsclient import gnewsclient
##client = gnewsclient.NewsClient()
##client.get_config()
##client.topics
##client.location = 'India'
##client.language = 'Hindi'
##client.topic = 'Sports'

##client.get_news()
##print(client.get_news)

from gnewsclient import gnewsclient
client = gnewsclient.NewsClient()
client.get_config()
client.topics
client.location = 'India'
client.language = 'Hindi'
client.topic = 'Sports'

client.get_news()

