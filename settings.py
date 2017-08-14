#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file contains the default and local settings (default name: pelicanconf.py)
# You can use these to generate the website locally with: pelican -s settings.py
# Some of these settings will be overwritten in the development (settings-dev.py) or production 
# environment (settings-prod.py).

# CONTENT

# Source content (Markdown files, images) are kept in "content".
# The site is generated in "output", which is ignored by git to avoid cluttering the repo.

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
PLUGINS = ["pelican-page-hierarchy"]

# URLS

# The URL structure we use is "path/to/page/" without .html at the end.
# Doing so has the advantage that there is a logical page at every level in the URL:
# 
# standards/     -> standards/index.html created from standards.md (rather than standards.html)
# standards/dwc/ -> standards/dwc/index.html created from standards/dwc.md
# 
# Pelican will already redirect "path/to/page" (no slash) to "path/to/page/" (with slash).
# The plugin pelican-page-hierarchy makes sure page paths in content are reflected in the output,
# rather than flattening the directory structure (default behaviour), which can cause name clashes.
# It also adds "parents/children" attributes to pages, which allow to create collapsed navigation.
#
# Articles/posts are only used for the news/ section, so we move it there. The default index.html 
# (which lists all articles) is moved to news/ as well and we use home.md as the static homepage.
# We add year/ to article URLs to group them somewhat. Author, category and tag pages are disabled.
# 
# The names of articles and pages are based on their filename, so no {slug} needs to be set in 
# the page metadata.

SITEURL = ""
SLUGIFY_SOURCE = "basename" # Use filename of Markdown files as {slug}:
ARTICLE_URL = "news/{date:%Y}/{slug}"
ARTICLE_SAVE_AS = "news/{date:%Y}/{slug}/index.html"
INDEX_SAVE_AS = "news/index.html"
ARCHIVES_SAVE_AS = "news/archives.html"
YEAR_ARCHIVE_SAVE_AS = "news/{date:%Y}/index.html"
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# FEEDS

# All feeds except articles/posts RSS are disabled.

FEED_DOMAIN = SITEURL
FEED_ATOM = None
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
SITESUBTITLE = "Biodiversity Information Standards"
AUTHOR = "TDWG"
DEFAULT_LANG = "en"
TIMEZONE = "Europe/Copenhagen" # Use file date as default article date
DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT = "%Y-%m-%d" # Articles with future dates are considered drafts
WITH_FUTURE_DATES = False
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 50
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ("News", "/news/index.html")
]
LINKS = []
SOCIAL = [
    ("Twitter", "https://twitter.com/tdwg"),
    ("GitHub", "https://github.com/tdwg")
]
GITHUB_URL = "https://github.com/tdwg/website"
