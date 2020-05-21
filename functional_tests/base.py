from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from pathlib import Path
import os


class Base(StaticLiveServerTestCase):

    def setUp(self):
        self.fp = webdriver.FirefoxProfile()
        self.fp.set_preference("browser.download.folderList", 2)
        path = Path(os.environ['HOME'])
        self.fp.set_preference("browser.download.manager.showWhenStarting", False)
        self.fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/json")
        self.fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")
        self.browser = webdriver.Firefox(firefox_profile=self.fp)

    def tearDown(self):
        self.browser.quit()
