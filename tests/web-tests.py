import unittest
from selenium import webdriver


class WebTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://localhost:5000/all')
        self.assertIn('My Todo List', self.browser.title)

    def testLogin(self):
        self.browser.get('http://localhost:5000/all')

        # Logout just incase
        self.browser.get('http://localhost:5000/logout')

        # Login button exists
        self.assertIsNotNone(self.browser.find_element_by_css_selector('a[href="/login"]'))

        # Click the login button
        self.browser.find_element_by_css_selector('a[href="/login"]').click()

        # Use the login form
        self.browser.find_element_by_css_selector('input[name="name"]').send_keys("admin")
        self.browser.find_element_by_css_selector('input[name="password"]').send_keys("password")
        self.browser.find_element_by_css_selector('input[type="submit"]').click()

        # We have successfully logged in and are at the "all tasks" page
        self.assertIn("/all", self.browser.current_url)
