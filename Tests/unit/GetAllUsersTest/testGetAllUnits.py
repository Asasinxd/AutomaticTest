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
        self.unitID = Helper().createUnit(self.createUnitData).json()[constants.unitID]

    def testGetAllUnits(self):
        """Get All Units"""
        getAllUnitsResponse = Helper().getUnits()
        compareStatusCodes(self, getAllUnitsResponse.status_code, HTTPStatus.OK)

        testing = getAllUnitsResponse.json()

        self.assertIn(constants.limit, testing, "No limit field in response body")
        self.assertIn(constants.count, testing, "No count field in response body")
        self.assertIn(constants.units, testing, "No units field in response body")

        unitsLength = len(testing[constants.units])

        self.assertTrue(10 >= unitsLength > 0, "Incorrect number of units array in response body")
        self.assertTrue(testing[constants.count] >= unitsLength, "Incorrect count compared to number of users in response body")
        self.assertEqual(10, testing[constants.limit], "Incorrect limit in response body")

    def testGetAllUnitsLimitAndOffset(self):
        """Get All Units. Limit And Offset Given"""
        getAllUnitsResponse = Helper().getUnits(limit = 2, offset = 1)
        compareStatusCodes(self, getAllUnitsResponse.status_code, HTTPStatus.OK)

        testing = getAllUnitsResponse.json()

        self.assertIn(constants.limit, testing, "No limit field in response body")
        self.assertIn(constants.count, testing, "No count field in response body")
        self.assertIn(constants.units, testing, "No units field in response body")
        self.assertIn(constants.offset, testing, "No offset fieldin response body")

        unitsLength = len(testing[constants.units])

        self.assertTrue(2 >= unitsLength > 0, "Incorrect number of units array in response body")
        self.assertTrue(testing[constants.count] >= unitsLength, "Incorrect count compared to number of users in response body")
        self.assertEqual(2, testing[constants.limit], "Incorrect limit in response body")
        self.assertEqual(1, testing[constants.offset], "Incorrect offset in response body")

    def tearDown(self):
        Helper().deleteCompany(self.companyID)
        Helper().deleteSite(self.siteID)
        Helper().deleteUnit(self.unitID)