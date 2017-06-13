from github import Github
from twython import Twython
from time import sleep

g = Github("loganoconnell", "")
repos = []

for repo in g.get_user().get_repos():
	repos.append(repo.name)

print "Repos:"
for repo in repos:
	print " - " + repo

def tweet(name):
	tweetStr = "I published a new GitHub repo: " + name + "\nhttps://github.com/loganoconnell/" + name

	apiKey = ""
	apiSecret = ""
	accessToken = ""
	accessTokenSecret = ""

	api = Twython(apiKey, apiSecret, accessToken, accessTokenSecret)
	api.update_status(status = tweetStr)

	print "Tweeted: " + tweetStr

while True:
	for repo in g.get_user().get_repos():
		if (repo.name not in repos):
			tweet(repo.name)
			
	print "Sleeping..."
	sleep(300)