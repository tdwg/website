#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file contains the Pelican settings (typically called "pelicanconf.py") for the TDWG website.
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
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["news"]
STATIC_PATHS = ["static", "pages"]
OUTPUT_PATH = "output"
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = []
CACHE_CONTENT = False
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.do"]} # Used in archive_nav.html template


# PLUGINS

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "pelican-page-order",
    "pelican-page-hierarchy",
    "tipue_search",
    "summary",
    "pelican-bootstrapify", # Adds bootstrap classes to content
    "pelican-cover-image",
    "pelican-github-edit"
]


# PLUGIN SETTINGS

PAGE_ORDER_BY = "title" # For pelican-page-order
IGNORE_PAGE_SLUG = True # For pelican-page-hierarchy
GITHUB_CONTENT_URL = "https://github.com/tdwg/website/blob/master/content" # For pelican-github-edit
COVER_IMAGES_PATH = "static/cover_images" # For pelican-cover-image
DEFAULT_COVER_IMAGE = "https://images.unsplash.com/photo-1489513963600-afa31b458fec" # For pelican-cover-image


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
SLUGIFY_SOURCE = "title" # IGNORE_PAGE_SLUG will ignore this and make {slug} = path/to/page
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "news/{date:%Y}/{slug}/"
ARTICLE_SAVE_AS = "news/{date:%Y}/{slug}/index.html"
DRAFT_URL = "news/{date:%Y}/{slug}/"
DRAFT_SAVE_AS = "news/{date:%Y}/{slug}/index.html"
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
PAGINATED_DIRECT_TEMPLATES = ["index", "archives"]


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


# PRESENTATION

SITENAME = "TDWG" # Appears in navbar and html title
SITESUBTITLE = "Biodiversity Information Standards (TDWG) is a non-profit organization and "\
               "community dedicated to developing biodiversity information standards."
AUTHOR = "Biodiversity Information Standards (TDWG)"
DEFAULT_LANG = "en"
TIMEZONE = "UTC"
DEFAULT_DATE = "fs" # Use file date as default article date
DEFAULT_DATE_FORMAT = "%d %B %Y"
DEFAULT_PAGINATION = 10 # Applies to news page only, not supported for period archives
SUMMARY_MAX_LENGTH = 40 # For generated summary. Existence of manual summary checked by 
                        # plugin "summary"
GITHUB_URL = "https://github.com/tdwg"
TWITTER_USERNAME = "tdwg"
GOOGLE_ANALYTICS = ""


# NAVIGATON

# Pages are organized in a hierarchy, which is also reflected in their URL (see URL settings above).
# 
# To hide pages from navigation, add "status: hidden" to the metadata. Note that doing so 
# for a parent page, will make all its children top level pages!
# 
# Pages are ordered by their title (see PLUGIN SETTINGS). This can be overwritten by adding 
# "page_order: integer" to their metadata. The plugin "pelican-page-order" allows to set this only 
# where necessary (rather than on every page).

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [ # Links in footer. Format: title, SITEURL/path
    ["What is TDWG?", "about/"],
    ["Contact us", "about/contact/"],
    ["Privacy policy", "about/privacy/"]
]


# THEME SETTINGS

# The website uses a dedicated tdwg-theme (https://github.com/tdwg/tdwg-theme)
# Technically, it could be build with other themes, but won't look as good. Only the homepage 
# requires the non-default "home.html" template.

THEME = "../tdwg-theme"
DIRECT_TEMPLATES.append("search") # Add tipue-search page templage
THUMBOR_SERVICE = "https://api.gbif.org/v1/image"
PAGE_LINKS = { # Pages directly linked to by theme. Format: id: SITEURL/path
    "standards": "standards/", 
    "news": "news/",
    "search": "search.html"
}
SUBPAGES_MARKER = "<!-- subpages -->" # Used in content to indicate where subpages should appear
LICENSE_STATEMENT = "Content on this site, made open by <a href=\"http://www.tdwg.org\">"\
                    "Biodiversity Information Standards (TDWG)</a> is licensed under a "\
                    "<a href=\"https://creativecommons.org/licenses/by/4.0/\">"\
                    "Creative Commons Attribution 4.0 International License</a>."
