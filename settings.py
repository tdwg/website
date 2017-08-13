#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file contains the default and local settings (default name: pelicanconf.py)
# You can use these to generate the website locally with: pelican -s settings.py
# Some of these settings will be overwritten in the development (settings-dev.py) 
# or production environment (settings-prod.py).

# Content
PATH = "content"
ARTICLE_PATHS = ["news"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["static"]
OUTPUT_PATH = "output"
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ()
CACHE_CONTENT = False

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["pelican-page-hierarchy"]# Keeps directory structure in page URLs, e.g. /standards/dwc/

# URLs
SITEURL = ""
SLUGIFY_SOURCE = "basename"         # Use filename of Markdown files as {slug}
ARTICLE_URL = "news/{slug}"         # Move articles/posts to news/
ARTICLE_SAVE_AS = "news/{date:%Y}/{slug}/index.html"    
INDEX_SAVE_AS = "news/index.html"   # Move list of articles to news/ Root index.html = home.md
AUTHOR_SAVE_AS = ""                 # Disable author pages
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""               # Disable category pages
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""                    # Disable tag pages
TAGS_SAVE_AS = ""
PAGE_URL = "{slug}/"                # Best setting for pelican-page-hierarchy
PAGE_SAVE_AS = "{slug}/index.html"

# Feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = None
FEED_RSS = "feeds/rss.xml"          # Enable RSS feed only
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
DEFAULT_DATE = 'fs'                 # File date
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
WITH_FUTURE_DATES = False           # Articles with future dates are considered drafts
DEFAULT_PAGINATION = False          # No pagination
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
