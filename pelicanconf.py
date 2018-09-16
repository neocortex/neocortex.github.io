#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# AUTHOR = 'Rafael Schultze-Kraft'
SITENAME = 'Rafael Schultze-Kraft'
SITEURL = ''
SUMMARY = 'Ex-neuroscientist, data and machine learning enthusiast, Python aficionado.'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

CSS_FILE = 'custom.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

IPYNB_USE_META_SUMMARY = True
IPYNB_IGNORE_CSS = False

DEFAULT_CATEGORY = 'misc'
# DISPLAY_PAGES_ON_MENU = True
# DISPLAY_CATEGORIES_ON_MENU = True

OUTPUT_PATH = 'output/'
THEME = '/Users/rafael/basic'
MENUITEMS = (('cv', 'resume.pdf'),
             ('email', 'mailto:skraftr@gmail.com'),
             ('linkedin', 'https://de.linkedin.com/in/rafael-schultze-kraft-9a044b93'),
             ('github', 'http://github.com/neocortex'))

LOAD_CONTENT_CACHE = False

# cname config
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

RELATIVE_URLS = True
