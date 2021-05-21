from unittest import TestCase
from http import HTTPStatus

from requests.api import delete

from ....TestsHelpers.Service import defaultDataCreator

from ....TestsHelpers.Service.helper import Helper 
from ....TestsHelpers.Service.comparator import SiteResponse as Comaprator
from ....TestsHelpers.Service.validator import SiteResponse as Validator
from ....TestsHelpers.Service import constants

from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomNumber, randomUUID4, randomWord

class TestSite(TestCase):
    
    def setUp(self):
        self.createCompanyData = defaultDataCreator.Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.companyID = Helper().createCompany(self.createCompanyData).json()[constants.companyID]

        self.createSiteData = defaultDataCreator.Site()
        self.createSiteData[constants.companyID] = self.companyID
        self.createSiteResponse = Helper().createSite(self.createSiteData).json()
        self.siteID = self.createSiteResponse[constants.siteID]

    def testGetSite(self):
        """Get Site"""
        getSiteResponse = Helper().getSite(self.siteID)
        compareStatusCodes(self, getSiteResponse.status_code, HTTPStatus.OK)

        testing = getSiteResponse.json()
        expected = self.createSiteResponse

        Validator(self, testing)\
            .companyID()\
            .name()\
            .address()\
                .street()\
                .city()\
                .postalCode()\
                .country()\
                .back()\
            .pricing()\
                .numberOfMinutes()\
                .price()\
                .back()

        Comaprator(self, testing, expected)\
            .companyID()\
            .name()\
            .address()\
                .street()\
                .city()\
                .postalCode()\
                .country()\
                .back()\
            .pricing()\
                .numberOfMinutes()\
                .price()\
                .currency()\
                .back()

    def testGetSiteNonExistingCompany(self):
        """Get Site. Non Existing Site"""
        getSiteResponse = Helper().getSite(siteID = randomUUID4())
        compareStatusCodes(self, getSiteResponse.status_code, HTTPStatus.NOT_FOUND)

    def testGetSiteDeleted(self):
        """Get Site. Site Has Been Deleted"""
        Helper().deleteSite(self.siteID)
        getSiteResponse = Helper().getSite(self.siteID)
        compareStatusCodes(self, getSiteResponse.status_code, HTTPStatus.NOT_FOUND)

    def testGetSiteIdEmpty(self):
        """Get Site. Site Id Is Empty"""
        getSiteResponse = Helper().getSite(siteID = '')
        compareStatusCodes(self, getSiteResponse.status_code, HTTPStatus.OK)

    def testGetNoSiteId(self):
        """Get Site. No Site Id Given"""
        getSiteResponse = Helper().getSite(siteID = None)
        compareStatusCodes(self, getSiteResponse.status_code, HTTPStatus.OK)


    def testGetSiteIdAsString(self):
        """Get Site. Site Id Is String Type"""
        getSiteResponse = Helper().getSite(siteID = randomWord(17))
        compareStatusCodes(self, getSiteResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetSiteIdAsInt(self):
        """Get Site. Site Id Is Integer Type"""
        getSiteResponse = Helper().getSite(siteID = randomNumber(1, 100))
        compareStatusCodes(self, getSiteResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetSiteIdAsBoolen(self):
        """Get Site. Site Id Is Boolen Type"""
        getSiteResponse = Helper().getSite(siteID = True)
        compareStatusCodes(self, getSiteResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetSiteIdAsArray(self):
        """Get Site. Site Id Is Array Type"""
        getSiteResponse = Helper().getSite(siteID = ["Ania"])
        compareStatusCodes(self, getSiteResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetSiteIdAsDict(self):
        """Get Site. Site Id Is Dictionary Type"""
        getSiteResponse = Helper().getSite(siteID = {"Ania": "Bania"})
        compareStatusCodes(self, getSiteResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        Helper().deleteCompany(self.companyID)
        Helper().deleteSite(self.siteID)