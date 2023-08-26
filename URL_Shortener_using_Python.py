# pip install pyshorteners
# pip install pyperclip

import pyshorteners

url = input('Enter the url: ')


def shortenurl(url):
    s = pyshorteners.Shortener()
    print("shortened URL is:")
    print(s.tinyurl.short(url))

shortenurl(url)
