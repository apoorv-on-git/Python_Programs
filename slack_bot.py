#Slackbot to send automated messages on the given time

from slackclient import SlackClient
import time

token = ""		#Your auth_token
sc = SlackClient(token)
channel = ""		#Channel ID
greeting = ""		#Message you want to post
time.sleep(60*60*7)
print sc.api_call(
	"chat.postMessage",
	as_user="true:",
	channel = channel,
	text = greeting
)

