#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""A Python script turned cron job to grab and assign the latest Calvin & Hobbes comic strip to my MacBook's wallpaper"""

# Here comes your imports
import sys
import datetime
import urllib.request
import re


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

    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    paragraphs = re.findall(r"https://assets\.amuniversal[^\"]*", str(respData))

    for eachP in paragraphs:  # Debug HTML contents to terminal
        print(eachP)

    return 0


if __name__ == "__main__":
    main()
