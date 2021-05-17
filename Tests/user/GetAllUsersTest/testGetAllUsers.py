from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service.defaultDataCreator import *
from ....TestsHelpers.Service.helper import Helper as helper
from ....TestsHelpers.Service.comparator import UserResponse as Comaprator
from ....TestsHelpers.Service.validator import UserResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import *

class TestGetAllUsers(TestCase):

    def setUp(self):
        self.createUserData = User()
        self.createUserData[constants.email] = f"{randomWord(17)}@{randomWord(17)}.com"
        self.createUserResponse = helper().createUser(self.createUserData).json()

    def testGetAllUsers(self):
        getAllUsersResponse = helper().getUsers()
        compareStatusCodes(self, getAllUsersResponse.status_code, HTTPStatus.OK)

    def tearDown(self):
        helper().deleteUser(self.userID)