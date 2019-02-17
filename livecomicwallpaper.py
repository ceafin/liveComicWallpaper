#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""A short description of the module -- called a docstring."""

# Here comes your imports
import datetime

# Here comes your (few) global variables
# Here comes your class definitions
# Here comes your function definitions


def main():
    url = "https://www.gocomics.com/calvinandhobbesespanol/"

    today = datetime.datetime.now()

    url += today.strftime("%Y/%m/%d/")

    print(url)

    return 0


if __name__ == "__main__":
    main()
