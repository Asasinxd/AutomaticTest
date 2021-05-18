from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as UserServiceHelper
from ....TestsHelpers.Service.comparator import UserResponse as Comaprator
from ....TestsHelpers.Service.validator import UserResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomWord, randomNumber, randomUUID4

class TestDeleteUser(TestCase):

    def setUp(self):
        self.createUserData = defaultDataCreator.User()
        self.createUserData[constants.email] = f"{randomWord(17)}@{randomWord(17)}.com"
        self.createUserResponse = UserServiceHelper().createUser(self.createUserData).json()
        self.userID = self.createUserResponse[constants.userID]

    def testDeleteUser(self):
        """Delete User"""
        deleteUserResponce = UserServiceHelper().deleteUser(self.userID)
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.NO_CONTENT)
    
    def testDeleteUserNonExisting(self):
        """Delete User. Non Existing User"""
        deleteUserResponce = UserServiceHelper().deleteUser(randomUUID4())
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteUserAlreadyDeleted(self):
        """Delete User. Already Deleted User"""
        deleteUserResponce = UserServiceHelper().deleteUser(self.userID)
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.NO_CONTENT)
        deleteUserResponce = UserServiceHelper().deleteUser(self.userID)
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteUserEmptyUserId(self):
        """Delete User. Empty User Id"""
        deleteUserResponce = UserServiceHelper().deleteUser(userID = '')
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def testDeleteUserIdAsString(self):
        """Delete User. User Id As String Type"""
        deleteUserResponce = UserServiceHelper().deleteUser(randomWord(17))
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUserIdAsInt(self):
        """Delete User. User Id As Integer Type"""
        deleteUserResponce = UserServiceHelper().deleteUser(randomNumber(1,100))
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUserIdAsDic(self):
        """Delete User. User Id As Dictionary Type"""
        deleteUserResponce = UserServiceHelper().deleteUser({"Ania", "10"})
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUserIdAsArray(self):
        """Delete User. User Id As Array Type"""
        deleteUserResponce = UserServiceHelper().deleteUser(["Ania"])
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUserIdAsBoolen(self):
        """Delete User. User Id As Bool Type"""
        deleteUserResponce = UserServiceHelper().deleteUser(True)
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        UserServiceHelper().deleteUser(self.userID)