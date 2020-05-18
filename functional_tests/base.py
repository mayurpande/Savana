from django.test import LiveServerTestCase
from selenium import webdriver


class Base(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
