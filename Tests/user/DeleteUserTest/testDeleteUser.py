from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper
from ....TestsHelpers.Service.comparator import UserResponse as Comaprator
from ....TestsHelpers.Service.validator import UserResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomWord, randomNumber, randomUUID4

class TestDeleteUser(TestCase):

    def setUp(self):
        self.createUserData = defaultDataCreator.User()
        self.createUserData[constants.email] = f"{randomWord(17)}@{randomWord(17)}.com"
        self.createUserResponse = Helper().createUser(self.createUserData).json()
        self.userID = self.createUserResponse[constants.userID]

    def testDeleteUser(self):
        """Delete User"""
        deleteUserResponce = Helper().deleteUser(self.userID)
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.NO_CONTENT)
    
    def testDeleteUserNonExisting(self):
        """Delete User. Non Existing User"""
        deleteUserResponce = Helper().deleteUser(randomUUID4())
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteUserAlreadyDeleted(self):
        """Delete User. Already Deleted User"""
        deleteUserResponce = Helper().deleteUser(self.userID)
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.NO_CONTENT)
        deleteUserResponce = Helper().deleteUser(self.userID)
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteUserEmptyUserId(self):
        """Delete User. Empty User Id"""
        deleteUserResponce = Helper().deleteUser(userID = '')
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def testDeleteUserIdAsString(self):
        """Delete User. User Id As String Type"""
        deleteUserResponce = Helper().deleteUser(randomWord(17))
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUserIdAsInt(self):
        """Delete User. User Id As Integer Type"""
        deleteUserResponce = Helper().deleteUser(randomNumber(1,100))
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUserIdAsDic(self):
        """Delete User. User Id As Dictionary Type"""
        deleteUserResponce = Helper().deleteUser({"Ania": "10"})
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUserIdAsArray(self):
        """Delete User. User Id As Array Type"""
        deleteUserResponce = Helper().deleteUser(["Ania"])
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUserIdAsBoolen(self):
        """Delete User. User Id As Bool Type"""
        deleteUserResponce = Helper().deleteUser(userID = True)
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        Helper().deleteUser(self.userID)