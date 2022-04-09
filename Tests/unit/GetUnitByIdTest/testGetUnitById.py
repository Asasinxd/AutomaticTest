import http
from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as Helper
from ....TestsHelpers.Service.comparator import UnitResponse as Comparator
from ....TestsHelpers.Service.validator import UnitResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomUUID4, randomWord, randomNumber

class TestGetUnitById(TestCase):

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
        self.createUnitResponse = Helper().createUnit(self.createUnitData).json()
        self.unitID = self.createUnitResponse[constants.unitID]

    def testGetUnit(self):
        """Get Unit By Id"""
        getUnitResponse = Helper().getUnit(self.unitID)
        compareStatusCodes(self, getUnitResponse.status_code, HTTPStatus.OK)

        testing = getUnitResponse.json()
        expected = self.createUnitResponse

        Comparator(self, testing, expected)\
            .unitID()\
            .siteID()\
            .name()

    def testGetUnitNonExistingUnit(self):
        """Get Unit. Non-Existing Unit"""
        getUnitResponse = Helper().getUnit(unitID = randomUUID4())
        compareStatusCodes(self, getUnitResponse.status_code, HTTPStatus.NOT_FOUND)

    def testGetUnitDeleted(self):
        """Get Unit. Unit Has Been Deleted"""
        Helper().deleteUnit(self.unitID)
        getUnitResponse = Helper().getUnit(self.unitID)
        compareStatusCodes(self, getUnitResponse.status_code, HTTPStatus.NOT_FOUND)

    def testGetUnitIdAsString(self):
        """Get Unit. Id As String Type"""
        getUnitResponse = Helper().getUnit(unitID = randomWord(17))
        compareStatusCodes(self, getUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetUnitIdAsInt(self):
        """Get Unit. Id As Integer Type"""
        getUnitResponse = Helper().getUnit(unitID = randomNumber(1,100))
        compareStatusCodes(self, getUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        Helper().deleteCompany(self.companyID)
        Helper().deleteSite(self.siteID)
        Helper().deleteUnit(self.unitID)