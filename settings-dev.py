#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file contains development environment settings.
# It will use (and overwrite) settings from settings.py.

import os
import sys
sys.path.append(os.curdir)
from settings import *

SITEURL = "https://www.tdwg.org"
THEME = "tdwg-theme" # Dependencies shouldn't be outside the Jenkins workspace
