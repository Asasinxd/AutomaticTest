from os import O_CREAT
from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator

from ....TestsHelpers.Service.helper import Helper 
from ....TestsHelpers.Service.comparator import SiteResponse as Comaprator
from ....TestsHelpers.Service.validator import Pricing, SiteResponse as Validator
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
        self.siteID = None

    def testPostSite(self):
        """Post Site"""
        print(self.createSiteData)
        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.CREATED)


        testing = createSiteResponse.json()
        expected = self.createSiteData

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
            .pricing()\
                .numberOfMinutes()\
                .price()\
                .back()
            
        self.siteID = testing[constants.siteID]

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

        getSiteResponse = Helper().getSite(self.siteID)
        compareStatusCodes(self, getSiteResponse.status_code, HTTPStatus.OK)

        testing = getSiteResponse.json()

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

    def testPostSiteNoBody(self):
        """Post Site. No Body Given"""
        createSiteResponse = Helper().createSite(data = None)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostSiteEmptyBody(self):
        """Post Site. Empty Body Given"""
        createSiteResponse = Helper().createSite(data = {})
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY) 

    def testPostSiteWithoutCompanyId(self):
        """Post Site. Without Company Id"""
        del self.createSiteData[constants.companyID]
        
        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostSiteEmptyCompanyId(self):
        """Post Site. Empty Company Id Given"""
        self.createSiteData[constants.companyID] = ''

        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostSiteCompanyIdAsString(self):
        """Post Site. Company Id As String Type"""
        self.createSiteData[constants.companyID] = randomWord(17)

        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostSiteCompanyIdAsInt(self):
        """Post Site. Company Id As Integer Type"""
        self.createSiteData[constants.companyID] = randomNumber(1,100)

        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostSiteCompanyIdAsRandomUUID(self):
        """Post Site. Company Id As Random UUID"""
        self.createSiteData[constants.companyID] = randomUUID4()

        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    def testPostSiteCompanyIdAsBool(self):
        """Post Site. Company Id As Boolen Type"""
        self.createSiteData[constants.companyID] = True

        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostSiteCompanyIdAsArray(self):
        """Post Site. Company Id As Array Type"""
        self.createSiteData[constants.companyID] = ["Ania"]

        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostSiteCompanyIdAsDict(self):
        """Post Site. Company Id Dictionary Type"""
        self.createSiteData[constants.companyID] = {"Ania" : "10"}

        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostSiteNameAsInt(self):
        """Post Site. Name As Integer Type"""
        self.createSiteData[constants.name] = randomNumber(1,100)

        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostSiteNameAsBool(self):
        """Post Site. Name As Boolen Type"""
        self.createSiteData[constants.name] = True

        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostSiteNameAsArray(self):
        """Post Site. Name As Array Type"""
        self.createSiteData[constants.name] = ["Ania"]

        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostSiteNameAsDict(self):
        """Post Site. Name Dictionary Type"""
        self.createSiteData[constants.name] = {"Ania" : "10"}

        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostSiteWithoutName(self):
        """Post Site. Without Name"""
        del self.createSiteData[constants.name]
        
        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostSiteEmptyName(self):
        """Post Site. Empty Name Given"""
        self.createSiteData[constants.name] = ''

        createSiteResponse = Helper().createSite(self.createSiteData)
        compareStatusCodes(self, createSiteResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        Helper().deleteCompany(self.companyID)
        Helper().deleteSite(self.siteID)