from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service.defaultDataCreator import *
from ....TestsHelpers.Service.helper import *
from ....TestsHelpers.Service.comparator import UserResponse as Comparator
from ....TestsHelpers.Service.validator import *
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import *
from ....TestsHelpers.TestsUtils.randomStuff import *

class TestGetUserById(TestCase):

    def setUp(self):
        self.createUserData = User()
        self.createUserData[constants.email] = f"{randomWord(17)}@{randomWord(17)}.com"
        self.createUserResponse = Helper().createUser(self.createUserData).json()
        self.userID = self.createUserResponse[constants.userID]
        

    def testGetUser(self):
        getUserResponse = Helper().getUser(userID = self.userID)
        compareStatusCodes(self, getUserResponse.status_code, HTTPStatus.OK)

        testing = getUserResponse.json()
        expected = self.createUserResponse

        Comparator(self, testing, expected)\
            .userID()\
            .firstName()\
            .lastName()\
            .email()

    def testGetUserNonExistingUser(self):
        getUserResponse = Helper().getUser(userID = randomUUID4())
        compareStatusCodes(self, getUserResponse.status_code, HTTPStatus.NOT_FOUND)

    def testGetUserDeleted(self):
        Helper().deleteUser(self.userID)
        getUserResponse = Helper().getUser(userID = self.userID)
        compareStatusCodes(self, getUserResponse.status_code, HTTPStatus.NOT_FOUND)

    def testGetUserIdAsString(self):
        getUserResponse = Helper().getUser(userID = randomWord(17))
        compareStatusCodes(self, getUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetUserIdAsInt(self):
        getUserResponse = Helper().getUser(userID = randomNumber(1,100))
        compareStatusCodes(self, getUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        Helper().deleteUser(self.userID)



        
