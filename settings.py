#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file contains the Pelican settings for the TDWG website (typically called "pelicanconf.py").
#
# All setting identifiers are explained at http://docs.getpelican.com/en/stable/settings.html, 
# except for some theme settings listed at the end of this file.
#
# To generate the site locally with these settings, use: "pelican -s settings.py". Some of these 
# settings will be overwritten on the development server using "settings-dev.py" or production 
# server using "settings-prod.py".

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
PLUGINS = [
    "pelican-page-hierarchy",
    "pelican-page-order",
    "tipue_search",
    "github_edit_url"
]

# URLS

# The URL structure we use is "path/to/page/" without .html at the end.
# Doing so has the advantage that there is a logical page at every level in the URL:
# 
# standards/     -> standards/index.html created from standards.md (rather than standards.html)
# standards/dwc/ -> standards/dwc/index.html created from standards/dwc.md
# 
# Pelican will already redirect "path/to/page" (no slash) to "path/to/page/" (with slash).
# The plugin "pelican-page-hierarchy" makes sure page paths in content are reflected in the output,
# rather than flattening the directory structure (default behaviour), which can cause name clashes.
# It also adds "parents/children" attributes to pages, which allows to create a collapsed navigation.
#
# Articles/posts are only used for the news section, so we move it there. The default index.html 
# (which lists all articles) is moved to news/ as well and we use home.md as the static homepage.
# We add year/ to article URLs to group them somewhat. Author, category and tag pages are disabled.
# 
# The names of articles and pages are based on their filename, so no {slug} needs to be set in 
# the page metadata.

SITEURL = ""
SLUGIFY_SOURCE = "basename" # Use filename of Markdown files as {slug}
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
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
DIRECT_TEMPLATES = ["index", "archives"] # Which "index" type templates to enable

# FEEDS

# All feeds except articles/posts RSS are disabled.

FEED_DOMAIN = SITEURL
FEED_ATOM = None
FEED_RSS = "feeds/rss.xml"
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# DISPLAY

SITENAME = "TDWG"
SITESUBTITLE = "Biodiversity Information Standards"
AUTHOR = "TDWG"
DEFAULT_LANG = "en"
TIMEZONE = "UTC"
DEFAULT_DATE = "fs" # Use file date as default article date
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 50
LINKS = []
SOCIAL = [
    ("Twitter", "https://twitter.com/tdwg"),
    ("GitHub", "https://github.com/tdwg")
]

# NAVIGATON

# Pages are organized in a hierarchy, which is also reflected in their URL (see URL settings above).
# 
# The navbar of tdwg-theme will show DISPLAY_PAGES_ON_MENU on the left, MENUITEMS on the right.
# Top level pages are always shown, 2nd level pages are collapsed, further levels are not displayed.
# To hide pages from the navigation, add "status: hidden" in their metadata. Note that doing so 
# for a parent page, will make all its children top level pages!

# Pages are ordered by their title. This can be overwritten by adding "page_order: integer" to their
# metadata. The plugin "pelican-page-order" allows to set this only where necessary (rather than on 
# every page).

PAGE_ORDER_BY = "title"
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ("News", "/news/")
]

# THEME + THEME SPECIFIC SETTINGS

THEME = "../tdwg-theme"
DIRECT_TEMPLATES.append("search") # For tipue-search
SITEDESCRIPTION = ""
GITHUB_CONTENT_URL = "https://github.com/tdwg/website/blob/master/content" # For github_edit_url plugin
