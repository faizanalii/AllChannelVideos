import requests
from bs4 import BeautifulSoup as bp
import subprocess
import youtube_dl
url=input()
r=requests.get("{}".format(url))
##r.text
soup=bp(r.text,'html.parser')
##creating a list to store links 
store_links=[]
for i in soup.findAll('a'):
    store_links.append(i.get('href'))
##"/watch?v=dgWOqZJ5S1g" we're getting only id's of videos so we can process them 
##There're also some links comeup so to remove them we can just do a simple loop
for i in store_links:
	if i[0:8]=='/watch?v':
		continue
	else:
		store_links.remove(i)
##""//www.youtube.com/yt/about/ur/"" Some links like this still remains so I can do another loop as the length of id is 20 
##so i can do a simple len loop 
for i in store_links:
	if len(i)!=20:
		store_links.remove(i)
	else:
		continue
##In my scenario 4 links still remains so I'm doing this manually by just popping hopefully you don't find any garbage links 
##if you do simply pop them "store_links.pop()" it'll remove the last item or you can pop them with the index like "store_links.pop(1)"
download_links=[]
##I have'nt tried the youtube_dl in python so I'm calling it from the command prompt.
##adding "https://www.youtube.com/" to the start of every id
for i in store_links:
	i="https://www.youtube.com/"+i
	download_links.append(i)
for i in download_links:
	print(i)
input("Enter NUmber")
##This loop download all the videos

# for i in download_links:
# 	subprocess.call('youtube-dl -f best {}'.format(i))