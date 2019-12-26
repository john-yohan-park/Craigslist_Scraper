# Craigslist_Scraper

Have you ever searched for *that one item* but haven't been able to find it? What if it was possible for you to search for that item *nationwide* and have a good deal while you're at it? That's where *Craigslist_Scraper* comes in :)

## Introduction
Searches Craigslist nationwide to see if someone is selling the item you're searching for

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
- `cd` into `Craigslist_Scraper` directory
- type `python3 craigslist_scraper.py 'ITEM NAME' MIN_PRICE MAX_PRICE` in Terminal
    - For example, `python3 craigslist_scraper.py 'Honda S2000' 6000 20000`
    - Don't forget to put single quotes around `ITEM NAME`:)
- returns list of searched cities & list of URLs for posts that have the item you're looking for

Fork / Clone this repo and narrow down the list of cities searched or mod it any way you'd like :)
