# encoding: UTF-8
import unittest
from actionwords import Actionwords
from selenium import webdriver


class TestSeleniumTutorial(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(executable_path="/home/harut/Documents/chromedriver")
        self.actionwords = Actionwords(self, driver)

    def test_finding_a_site_on_google(self):
        self.actionwords.i_open(link="http://google.ru")
        self.actionwords.search_for(word="hiptest", css_id="lst-ib")
        self.actionwords.click_on_the_first_result('//*[@id="rso"]/div[1]/div/div/div/div/h3/a')

