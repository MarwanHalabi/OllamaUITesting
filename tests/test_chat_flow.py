import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_factory import get_driver
import requests

OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:3000')

class ChatFlowTestCase(unittest.TestCase):

    def setUp(self):
        try:
            requests.get(OLLAMA_URL, timeout=5)
        except Exception as e:
            self.fail(f"Server not reachable at {OLLAMA_URL}: {e}")
        self.driver = get_driver()
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
