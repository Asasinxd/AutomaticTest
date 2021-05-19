from unittest import TestCase
from http import HTTPStatus


from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper
from ....TestsHelpers.Service.comparator import UserResponse as Comaprator
from ....TestsHelpers.Service.validator import UserResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomWord

class TestGetAllUsers(TestCase):

    def setUp(self):
        self.createUserData = defaultDataCreator.User()
        self.createUserData[constants.email] = f"{randomWord(17)}@{randomWord(17)}.com"
        self.createUserResponse = Helper().createUser(self.createUserData).json()
        self.userID = self.createUserResponse[constants.userID]

        self.createCompanyData = defaultDataCreator.Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.companyID = Helper().createCompany(self.createCompanyData).json()[constants.companyID]


    def testGetAllUsers(self):
        """Get All Users"""
        getAllUsersResponse = Helper().getUsers()
        compareStatusCodes(self, getAllUsersResponse.status_code, HTTPStatus.OK)

        testing = getAllUsersResponse.json()

        self.assertIn(constants.limit, testing, "No limit field in response body")
        self.assertIn(constants.count, testing, "No count field in response body")
        self.assertIn(constants.users, testing, "No users field in response body")

        usersLength = len(testing[constants.users])
        self.assertTrue(10 >= usersLength > 0, "Incorrect number of users array in response body")
        self.assertTrue(testing[constants.count] >= usersLength, "Incorrect count compared to number of users in response body")
        self.assertEqual(10, testing[constants.limit], "Incorrect limit in response body")

    def testGetAllUsersLimitAndOffset(self):
        """Get All Users. Limit And Offset Given"""
        getAllUsersResponse = Helper().getUsers(limit = 20, offset = 10)
        compareStatusCodes(self, getAllUsersResponse.status_code, HTTPStatus.OK)

        testing = getAllUsersResponse.json()

        self.assertIn(constants.limit, testing, "No limit field in response body")
        self.assertIn(constants.count, testing, "No count field in response body")
        self.assertIn(constants.offset, testing, "No offset field in response body")
        self.assertIn(constants.users, testing, "No user field in response body")

        usersLength = len(testing[constants.users])
        self.assertTrue(20 >= usersLength > 0, "Incorrect number of users array in response body")
        self.assertTrue(testing[constants.count] >= usersLength, "Incorrect count compared to number of users in response body")
        self.assertEqual(20, testing[constants.limit], "Incorrect limi in response body")
        self.assertEqual(10, testing[constants.offset], "Incorrect offset in response body")

    def testGetAllUsersCompanyID(self):
        """Get All Users. Company Id Given"""
        getAllUsersResponse = Helper().getUsers(companyID = self.companyID)
        compareStatusCodes(self, getAllUsersResponse.status_code, HTTPStatus.OK)

        testing = getAllUsersResponse.json()

        self.assertIn(constants.limit, testing, "No limit field in response body")
        self.assertIn(constants.count, testing, "No count field in response body")
        self.assertIn(constants.users, testing, "No users field in response body")

        usersLength = len(testing[constants.users])
        self.assertTrue(10 >= usersLength > 0, "Incorrect number of users array in response body")
        self.assertTrue(testing[constants.count] >= usersLength, "Incorrect count compared to number of users in response body")
        self.assertEqual(10, testing[constants.limit], "Incorrect limit in response body")

    def testGetAllUserSiteID(self):
        """Get All Users. Site Id Given"""

    def tearDown(self):
        Helper().deleteCompany(self.companyID)
        Helper().deleteUser(self.userID)