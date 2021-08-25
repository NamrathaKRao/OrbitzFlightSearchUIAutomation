from traceback import print_stack
import logging
import utilities.custome_logger as cl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)


    def __init__(self,driver):
        self.driver = driver


    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def GetElements(self,locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element



    def waitForElementNotToBePresent(self, locator, locatorType="id",
                               timeout=15, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.invisibility_of_element_located((byType, locator)))
            
            self.log.info("Element is not visible")
        except:
            self.log.info("Element is still visible")
            print_stack()
        return element

    def waitForElement(self, locator, locatorType="id",
                               timeout=15, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element "+locator+"")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            self.log.info("Element "+locator+" appeared on the web page")
        except:
            self.log.info("Element "+locator+" not appeared on the web page")
            print_stack()
        return element

    def ElementClick(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            self.log.info("Clicked on Element with Locator: " + locator + " LocatorType:" + locatorType)

        except:
            try:
                element = self.getElement(locator, locatorType)
                self.driver.execute_script("arguments[0].click();", element)
                self.log.info("Clicked on Element with Locator: " + locator + " LocatorType:" + locatorType + " using JavascriptExecutor")
            except:
                self.log.info("Could not click on Element with Locator: " + locator + " LocatorType:" + locatorType)




    def getText(self, locator="", locatorType="id", element=None, info="",attribute="innerText"):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                    text = element.get_attribute(attribute)

            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text


    def isElementPresent(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def isElementNotPresent(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            if element is None:
                self.log.info("Element not Present")
                return True
            else:
                self.log.info("Element present")
                return False
        except:
            self.log.info("Element not found")
            return False


    def sendKeys(self,data,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            element.send_keys(data)
            self.log.info("Sent data on Element with Locator: " + locator + " LocatorType:" + locatorType)
        except:
            self.log.info("Cannot send value to Locator: " + locator + " LocatorType:" + locatorType)
            print_stack()


    def MouseHoverOnElement(self,locator ,locatorType="id",element=None):
        #isPerform = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                hover = ActionChains(self.driver).move_to_element(element)
                isPerforme = hover.perform()
                self.log.info("Element is Enabled" + locator + "LocatorType:" +locatorType)
            else:
                self.log.info("Element not Enabled")
            #return isPerform
        except:
            print("Element not found")
            #return False

    def SwitchWindow(self,window_no):
        window_after = self.driver.window_handles[window_no]
        self.driver.switch_to_window(window_after)

    def VerifyExpected_and_Actual_Result(self,expected,actual):

         if(expected == actual):
            self.log.info("Expected result, " + expected + " is equal to actual result, " +actual)
            return True

         else:

            self.log.error("Expected Result, "+expected+" is not equal to actual result, "+actual)
            return False










