from core.config.ConfigHelper import ConfigHelper
from selenium import webdriver

class FactoryDriver():

    __driver = None
    __config = ConfigHelper.getInstance()

    def createDriver(self):
        """
            This method creates an instance of WebDriver.
            This Webdriver is created with the settings that contain the file 'config.json'
            :param: WebDriver
        """

        if(self.__config.getBrowser() == "chrome"):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--lang=en")
            chrome_options.add_argument("--incognito")
            if (self.__config.getHeadlessMode()):
                chrome_options.add_argument("--headless")
            self.__driver = webdriver.Chrome(chrome_options)

        self.__driver.set_page_load_timeout(self.__config.getDefaultWait())
        self.__driver.implicitly_wait(self.__config.getDefaultWait())
        self.__driver.get(self.__config.getUrlApp())

        return self.__driver