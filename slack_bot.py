#Slackbot to send automated messages on the given time

from slackclient import SlackClient
import time

token = "xoxp-86400529792-267960808803-279459752420-3406cfad8df5b037d0a7fd746e259e94"
sc = SlackClient(token)
channel = "C2JBSS9ML"
greeting = "Yesterday's introspection:-\n1. Less productive day.\n2. I feel good.\n3. I enjoyed working with Rishabh Bhaiya.\n4. Yesterday I learned about Tableau and how to create some awesome data visualisations which are interactive too.\n5. I am thankful to the mentors for helping me out and guiding me to the right way of learning.\nToday's agenda:-\nToday, I will learn how to scrape data from a website by creating a python program."
time.sleep(60*60*7)
print sc.api_call(
	"chat.postMessage",
	as_user="true:",
	channel = channel,
	text = greeting
)

