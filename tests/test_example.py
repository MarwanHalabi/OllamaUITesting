import os
import unittest
from selenium import webdriver

OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:3000')  # Default to localhost if not set

class ExampleTestCase(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_page_title(self):
        self.driver.get(OLLAMA_URL)
        self.assertIn('Ollama UI', self.driver.title)

if __name__ == '__main__':
    unittest.main() 