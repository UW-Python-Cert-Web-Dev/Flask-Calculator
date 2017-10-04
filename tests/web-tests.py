import unittest
from selenium import webdriver


class WebTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def getTotal(self):
        return int(self.browser.find_element_by_css_selector('#total').text())

    def testPageTitle(self):
        self.browser.get('http://localhost:5000/all')
        self.assertIn('Calculator', self.browser.title)

    def testCalculate(self):
        self.browser.get('http://localhost:5000/add')

        # The total should be zero
        self.assertEqual(0, self.getTotal())

        # Add the number 5
        self.browser.find_element_by_css_selector('input[name="name"]').send_keys("5")
        self.browser.find_element_by_css_selector('input[type="submit"]').click()

        # We are brought back to the add page
        self.assertIn("/add", self.browser.current_url)

        # The total is now 5
        self.assertEqual(5, self.getTotal())

        # Add the number 10
        self.browser.find_element_by_css_selector('input[name="name"]').send_keys("10")
        self.browser.find_element_by_css_selector('input[type="submit"]').click()

        # We are brought back to the add page
        self.assertIn("/add", self.browser.current_url)

        # The total is now 15
        self.assertEqual(15, self.getTotal())
