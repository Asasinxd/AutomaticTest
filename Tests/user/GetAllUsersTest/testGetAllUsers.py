from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as UserServiceHelper
from ....TestsHelpers.Service.comparator import UserResponse as Comaprator
from ....TestsHelpers.Service.validator import UserResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomWord

class TestGetAllUsers(TestCase):

    def setUp(self):
        self.createUserData = defaultDataCreator.User()
        self.createUserData[constants.email] = f"{randomWord(17)}@{randomWord(17)}.com"
        self.createUserResponse = UserServiceHelper().createUser(self.createUserData).json()
        self.userID = self.createUserResponse[constants.userID]

    def testGetAllUsers(self):
        """Get All Users"""
        getAllUsersResponse = UserServiceHelper().getUsers()
        compareStatusCodes(self, getAllUsersResponse.status_code, HTTPStatus.OK)

    def testGetAllUsersLimitAndOffset(self):
        """Get User. Limit And Offset Given"""
        getAllUsersResponse = UserServiceHelper().getUsers(limit = 10, offset = 2)
        compareStatusCodes(self, getAllUsersResponse.status_code, HTTPStatus.OK)

    def tearDown(self):
        UserServiceHelper().deleteUser(self.userID)