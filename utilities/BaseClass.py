import inspect
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging


@pytest.mark.usefixtures("browserSetup")
class BaseClass:

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler("../logs/logfile.log")
        Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(Formatter)
        logger.addHandler(fileHandler)  # Passing File handler object in this

        logger.setLevel(logging.INFO)

        return logger

    def CreateWebDriverWaitObject(self, time):
        explicitWait = WebDriverWait(self.driver, time)
        return explicitWait

    def ExplicitWaitForAllPageElements(self, time):
        explicitWait = self.CreateWebDriverWaitObject(time)
        explicitWait.until(expected_conditions.visibility_of_all_elements_located)

    def ExplicitWaitUntilElementPresence(self, element, time):
        explicitWait = self.CreateWebDriverWaitObject(time)
        explicitWait.until(
            expected_conditions.presence_of_element_located(element))



