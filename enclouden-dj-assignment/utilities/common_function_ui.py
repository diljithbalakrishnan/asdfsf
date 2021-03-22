from utilities import driver

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, TimeoutException
from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException
from polling import TimeoutException, poll
import time


def timer(func):
    """
    Execution Timer for functions - Being used as a decorator
    :param func:
    :return executed time:
    """

    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        returnValue = func(*args, **kwargs)
        end_ts = time.time()
        millis = end_ts - beg_ts
        # print('%s() - Function Took %0.3f secs' % (func.func_name, (millis * 1000.0) / 1000))
        return returnValue

    return wrapper


def getElementByXPath(selector):
    """
    Get the element from XPath
    :param selector:
    :return boolean:
    """
    try:
        element = driver.Instance.find_element_by_xpath(selector)
        return element
    except NoSuchElementException:
        return False

@timer
def getUrl(url):
    """
    Hits the URL
    :param url:
    :return:
    """
    driver.Instance.get(url)

@timer
def waitForPageLoad():
    """
    Waits till the web page returns 'complete' status for document.readyState
    :return: page_state
    """

    try:
        page_state = driver.Instance.execute_script('return document.readyState;')
        poll(lambda: page_state == 'complete', timeout=20, step=1)
        return page_state
    except TimeoutException:
        return TimeoutError

@timer
def isElementDisplayedByXPath(selector):
    """
    Checks if the element is Displayed
    :param selector:
    :return boolean:
    """

    try:
        getElementByXPath(selector).is_displayed()
        return True
    except ElementNotVisibleException:
        return False

@timer
def clickByXPath(selector):
    """
    Clicks on a element
    :param selector:
    :return boolean:
    """

    try:
        button = getElementByXPath(selector)
        button.click()
        return True
    except ElementNotInteractableException:
        return False
    except StaleElementReferenceException:
        return False
    except NoSuchElementException:
        return False

@timer
def returnText(selector):
    """
    Returns Text on passing a selector
    :param selector:
    :return: Text
    """
    try:
        element = getElementByXPath(selector)
        return element.text
    except NoSuchElementException:
        raise Exception('Never saw %s' % selector)
