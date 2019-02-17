#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""A Python script turned cron job to grab and assign the latest Calvin & Hobbes comic strip to my MacBook's wallpaper"""

# Here comes your imports
import sys
import datetime
import urllib.request
from urllib.request import urlretrieve
import re
from appscript import app, mactypes


def main():

    print(len(sys.argv))  # Debug the arg by output to terminal

    # Build the "today" URL variable
    url = "https://www.gocomics.com/calvinandhobbesespanol/"
    if len(sys.argv) < 2:
        today = datetime.datetime.now()
        url += today.strftime("%Y/%m/%d/")
    else:
        url += sys.argv[1]
        if url[-1] != "/":
            url += "/"

    print(url)  # Debug the string by output to terminal

    # Request URL, Open it, Read in data
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    # Regex to find the comic graphic asset
    if re.search(r"https://assets\.amuniversal[^\"]*", str(respData)):
        comic = re.findall(r"https://assets\.amuniversal[^\"]*", str(respData))[0]
    else:
        return 1

    print(comic)  # Debug the string of the comic found

    # Grab asset and write to workstation
    urlretrieve(comic, "/tmp/liveComic.png")

    # Set wallpaper
    app("Finder").desktop_picture.set(mactypes.File("/tmp/liveComic.png"))

    return 0


if __name__ == "__main__":
    main()
