import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:3000')

class ChatFlowTestCase(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-web-security")
        options.add_argument("--user-data-dir=/tmp/ollama-profile")
        # options.add_argument("--headless")  # optional

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(OLLAMA_URL)

    def tearDown(self):
        self.driver.quit()

    def test_chat_flow(self):
        driver = self.driver

        # Open model dropdown
        model_selector = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))
        )
        model_selector.click()

        model_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'gemma3')]"))
        )
        model_option.click()


        chat_input = self.driver.find_element(By.NAME, "message")
        chat_input.clear()

        # Type character by character to trigger frontend events
        for char in "Hello, Ollama!":
            chat_input.send_keys(char)
            time.sleep(0.05)  # simulate natural typing

        chat_input.send_keys(Keys.ENTER)

        # Wait briefly for message to be processed
        time.sleep(1)

        # Optional: Click the send button
        # First locate the chat bottombar container
        chat_bottombar = self.driver.find_element(By.TAG_NAME, "form")

        # Then, within the bottombar, locate the send button
        send_button = chat_bottombar.find_element(By.CSS_SELECTOR, "button[type='submit']")
        send_button.click()

        # Wait briefly for message to be processed
        time.sleep(1)

        # Check input is empty
        chat_input = self.driver.find_element(By.NAME, "message")
        self.assertEqual(chat_input.get_attribute("value"), "")

if __name__ == '__main__':
    unittest.main()
