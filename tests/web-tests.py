import unittest
from selenium import webdriver


class WebTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://localhost:5000/all')
        self.assertIn('Calculator', self.browser.title)

