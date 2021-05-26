from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator

from ....TestsHelpers.Service.helper import Helper 
from ....TestsHelpers.Service.comparator import SiteResponse as Comaprator
from ....TestsHelpers.Service.validator import SiteResponse as Validator
from ....TestsHelpers.Service import constants

from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomNumber, randomUUID4, randomWord

class TestPostSite(TestCase):
    
    def setUp(self):
        self.createCompanyData = defaultDataCreator.Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.companyID = Helper().createCompany(self.createCompanyData).json()[constants.companyID]

        self.createSiteData = defaultDataCreator.Site()
        self.createSiteData[constants.companyID] = self.companyID
        self.createSiteResponse = Helper().createSite(self.createSiteData).json()
        self.siteID = self.createSiteResponse[constants.siteID]

    def testDeleteSite(self):
        """Delete Site"""
        deleteCompanyResponse = Helper().deleteSite(self.siteID)
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.NO_CONTENT)

    def testDeleteSiteAlreadyDeleted(self):
        """Delete Site. Already Deleted Site"""
        deleteCompanyResponse = Helper().deleteSite(self.siteID)
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.NO_CONTENT)
        deleteCompanyResponse = Helper().deleteSite(self.siteID)
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteSiteDoesNotExist(self):
        """Delete Site. Non-Existing Site"""
        deleteCompanyResponse = Helper().deleteSite(siteID = randomUUID4())
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteSiteWithEmptyId(self):
        """Delete Site. Empty Site Id"""
        deleteCompanyResponse = Helper().deleteSite(siteID = '')
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def testDeleteSiteIdAsStirng(self):
        """Delete Site. Site Id Is String Type"""
        deleteCompanyResponse = Helper().deleteSite(siteID = randomWord(17))
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteSiteIdAsInt(self):
        """Delete Site. Site Id Is Integer Type"""
        deleteCompanyResponse = Helper().deleteSite(siteID = randomNumber(1,100))
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteSiteIdAsBool(self):
        """Delete Site. Site Id Is Boolen Type"""
        deleteCompanyResponse = Helper().deleteSite(siteID = True)
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteSiteIdAsArray(self):
        """Delete Site. Site Id Is Array Type"""
        deleteCompanyResponse = Helper().deleteSite(siteID = ["Ania"])
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteSiteIdAsDict(self):
        """Delete Site. Site Id Is Dictionary Type"""
        deleteCompanyResponse = Helper().deleteSite(siteID = {"Ania": "10"})
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        Helper().deleteCompany(self.companyID)
        Helper().deleteSite(self.siteID)