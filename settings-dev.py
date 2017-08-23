#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file contains development environment settings.
# It will use (and overwrite) settings from settings.py.

import os
import sys
sys.path.append(os.curdir)
from settings import *

# TDWG servers are set to UTC
TIMEZONE = "UTC"

# Dependencies shouldn't be outside the Jenkins workspace
THEME = "tdwg-theme"
