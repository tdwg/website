#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file contains production environment settings.
# It will use (and overwrite) settings from settings.py.

import os
import sys
sys.path.append(os.curdir)
from settings import *

SITEURL = "https://www.tdwg.org"
THEME = "tdwg-theme" # Directory in the Jenkins workspace

# EXTERNAL SERVICES
DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-122881526-1"
