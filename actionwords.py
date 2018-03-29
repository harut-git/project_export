# encoding: UTF-8


class Actionwords:
    def __init__(self, test, driver):
        self.test = test
        self.driver = driver

    def i_open(self, link=""):
        self.driver.get(link)

    def search_for(self, word="", css_id =""):
        self.driver.find_element_by_id(css_id).send_keys(word)
        self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click()

    def click_on_the_first_result(self, object=""):
        self.driver.find_element_by_xpath(object).click()
