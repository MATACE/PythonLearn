#!/usr/bin/python
# coding=utf-8

import logging
import webbrowser
import requests
import bs4

class WebOp():
    def __init__(self):
        pass
    
    def open_url(self, url):
        logging.info("Open url: " + url)
        webbrowser.open(url)
    
    def download(self, url):
        """ Download file from the web

        Args:
            url (string): The download file in the web
        """

        ret = requests.get(url)
        print(len(ret.text))
        print(ret.text[:256])
    
    def get_web_element(sef, url):
        ret = requests.get(url)
        try:
            ret.raise_for_status()
        except Exception as exc:
            print('There was a problem: %s' % (exc))
        get_soup = bs4.BeautifulSoup(ret.text)
        type(get_soup)