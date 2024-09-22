from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    close = (By.XPATH, "//span[@class='logSprite icClose']")
    trainIcon = (By.XPATH, "(//span[@class ='sc-1f95z5i-4 drxYQA']) [3]")

    def closeDialogBox(self):
        return self.driver.find_element(*HomePage.close)
        # driver.find_element(By.XPATH, "//span[@class='logSprite icClose']")

    def chooseTrainIcon(self):
        return self.driver.find_element(*HomePage.trainIcon)
        # self.driver.find_element(By.XPATH, "(//span[@class ='sc-1f95z5i-4 drxYQA']) [3]").click()

