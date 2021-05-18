from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as UserServiceHelper
from ....TestsHelpers.Service.comparator import UserResponse as Comparator
from ....TestsHelpers.Service.validator import UserResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomUUID4, randomWord, randomNumber

class TestGetUserById(TestCase):

    def setUp(self):
        self.createUserData = defaultDataCreator.User()
        self.createUserData[constants.email] = f"{randomWord(17)}@{randomWord(17)}.com"
        self.createUserResponse = UserServiceHelper().createUser(self.createUserData).json()
        self.userID = self.createUserResponse[constants.userID]
        

    def testGetUser(self):
        """Get User"""
        getUserResponse = UserServiceHelper().getUser(userID = self.userID)
        compareStatusCodes(self, getUserResponse.status_code, HTTPStatus.OK)

        testing = getUserResponse.json()
        expected = self.createUserResponse

        Comparator(self, testing, expected)\
            .userID()\
            .firstName()\
            .lastName()\
            .email()

    def testGetUserNonExistingUser(self):
        """Get User. Non Existing User"""
        getUserResponse = UserServiceHelper().getUser(userID = randomUUID4())
        compareStatusCodes(self, getUserResponse.status_code, HTTPStatus.NOT_FOUND)

    def testGetUserDeleted(self):
        """Get User. User Has Benn Deleted"""
        UserServiceHelper().deleteUser(self.userID)
        getUserResponse = UserServiceHelper().getUser(userID = self.userID)
        compareStatusCodes(self, getUserResponse.status_code, HTTPStatus.NOT_FOUND)

    def testGetUserIdAsString(self):
        """Get User. User Id As String Type"""
        getUserResponse = UserServiceHelper().getUser(userID = randomWord(17))
        compareStatusCodes(self, getUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetUserIdAsInt(self):
        """Get User. User Id As Integer Type"""
        getUserResponse = UserServiceHelper().getUser(userID = randomNumber(1,100))
        compareStatusCodes(self, getUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        UserServiceHelper().deleteUser(self.userID)



        
