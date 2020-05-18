from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class Base(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
