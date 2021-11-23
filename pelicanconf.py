#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pablo Rodríguez-Sánchez'
SITENAME = 'PabRod'
SITEURL = 'https://pabrod.github.io'
SITESUBTITLE = 'Applied mathematician. Science storyteller'
# SITEDESCRIPTION = 'Flex - The minimalist Pelican theme.'
SITELOGO = '/images/profile.png'

FAVICON = '/images/favicon.ico'
THEME = "themes/flex"
BROWSER_COLOR = '#333333'
# Use Pygments for styling code chunks
# See gallery here: https://help.farbox.com/pygments.html
PYGMENTS_STYLE = 'emacs'

GOOGLE_ANALYTICS = 'UA-118019878-1'
DISQUS_SITENAME = 'pabrod'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git', 'README.md']

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']
# PAGE_PATHS =
# ARTICLE_PATHS =

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Extract metadata from filename
# FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# Maximum length of automatic summaries
SUMMARY_MAX_LENGTH = 25 # Only used if summary is not specified

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/all-{lang}.atom.xml'
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = 'feeds/tag-{slug}.atom.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False # Maybe change this after deciding folder structure
MAIN_MENU = True
HOME_HIDE_TAGS = True

#MENUITEMS = (
#    ('Blog', 'https://pabrod.github.io'),
#)

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
    ('linkedin', 'https://www.linkedin.com/in/pabrod'),
    ('rss', SITEURL + '/pages/feeds-list-en.html')
)

DEFAULT_PAGINATION = 10
