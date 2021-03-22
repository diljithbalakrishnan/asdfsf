import unittest
from utilities import driver
from ui.pages.judicial_branch import JudicialBranch
import pytest


class JudicialBranchTest(unittest.TestCase):

    def setUp(self):
        driver.initialize()
        self.jb = JudicialBranch()

    @pytest.mark.judicialbranch
    def test_judicial(self):

        # Check Header
        self.jb.check_header()

    @pytest.mark.countryname
    def test_country_name(self):

        # Check Country Name
        self.jb.check_country_name()

    @pytest.mark.noticeflow
    def test_notice_flow(self):

        # Verify the Notice flow
        self.jb.verify_notice_flow()

        # Verify the Back flow
        self.jb.verify_back_flow()


    def tearDown(self):
        driver.quitting()
