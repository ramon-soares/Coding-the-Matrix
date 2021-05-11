# pip install pyshorteners
import pyshorteners

url = "https://pypi.org/project/pyshorteners/"

link = pyshorteners.Shortener()
shorten_url = link.tinyurl.short(url)
print(f"\n{shorten_url}")
