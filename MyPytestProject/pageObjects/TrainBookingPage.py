from selenium.webdriver.common.by import By


class TrainBooking:
    def __init__(self, driver):
        self.driver = driver

    sourceBox = (By.XPATH, "//p[text()='Enter Source Name']")
    sourceName = (By.XPATH, "//input[contains(@type,'text')]")
    sourceList = (By.XPATH, "//li[@class='styles_FswAutoCompItem__RE1dP']")
    destinationBox = (By.XPATH, "//p[text()='Enter Destination Name']")
    destinationName = (By.XPATH, "//input[contains(@type,'text')]")
    destinationList = (By.XPATH, "//li[@class='styles_FswAutoCompItem__RE1dP']")
    tomorrow = (By.XPATH, "//button/div[1]/span[text()='Tomorrow']")
    searchButton = (By.XPATH, "//div/span[text()='SEARCH TRAINS']")

    def clickSourceBox(self):
        return self.driver.find_element(*TrainBooking.sourceBox)
        # self.driver.find_element(By.XPATH, "//p[text()='Enter Source Name']").click()

    def enterSourceName(self):
        return self.driver.find_element(*TrainBooking.sourceName)
        # self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]").send_keys("bengaluru")

    def getSouceList(self):
        return self.driver.find_elements(*TrainBooking.sourceList)
        # sourceStations = self.driver.find_elements(By.XPATH, "//li[@class='styles_FswAutoCompItem__RE1dP']")

    def clickDestinationBox(self):
        return self.driver.find_element(*TrainBooking.destinationBox)
        # self.driver.find_element(By.XPATH, "//p[text()='Enter Destination Name']").click()  # //p[normalize-space()='Enter Destination Name']

    def enterDestinationName(self):
        return self.driver.find_element(*TrainBooking.destinationName)
        # self.driver.find_element(By.XPATH, "//input[contains(@type,'text')]").send_keys("hyderabad")

    def getDestinationList(self):
        return self.driver.find_elements(*TrainBooking.destinationList)
        # destinationStations = self.driver.find_elements(By.XPATH, "//li[@class='styles_FswAutoCompItem__RE1dP']")

    def clickTomorrow(self):
        return self.driver.find_element(*TrainBooking.tomorrow)
        # self.driver.find_element(By.XPATH, "//button/div[1]/span[text()='Tomorrow']").click()

    def clickSearchButton(self):
        return self.driver.find_element(*TrainBooking.searchButton)
        # self.driver.find_element(By.XPATH, "//div/span[text()='SEARCH TRAINS']").click()
