#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file contains the default and local settings (default name: pelicanconf.py)
# You can use these to generate the website locally with: pelican -s settings.py
# Some of these settings will be overwritten in the development (settings-dev.py) 
# or production environment (settings-prod.py).


# CONTENT

PATH = "content"
ARTICLE_PATHS = ["news"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["static"]
OUTPUT_PATH = "output"
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ()
CACHE_CONTENT = False


# PLUGINS

PLUGIN_PATHS = ["plugins"]
# Keep directory structure in page URLs (e.g. /standards/dwc/):
PLUGINS = ["pelican-page-hierarchy"]


# URLS

SITEURL = ""
# Use filename of Markdown files as {slug}:
SLUGIFY_SOURCE = "basename"
# Move articles/posts to news/ (e.g. news/2016/conference-announced/):
ARTICLE_URL = "news/{date:%Y}/{slug}"
ARTICLE_SAVE_AS = "news/{date:%Y}/{slug}/index.html"
# Move list of articles to news/ (root index.html is home.md):
INDEX_SAVE_AS = "news/index.html"
ARCHIVES_SAVE_AS = "news/archives.html"
YEAR_ARCHIVE_SAVE_AS = "news/{date:%Y}/index.html"
# Disable author pages:
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
# Disable category pages:
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
# Disable tag pages:
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
# These page settings make most sense for pelican-page-hierarchy:
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"


# FEEDS

FEED_DOMAIN = SITEURL
FEED_ATOM = None
# Enable RSS feed only:
FEED_RSS = "feeds/rss.xml"
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


# DISPLAY

SITENAME = "TDWG"
AUTHOR = "TDWG"
DEFAULT_LANG = "en"
TIMEZONE = "Europe/Copenhagen"
# Use file date as default article date:
DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
# Articles with future dates are considered drafts:
WITH_FUTURE_DATES = False
# No pagination:
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 50
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False


# THEME

# THEME = ""


# BLOGROLL

LINKS = ()


# SOCIAL WIDGET

SOCIAL = (
    ("Twitter", "https://twitter.com/tdwg"),
    ("GitHub", "https://github.com/tdwg")
)
