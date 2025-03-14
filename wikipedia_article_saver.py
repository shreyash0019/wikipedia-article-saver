from bs4 import BeautifulSoup
import requests

# Trying to open a random Wikipedia article
# Special:Random opens random articles
res = requests.get("https://en.wikipedia.org/wiki/Special:Random")
res.raise_for_status()

# Parse the article
wiki = BeautifulSoup(res.text, "html.parser")

# Open a file to save the article
r = open("random_wiki.txt", "w+", encoding='utf-8')

# Adding the heading to the text file
heading = wiki.find("h1").text
r.write(heading + "\n")

# Write the content of the article
for i in wiki.select("p"):
    r.write(i.getText())

r.close()
print("File Saved as random_wiki.txt")
