# encoding: UTF-8
import unittest
from actionwords import Actionwords
from selenium import webdriver


class TestTutorial(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(executable_path="/home/harut/Documents/chromedriver")
        self.actionwords = Actionwords(self, driver)

    def test_open_a_website(self):
        self.actionwords.i_open(url="http://google.ru")
