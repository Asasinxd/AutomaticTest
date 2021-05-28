from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as Helper
from ....TestsHelpers.Service.comparator import UnitResponse as Comaprator
from ....TestsHelpers.Service.validator import UnitResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomUUID4, randomWord

class TestPatchUnit(TestCase):

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
        self.updateData = defaultDataCreator.UnitUpdate()

    def testPatchUnit(self):
        """Patch Unit"""
        updateUnitResponse = Helper().updateUnit(self.unitID, self.updateData)
        compareStatusCodes(self, updateUnitResponse.status_code, HTTPStatus.OK)

        testing = updateUnitResponse.json()
        expected = self.updateData

        Validator(self, testing)\
            .unitID()\
            .siteID()\
            .name()

        Comaprator(self, testing, expected)\
            .name()

        getUnitResponse = Helper().getUnit(self.unitID)
        compareStatusCodes(self, getUnitResponse.status_code, HTTPStatus.OK)

        testing = getUnitResponse.json()
        expected = updateUnitResponse.json()

        Validator(self, testing)\
            .unitID()\
            .siteID()\
            .name()

        Comaprator(self, testing, expected)\
            .unitID()\
            .siteID()\
            .name()

    def testPatchUnitNonExistingUnit(self):
        """Patch Unit. Non-Existing Unit"""
        updateUnitResponse = Helper().updateUnit(unitID = randomUUID4(), data = self.updateData)
        compareStatusCodes(self, updateUnitResponse.status_code, HTTPStatus.NOT_FOUND)

    def testPatchUnitNoBody(self):
        """Patch Unit. No Body Given"""
        updateUnitResponse = Helper().updateUnit(self.unitID, data = None)
        compareStatusCodes(self, updateUnitResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPatchUnitEmptyBody(self):
        """Patch Unit. Empty Body Given"""
        updateUnitResponse = Helper().updateUnit(self.unitID, data = {})
        compareStatusCodes(self, updateUnitResponse.status_code, HTTPStatus.OK)

    def tearDown(self):
        Helper().deleteCompany(self.companyID)
        Helper().deleteSite(self.siteID)
        Helper().deleteUnit(self.unitID)