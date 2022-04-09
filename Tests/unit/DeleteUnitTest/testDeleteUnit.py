from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as Helper
from ....TestsHelpers.Service.comparator import UnitResponse as Comaprator
from ....TestsHelpers.Service.validator import UnitResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomUUID4, randomWord, randomNumber

class TestDeleteUnit(TestCase):

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

    def testDeleteUnit(self):
        """Delete Unit"""
        deleteUnitResponse = Helper().deleteUnit(self.unitID)
        compareStatusCodes(self, deleteUnitResponse.status_code, HTTPStatus.NO_CONTENT)

    def testDeleteUnitAlreadyDeletd(self):
        """Delete Unit. Already Deleted Unit"""
        deleteUnitResponse = Helper().deleteUnit(self.unitID)
        compareStatusCodes(self, deleteUnitResponse.status_code, HTTPStatus.NO_CONTENT)
        deleteUnitResponse = Helper().deleteUnit(self.unitID)
        compareStatusCodes(self, deleteUnitResponse.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteUnitDoesNotExist(self):
        """Delete Unit. Non-Existing Unit"""
        deleteUnitResponse = Helper().deleteUnit(unitID = randomUUID4())
        compareStatusCodes(self, deleteUnitResponse.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteUnitWithEmptyId(self):
        """Delete Unit. Empty Unit Id Given"""
        deleteUnitResponse = Helper().deleteUnit(unitID = '')
        compareStatusCodes(self, deleteUnitResponse.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def testDeleteUnitIdAsString(self):
        """Delete Unit. Unit Id As String Type"""
        deleteUnitResponse = Helper().deleteUnit(unitID = randomWord(17))
        compareStatusCodes(self, deleteUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUnitIdAsInt(self):
        """Delete Unit. Unit Id As Integer Type"""
        deleteUnitResponse = Helper().deleteUnit(unitID = randomNumber(1,100))
        compareStatusCodes(self, deleteUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUnitIdAsBool(self):
        """Delete Unit. Unit Id As Boolen Type"""
        deleteUnitResponse = Helper().deleteUnit(unitID = True)
        compareStatusCodes(self, deleteUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUnitIdArray(self):
        """Delete Unit. Unit Id As Array Type"""
        deleteUnitResponse = Helper().deleteUnit(unitID = ["Ania"])
        compareStatusCodes(self, deleteUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUnitIdDict(self):
        """Delete Unit. Unit Id As Dictionary Type"""
        deleteUnitResponse = Helper().deleteUnit(unitID = {"Ania":"10"})
        compareStatusCodes(self, deleteUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        Helper().deleteCompany(self.companyID)
        Helper().deleteSite(self.siteID)
        Helper().deleteUnit(self.unitID)