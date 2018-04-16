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

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'

STATIC_PATHS = ['images', 'pdfs']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
USE_FOLDER_AS_CATEGORY = False
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
