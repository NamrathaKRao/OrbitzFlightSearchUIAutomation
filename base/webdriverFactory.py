from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver


class WebDriverFactory():

    # def __init__(self, browser):
    #     self.browser = browser

    def getWebDriverInstance(self,browser,url):

        if browser == "firefox":
            # driver = webdriver.Firefox(GeckoDriverManager().install())
             driver = webdriver.Firefox(executable_path="drivers/geckodriver")


        elif browser == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())

        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())

        # setting driver implicit time out for an element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.delete_all_cookies()
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(url)
        return driver
