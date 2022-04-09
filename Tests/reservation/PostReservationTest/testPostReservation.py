from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as Helper
from ....TestsHelpers.Service.comparator import ReservationResponse as Comaprator
from ....TestsHelpers.Service.validator import ReservationResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomWord

class TestPostReservation(TestCase):

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

        self.createUserData = defaultDataCreator.User()
        self.createUserData[constants.email] = f"{randomWord(17)}@{randomWord(17)}.com"
        self.userID = Helper().createUser(self.createUserData).json()[constants.userID]

        self.createReservationData = defaultDataCreator.Reservation()
        self.createReservationData[constants.userID] = self.userID
        self.createReservationData[constants.unitID] = self.unitID
        self.reservationID = None

    def testPostReservation(self):
        """Post Reservation"""
        Helper().getSite(self.siteID)
        createReservationResponse = Helper().createReservation(self.createReservationData)
        compareStatusCodes(self, createReservationResponse.status_code, HTTPStatus.CREATED)


        testing = createReservationResponse.json()
        self.reservationID = testing[constants.reservationID]

    def tearDown(self):
        Helper().deleteCompany(self.companyID)
        Helper().deleteSite(self.siteID)
        Helper().deleteUnit(self.unitID)
        Helper().deleteUser(self.userID)
        Helper().deleteReservation(self.reservationID)