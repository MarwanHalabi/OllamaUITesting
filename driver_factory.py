import os, tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class DriverFactory:
    def __init__(self):
        self.browser = os.getenv('BROWSER', 'chrome').lower()
        self.width = int(os.getenv('SCREEN_WIDTH', '1920'))
        self.height = int(os.getenv('SCREEN_HEIGHT', '1080'))
        self.headless = os.getenv('HEADLESS', 'false').lower() in ('1','true','yes')

    def create_driver(self):
        if self.browser == 'chrome':
            return self._create_chrome_driver()
        elif self.browser == 'firefox':
            return self._create_firefox_driver()
        raise ValueError(f"Unsupported browser: {self.browser}")

    def _create_chrome_driver(self):
        opts = ChromeOptions()
        if self.headless:
            opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
        opts.add_argument(f"--window-size={self.width},{self.height}")
        opts.add_argument("--remote-debugging-port=0")  # avoid conflicts
        opts.set_capability("pageLoadStrategy", "eager")

        d = webdriver.Chrome(options=opts)
        d.set_page_load_timeout(30)
        d.set_script_timeout(30)
        return d

    def _create_firefox_driver(self):
        opts = FirefoxOptions()
        if self.headless:
            opts.add_argument("--headless")
        opts.set_preference("network.http.referer.spoofSource", False)
        d = webdriver.Firefox(options=opts)
        d.set_window_size(self.width, self.height)
        d.set_page_load_timeout(30)
        d.set_script_timeout(30)
        return d

def get_driver():
    return DriverFactory().create_driver()
