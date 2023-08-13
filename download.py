import csv
from youtube_search import YoutubeSearch
import webbrowser
import pafy
import youtube_dl
import os

# Extracting Names of songs from Songs(.csv File) and storing in a list  
result = []
with open(r'Your path to songs.csv file', 'r') as file:
    csvreader = csv.reader(file, delimiter=':')
    for row in csvreader:
        result += row

# Using the Names of Songs,Searching them on youtube and storing the url of the first result 
links = []
i = 0
for song in result:
    if i == 0:
        i = 1
        continue
    results = YoutubeSearch(f"{song}", max_results=1).to_dict()
    for v in results:
        links.append('https://www.youtube.com' + v['url_suffix'])

# Make a txt file and put its path down here 
# Converting the links to a txt file 
with open(r'Path of txt file', 'w') as fp:
    for item in links:
        fp.write("%s\n" % item)


SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + 'Path of where you want to save downloaded songs'
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
}

# Extracting URLs from txt file and downloading audio using youtube_dl 
file = open(
    'Path of txt file', 'r')


for line in file:

    url = line
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


file.close()



