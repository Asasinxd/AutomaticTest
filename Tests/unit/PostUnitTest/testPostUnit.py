from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as Helper
from ....TestsHelpers.Service.comparator import UnitResponse as Comaprator
from ....TestsHelpers.Service.validator import UnitResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomUUID4, randomWord, randomNumber

class TestPostUnit(TestCase):

    def setUp(self):
        self.createCompanyData = defaultDataCreator.Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.companyID = Helper().createCompany(self.createCompanyData).json()[constants.companyID]

        self.createSiteData = defaultDataCreator.Site()
        self.createSiteData[constants.companyID] = self.companyID
        self.createSiteResponse = Helper().createSite(self.createSiteData).json()
        self.siteID = self.createSiteResponse[constants.siteID]

        self.createUnitData = defaultDataCreator.Unit()
        self.createUnitData[constants.siteID] = self.siteID
        self.unitID = None

    def testPostUnit(self):
        """Post Unit"""
        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.CREATED)

        testing = createUnitResponse.json()
        expected = self.createUnitData

        Validator(self, testing)\
            .unitID()\
            .siteID()\
            .name()

        self.unitID = testing[constants.unitID]

        Comaprator(self, testing, expected)\
            .name()\
            .siteID()

        getUnitResponse = Helper().getUnit(self.unitID)
        compareStatusCodes(self, getUnitResponse.status_code, HTTPStatus.OK)

        expected = createUnitResponse.json()
        testing = getUnitResponse.json()

        Validator(self, testing)\
            .unitID()\
            .siteID()\
            .name()

        Comaprator(self, testing, expected)\
            .name()\
            .siteID()

    def testPostUnitAlreadyExist(self):
        """Post Unit. Unit Already Exist"""
        createUnitResponse = Helper().createUnit(self.createUnitData)
        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.CONFLICT)

    def testPostUnitEmptyBody(self):
        """Post Unit. Empty Body Given"""
        createUnitResponse = Helper().createUnit(data = {})
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUnitWithoutBody(self):
        """Post Unit. No Body Given"""
        createUnitResponse = Helper().createUnit(data = None)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUnitWithoutSiteId(self):
        """Post Unit. No Site Id Given"""
        del self.createUnitData[constants.siteID]
        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUnitEmptySiteId(self):
        """Post Unit. Empty Site Id Given"""
        self.createUnitData[constants.siteID] = ""

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUnitSiteIdAsString(self):
        """Post Unit. Site Id As String Type"""
        self.createUnitData[constants.siteID] = randomWord(17)

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUnitSiteIdAsRandomUUID(self):
        """Post Unit. Site Id As Random UUID"""
        self.createUnitData[constants.siteID] = randomUUID4()

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    def testPostUnitSiteIdAsInt(self):
        """Post Unit. Site Id As Integer Type"""
        self.createUnitData[constants.siteID] = randomNumber(1,100)

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUnitSiteIdAsArray(self):
        """Post Unit. Site Id As Array Type"""
        self.createUnitData[constants.siteID] = ["Ania"]

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.BAD_REQUEST)


    def testPostUnitSiteIdAsDict(self):
        """Post Unit. Site Id As Dictionary Type"""
        self.createUnitData[constants.siteID] = {"Ania":"10"}

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUnitSiteIdAsBool(self):
        """Post Unit. Site Id As Boolen Type"""
        self.createUnitData[constants.siteID] = True

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUnitWithoutName(self):
        """Post Unit. No Name Given"""
        del self.createUnitData[constants.name]

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUnitEmptyName(self):
        """Post Unit. Empty Name Given"""
        self.createUnitData[constants.name] = ""

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUnitNameAsInt(self):
        """Post Unit. Name As Integer Type"""
        self.createUnitData[constants.name] = randomNumber(1,100)

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUnitNameAsBool(self):
        """Post Unit. Name As Boolen Type"""
        self.createUnitData[constants.name] = True

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUnitNameAsArray(self):
        """Post Unit. Name As Array Type"""
        self.createUnitData[constants.name] = ["Ania"]

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUnitNameAsDict(self):
        self.createUnitData[constants.name] = {"Ania": "10"}

        createUnitResponse = Helper().createUnit(self.createUnitData)
        compareStatusCodes(self, createUnitResponse.status_code, HTTPStatus.BAD_REQUEST)

    def tearDown(self):
        Helper().deleteCompany(self.companyID)
        Helper().deleteSite(self.siteID)
        Helper().deleteUnit(self.unitID)