#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pablo Rodríguez-Sánchez'
SITENAME = 'PabRod'
SITEURL = ''
SITESUBTITLE = 'Physicist. PhD Student. Science journalist'
# SITEDESCRIPTION = 'Flex - The minimalist Pelican theme.'
# SITELOGO = ''
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']
# PAGE_PATHS =
# ARTICLE_PATHS =

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'

# Extract metadata from filename
# FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# Maximum length of automatic summaries
SUMMARY_MAX_LENGTH = 25 # Only used if summary is not specified

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
USE_FOLDER_AS_CATEGORY = False # Maybe change this after deciding folder structure
DISPLAY_PAGES_ON_MENU = True
MAIN_MENU = True
HOME_HIDE_TAGS = True

MENUITEMS = (
    ('Blog', 'http://fuga.naukas.com/'),
)

# Blogroll
# LINKS = (
#    ('Fuga de cerebros', 'http://fuga.naukas.com/'),
#)

# Social widget
SOCIAL = (
    ('envelope-o', 'mailto:pablo.rodriguez.sanchez@gmail.com'),
    ('github', 'https://github.com/PabRod'),
    ('twitter', 'http://twitter.com/DonMostrenco'),
    ('linkedin', 'https://www.linkedin.com/in/pablo-rodríguez-sánchez-40672658')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
