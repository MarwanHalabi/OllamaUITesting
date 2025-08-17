import os
import unittest
from selenium import webdriver
from driver_factory import get_driver

OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:3000')  # Default to localhost if not set

class ExampleTestCase(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(OLLAMA_URL)

    def tearDown(self):
        self.driver.quit()

    def test_page_title(self):
        self.assertIn('Ollama UI', self.driver.title)

if __name__ == '__main__':
    unittest.main() 