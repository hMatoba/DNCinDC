import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

HOST = "http://webapp"

class BrowserTests(unittest.TestCase):
    """tests for main five functions."""

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor = 'http://127.0.0.1:8889/wd/hub',
            desired_capabilities = DesiredCapabilities.CHROME
        )
        self.driver.implicitly_wait(10)

    def test_top(self):
        """top page"""
        self.driver.get(HOST + "/")
        self.assertIn("Home Page", self.driver.title)



def suite():
    """run tests"""
    suite = unittest.TestSuite()
    suite.addTests([unittest.makeSuite(BrowserTests),
                    ])
    return suite


if __name__ == '__main__':
    unittest.main()