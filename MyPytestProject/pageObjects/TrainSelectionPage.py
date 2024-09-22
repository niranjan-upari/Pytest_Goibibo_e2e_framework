from selenium.webdriver.common.by import By


class TrainSelection:
    def __init__(self, driver):
        self.driver = driver

    selectTrain = (By.XPATH, "//div[3]/div[3]/ul[1]/li[4]/div[1]")

    def getSelectedTrain(self):
        return self.driver.find_element(*TrainSelection.selectTrain)
        # self.driver.find_element(By.XPATH, "//div[3]/div[3]/ul[1]/li[4]/div[1]").click()
