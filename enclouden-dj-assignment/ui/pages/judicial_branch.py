from config import url,locators, variables
from utilities import common_function_ui


class JudicialBranch:

    @staticmethod
    def go_to_url():

        common_function_ui.waitForPageLoad()
        # Authenticate the App
        common_function_ui.getUrl(url.JUDICIAL_URL)

    @staticmethod
    def check_header():
        common_function_ui.isElementDisplayedByXPath(locators.JUDICIAL_HEADER_XPATH)

    @staticmethod
    def check_country_name():
        common_function_ui.waitForPageLoad()
        country_name = locators.COUNTRY_NAMES.replace('COUNTRY_NAME', variables.COUNTRY_NAME)
        common_function_ui.isElementDisplayedByXPathlocators.COUNTRY(country_name)
        name_text = common_function_ui.returnText(country_name)
        name_text = str(name_text).strip().upper()
        assert variables.COUNTRY_NAME == name_text, "Not Displaying Country Name"

    @staticmethod
    def verify_notice_flow():
        """
        View Notice Flow
        """
        common_function_ui.waitForPageLoad()
        country_name = locators.COUNTRY_NAMES.replace('COUNTRY_NAME', variables.COUNTRY_NAME)
        common_function_ui.clickByXPath(country_name)
        common_function_ui.clickByXPath(locators.VIEW_FULL_NOTICE_XPATH)
        name_text = common_function_ui.returnText(locators.NOTICE_FLOW_CHECK_XPATH)
        assert variables.NOTICE_FLOW == name_text, "Page is not navigated to Notice page"



    @staticmethod
    def verify_back_flow():
        """
        Verify that the user is able to click the link and check it is navigating to previous page

        """
        common_function_ui.waitForPageLoad()
        common_function_ui.clickByXPath(locators.COUNTRY_BACK_FLOW)
        common_function_ui.isElementDisplayedByXPath(locators.JUDICIAL_HEADER_XPATH)