from io import SEEK_CUR
from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator

from ....TestsHelpers.Service.helper import Helper 
from ....TestsHelpers.Service.comparator import SiteResponse as Comaprator
from ....TestsHelpers.Service.validator import SiteResponse as Validator
from ....TestsHelpers.Service import constants

from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomUUID4, randomWord

class TestPostSite(TestCase):
    
    def setUp(self):
        self.createCompanyData = defaultDataCreator.Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.companyID = Helper().createCompany(self.createCompanyData).json()[constants.companyID]

        self.createSiteData = defaultDataCreator.Site()
        self.createSiteData[constants.companyID] = self.companyID
        self.siteID = None

    def testPostSite(self):
        """Post Site"""
        print(self.createSiteData)
        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.CREATED)


        testing = createSiteResponse.json()
        # expected = self.createSiteData

        self.siteID = testing[constants.siteID]

    def tearDown(self):
        Helper().deleteCompany(self.companyID)
        Helper().deleteSite(self.siteID)