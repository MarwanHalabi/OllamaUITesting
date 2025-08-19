import os
import unittest
from selenium import webdriver
import allure
from allure import severity_level
from driver_factory import get_driver

OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://54.247.216.178:3000')  # Default to localhost if not set

class ExampleTestCase(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(OLLAMA_URL)

    def tearDown(self):
        self.driver.quit()

    @allure.title("Test home endpoint")
    @allure.description("Description............")
    @allure.severity(severity_level.CRITICAL)
    @allure.label("owner", "API Team")
    @allure.link("https://dev.example.com/", name="Website")
    @allure.issue("AUTH-123")
    @allure.testcase("TMS-456")
    def test_page_title(self):
        self.assertIn('Ollama UI', self.driver.title)

if __name__ == '__main__':
    unittest.main() 