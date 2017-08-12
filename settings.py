#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file contains the default and local settings.
# You can safely use these to generate the website locally with: pelican -s settings.py
# Some of these settings will be overwritten in the development or production environment.

# Content input/output
PATH = "content"
ARTICLE_PATHS = ["news"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = [
	"images",
	"files"
]
OUTPUT_PATH = "output"
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ()
CACHE_CONTENT = False

# URLs
SITEURL = ""
SLUGIFY_SOURCE = "basename" # Use filename by default
ARTICLE_SAVE_AS = "news/{slug}.html"
ARTICLE_URL = "news/{slug}.html"
# Feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = None
FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Display
SITENAME = "TDWG"
AUTHOR = "TDWG"
DEFAULT_LANG = "en"
TIMEZONE = "Europe/Copenhagen"
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
WITH_FUTURE_DATES = False # Set future dates to draft
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 50
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Theme
# THEME = ""

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ("Twitter", "https://twitter.com/tdwg"),
    ("GitHub", "https://github.com/tdwg")
)
