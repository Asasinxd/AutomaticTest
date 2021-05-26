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
        self.updateData = defaultDataCreator.SiteUpdate()

    def testPatchSite(self):
        """Patch Site"""
        updateSietResponse = Helper().updateSite(self.siteID, self.updateData)
        compareStatusCodes(self, updateSietResponse.status_code, HTTPStatus.OK)

        testing = updateSietResponse.json()
        expected = self.updateData

        Validator(self, testing)\
            .siteID()\
            .companyID()\
            .name()\
            .address()\
                .street()\
                .city()\
                .postalCode()\
                .country()\
                .back()\
            .weeklyOpeningTimes()\
                .monday()\
                .tuesday()\
                .wednesday()\
                .thursday()\
                .friday()\
                .saturday()\
                .sunday()\
                .back()\
            .pricing()\
                .numberOfMinutes()\
                .price()\
                .back()

        Comaprator(self, testing, expected)\
            .name()\
            .address()\
                .street()\
                .city()\
                .postalCode()\
                .country()\
                .back()\
            .weeklyOpeningTimes()\
                .monday()\
                .tuesday()\
                .wednesday()\
                .thursday()\
                .friday()\
                .saturday()\
                .sunday()\
                .back() 


    def testPatchSiteNonExistingSite(self):
        """Patch Site. Non Existing Site"""
        updateSietResponse = Helper().updateSite(siteID = randomUUID4(), data = self.updateData)
        compareStatusCodes(self, updateSietResponse.status_code, HTTPStatus.NOT_FOUND)

    def testPatchSiteNoBody(self):
        """Patch Site. No Body Given"""
        updateSietResponse = Helper().updateSite(self.siteID, data = None)
        compareStatusCodes(self, updateSietResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPatchSiteEmptyBody(self):
        """Patch Site. Empty Body Given"""
        updateSietResponse = Helper().updateSite(self.siteID, data = {})
        compareStatusCodes(self, updateSietResponse.status_code, HTTPStatus.OK)


    def tearDown(self):
        Helper().deleteCompany(self.companyID)
        Helper().deleteSite(self.siteID)