#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file contains the default and local settings.
# You can safely use these to generate the website locally with: pelican -s settings.py
# Some of these settings will be overwritten in the development or production environment.

# Site
SITENAME = "TDWG"
SITEURL = ""
AUTHOR = "TDWG"
TIMEZONE = "Europe/Copenhagen"
DEFAULT_LANG = "en"

# Display
# THEME = ""
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = False
DEFAULT_DATE = 'fs'

# URLs
ARTICLE_URL = "news/{slug}.html"
ARTICLE_SAVE_AS = "news/{slug}.html"

# Content
PATH = "content"
ARTICLE_PATHS = ["news"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = [
	"images",
	"files"
]
OUTPUT_PATH = "output" # Default
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ()
CACHE_CONTENT = False

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

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
	("Twitter", "https://twitter.com/tdwg"),
    ("GitHub", "https://github.com/tdwg")
)
