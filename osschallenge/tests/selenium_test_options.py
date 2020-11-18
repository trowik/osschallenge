from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(self):
        super(SeleniumTests, self).setUpClass()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('no-sandbox')
        options.add_argument('window-size=1200x600')
        self.driver = webdriver.Chrome(chrome_options=options, ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
