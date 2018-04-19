#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pablo Rodríguez-Sánchez'
SITENAME = 'PabRod'
SITEURL = 'https://pabrod.github.io'
SITESUBTITLE = 'Physicist. PhD Student. Science journalist'
# SITEDESCRIPTION = 'Flex - The minimalist Pelican theme.'
# SITELOGO = ''

FAVICON = '/images/favicon.ico'
THEME = "themes/flex"
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

DELETE_OUTPUT_DIRECTORY = False

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
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/all-%s.atom.xml'
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False # Maybe change this after deciding folder structure
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
    ('instagram', 'https://instagram.com/pablo.rodriguez.sanchez/'),
    ('linkedin', 'https://www.linkedin.com/in/pablo-rodríguez-sánchez-40672658'),
    ('rss', SITEURL + '/pages/feeds-list-English.html')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
