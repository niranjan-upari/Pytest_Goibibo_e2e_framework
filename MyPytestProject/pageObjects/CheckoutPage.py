from selenium.webdriver.common.by import By


class CheckOut:
    def __init__(self, driver):
        self.driver = driver

    IRCTC_UserName = (By.XPATH, "//input[@id='IRCTC_Username']")
    IRCTC_UserNameValidate = (By.XPATH, "//button[@class='AppButton_btnStyle__HmavT styles_mainCnt__vldtBtn__UeBKE rubik400 ']")
    click_add_new_traveller_button = (By.XPATH, "//button/p[text()='ADD NEW TRAVELLER']")
    traveller_name = (By.CSS_SELECTOR, "div input[id='user_name']")
    age = (By.ID, "user_age")
    food = (By.XPATH, "//label/p[text()='Veg']")
    save = (By.XPATH, "//div/button/p[text()='Save']")
    contactNo = (By.ID, "contact_no")
    payment_button = (By.XPATH, "//div/button/p[text()='Proceed to Payment']")
    refund_option = (By.XPATH, "(//label[@for='getRefund_yes']) [p]")
    insurance_option = (By.XPATH, "(//label/p[@class='font18 lineHight21 blackText2 fontW400 rubik400'])[1]")

    def getIRCTC_UserName(self):
        return self.driver.find_element(*CheckOut.IRCTC_UserName)
        # self.driver.find_element(By.XPATH, "//input[@id='IRCTC_Username']").send_keys("nupari")

    def getIRCTC_UserNameValidation(self):
        return self.driver.find_element(*CheckOut.IRCTC_UserNameValidate)
        # self.driver.find_element(By.XPATH, "//button[@class='AppButton_btnStyle__HmavT styles_mainCnt__vldtBtn__UeBKE rubik400 ']").click()

    def get_add_new_traveller_button(self):
        return self.driver.find_element(*CheckOut.click_add_new_traveller_button)
        # self.driver.find_element(By.XPATH, "//button/p[text()='ADD NEW TRAVELLER']").click()

    def get_Traveller_name(self):
        return self.driver.find_element(*CheckOut.traveller_name)
        # self.driver.find_element(By.CSS_SELECTOR, "div input[id='user_name']").send_keys("Niranjan")

    def get_traveller_age(self):
        return self.driver.find_element(*CheckOut.age)
        # self.driver.find_element(By.ID, "user_age").send_keys("25")

    def select_food(self):
        return self.driver.find_element(*CheckOut.food)
        # self.driver.find_element(By.XPATH, "//label/p[text()='Veg']").click()

    def click_save_button(self):
        return self.driver.find_element(*CheckOut.save)
        # self.driver.find_element(By.XPATH, "//div/button/p[text()='Save']").click()

    def traveller_contact_no(self):
        return self.driver.find_element(*CheckOut.contactNo)
        # self.driver.find_element(By.ID, "contact_no").send_keys("1234567890")

    def click_payment_button(self):
        return self.driver.find_element(*CheckOut.payment_button)
        # self.driver.find_element(By.XPATH, "//div/button/p[text()='Proceed to Payment']").click()

    def click_refund_option(self):
        return self.driver.find_element(*CheckOut.refund_option)
        # actions.move_to_element(self.driver.find_element(By.XPATH, "(//label[@for='getRefund_yes']) [p]")).click().perform()

    def click_insurance_option(self):
        return self.driver.find_element(*CheckOut.insurance_option)
        # actions.move_to_element(self.driver.find_element(By.XPATH, "(//label/p[@class='font18 lineHight21 blackText2 fontW400 rubik400'])[1]")).click().perform()
