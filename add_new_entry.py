#!/usr/bin/env python

__author__ = "Christian Christiansen"
__copyright__ = "Copyright 2021, Christian Christiansen"
__license__ = "AGPLv3"
__email__ = "christian dot l dot christiansen at gmail dot com"

import sys
import os
import re
import html
from datetime import datetime
from pytz import timezone

man = ("Add an entry to log. Run python add_new_entry.py path/to/entry.html "
       "to add an entry.")

class Entry:
    def __init__(self, filename, url="https://christianchristiansen.net/"):
        self.filename = filename
        self.link = url+self.filename
        with open(filename, "r") as f:
            self.text = f.read()

    @property
    def title(self):
        return re.search(
            ".*?<h1 class=\"title\">(.*?)</h1>.*?", self.text).group(1)

    @property
    def content(self):
        return re.search(
            ".*?<div id=\"content\">(.*?)</div>\n<div class=\"footer\".*?",
            self.text,
            re.DOTALL).group(1)

    @property
    def pubDate(self):
        return datetime.now(timezone('Australia/Sydney')).strftime(
            "%a, %d %b %Y %H:%M:%S %Z")

    @property
    def rss_content(self):
        return html.escape(self.content)

    def rss_entry(self, rss):
        insert_here = -1
        for i, line in enumerate(rss):
            if "<item>" in line:
                insert_here = i
                break
        if insert_here == -1:
            raise Exception("Unable to find place to insert new entry.")

        new_rss_entry = f"""    <item>
        <title>{self.title}</title>
        <link>{self.link}</link>
        <pubDate>{self.pubDate}</pubDate>
        <guid>
        {self.link}
        </guid>
        <description>
        {self.rss_content}
        </description>
    </item>\n"""

        return rss[:insert_here]+[new_rss_entry]+rss[insert_here:]

    def add_to_rss(self, filename):
        with open(filename, "r") as f:
            rss = f.readlines()
            if self.link in rss:
                ans = input(
                    "This file has already been added to rss. Are you sure you"
                    " want to add this file? (y, N) ")
                if len(ans) == 0 or ans[0].lower() != "y":
                    raise Exception(
                        f"{self.title} has already been added to rss")
            rss = self.rss_entry(rss)

        with open(filename, "w") as f:
            f.write("".join(rss))

def insert(entry, index, same_dir=False):
    if entry.filename in "".join(index):
        ans = input(
            "This file has already been added to this index. Are you sure you "
            " want to add this file? (y, N) ")
        if len(ans) == 0 or ans[0].lower() != "y":
            raise Exception(f"{entry.filename} has already been added")

    insert_here = -1
    for i, line in enumerate(index):
        if ".htm" in line and "<p" in line[:2]:
            insert_here = i
            insert_line = line
            break
    if insert_here == -1:
        raise Exception("Unable to find place to insert new entry.")

    if same_dir:
        filename = entry.filename.split("/")[-1]
    else:
        filename = entry.filename

    insert_line = insert_line.replace(
        re.search(".*?href=\"(.*?\.htm.*?)\".*?", insert_line).group(1),
        filename)
    insert_line = insert_line.replace(
        re.search(".*?htm.*?>(.*?)<.*?", insert_line).group(1),
        entry.title)

    return index[:insert_here]+[insert_line]+index[insert_here:]


def add_entry(filename, default_indices=list(), rss="rss.xml"):
    if len(default_indices) == 0:
        default_indices = ["details.html", "log/index.html"]

    if filename.split(".")[-1].lower() not in ["html", "htm"]:
        ans = input(
            "This file does not end in html or htm. Are you sure you want to "
            "add this file? (y, N) ")
        if len(ans)==0 or ans[0].lower() != "y":
            raise Exception(f"{filename} does not end in html or htm.")
    try:
        entry = Entry(filename)

        for x in default_indices:
            with open(x, "r") as f:
                index = f.readlines()
                if "log/" in x:
                    index = insert(entry, index, same_dir=True)
                else:
                    index = insert(entry, index)

            with open(x, "w") as f:
                f.write("".join(index))

        entry.add_to_rss(rss)

    except Exception as e:
        print(f"{filename} coud not be added due to error {e}.")

def main(args):
    if args[0] in ["-h", "--help"]:
        print(man)
        return True

    for filename in args:
        try:
            add_entry(filename)
        except Exception as e:
            print(f"{filename} could not be added due to error {e}.")

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        main(sys.argv[1:])
    else:
        print(man)
