import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOut
from pageObjects.HomePage import HomePage
from pageObjects.TrainBookingPage import TrainBooking
from pageObjects.TrainSelectionPage import TrainSelection
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestGoibiboWebsite(BaseClass):

    def test_e2e(self):

        # Page Objects of HomePage
        homePage = HomePage(self.driver)
        homePage.closeDialogBox().click()
        homePage.chooseTrainIcon().click()

        # Page Objects of TrainBookingPage
        trainBooking = TrainBooking(self.driver)
        trainBooking.clickSourceBox().click()
        trainBooking.enterSourceName().send_keys("bengaluru")

        sourceStations = trainBooking.getSouceList()
        print("Source Stations Length")
        print(len(sourceStations))
        for sourceStation in sourceStations:
            if "SBC" in sourceStation.text:
                sourceStation.click()
                break

        trainBooking.clickDestinationBox().click()
        trainBooking.enterDestinationName().send_keys("hyderabad")

        destinationStations = trainBooking.getDestinationList()
        print("Destination Stations Length")
        print(len(destinationStations))
        for destinationStation in destinationStations:
            if "Secunderabad" in destinationStation.text:
                destinationStation.click()
                break

        trainBooking.clickTomorrow().click()
        trainBooking.clickSearchButton().click()

        # Page Objects of TrainSelectionPage
        trainWhichIsSelected = TrainSelection(self.driver)
        trainWhichIsSelected.getSelectedTrain().click()

        # Page Objects of CheckoutPage
        checkOutPage = CheckOut(self.driver)
        checkOutPage.getIRCTC_UserName().send_keys("nupari")
        checkOutPage.getIRCTC_UserNameValidation().click()
        checkOutPage.get_add_new_traveller_button().click()

        checkOutPage.get_Traveller_name().send_keys("Niranjan")
        checkOutPage.get_traveller_age().send_keys("25")
        checkOutPage.select_food().click()
        checkOutPage.click_save_button().click()

        time.sleep(5)
        actions = ActionChains(self.driver)
        actions.move_to_element(checkOutPage.click_refund_option()).click().perform()
        # actions.move_to_element(self.driver.find_element(By.XPATH, "(//label[@for='getRefund_yes']) [p]")).click().perform()
        # actions.move_to_element(self.driver.find_element(By.XPATH, "(//label[@for='goCnfrm_yes'])[p]")).click().perform()
        # above were used, when webelements got changed
        checkOutPage.traveller_contact_no().send_keys("1234567890")
        actions.move_to_element(checkOutPage.click_insurance_option()).click().perform()
        # actions.move_to_element(self.driver.find_element(By.XPATH, "(//label/p[@class='font18 lineHight21 blackText2 fontW400 rubik400'])[1]")).click().perform()
        self.driver.find_element(By.XPATH, "//label[@for='apply_accIns']").click()

        checkOutPage.click_payment_button().click()
        time.sleep(10)
