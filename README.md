# National_Craigslist

Have you ever searched online for *that one item* but haven't been able to find it? What if it was possible for you to search for that item *nationwide* and have a good deal while you're at it? That's where *National Craigslist* comes in handy :)

## Introduction
Searches Craigslist nationwide to see if someone is selling the item you're looking for

## System Requirements
Name           | Terminal Command
---            | ---
Homebrew       | `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
Python 3       | `brew install python`
Firefox        | `brew cask install firefox`
Selenium       | `pip3 install selenium`
Beautiful Soup | `pip3 install beautifulsoup4`
lxml           | `pip3 install lxml`

## Instructions
- open Terminal
- `cd` into `National_Craigslist` directory
- type `python3 national_craigslist.py 'ITEM NAME' MIN_PRICE MAX_PRICE` in Terminal
    - For example, `python3 national_craigslist.py 'Honda S2000' 6000 20000`
    - Don't forget to put single quotes around `ITEM NAME`:)
- returns list of searched cities & list of URLs for posts that have the item you're looking for

Fork or clone this repo and narrow down the list of cities searched or mod it any way you'd like :)
