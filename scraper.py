#!/usr/bin/env python                                                                                                                                                                
import os
import sys
import django

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), 'scraper/')))
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), 'scraper/scraper/')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()

from django.core.exceptions import ObjectDoesNotExist
from scrap.models import *

class CustomScraper(object):
    def __init__(self):
        self.url = ""

    def scrape(self):
        print 'scraping...'

if __name__ == '__main__':
    scraper = CustomScraper()
    scraper.scrape()
