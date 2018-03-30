# encoding: UTF-8


class Actionwords:
    def __init__(self, test, driver):
        self.test = test
        self.driver = driver

    def i_open(self, url=""):
        self.driver.get(url)
