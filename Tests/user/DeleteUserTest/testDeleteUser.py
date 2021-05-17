from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service.defaultDataCreator import *
from ....TestsHelpers.Service.helper import Helper as helper
from ....TestsHelpers.Service.comparator import UserResponse as Comaprator
from ....TestsHelpers.Service.validator import UserResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import *

class TestDeleteUser(TestCase):

    def setUp(self):
        self.createUserData = User()
        self.createUserData[constants.email] = f"{randomWord(17)}@{randomWord(17)}.com"
        self.createUserResponse = helper().createUser(self.createUserData).json()
        self.userID = self.createUserResponse[constants.userID]

    def testDeleteUser(self):
        deleteUserResponce = helper().deleteUser(self.userID)
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.NO_CONTENT)
    
    def testDeleteUserNonExisting(self):
        deleteUserResponce = helper().deleteUser(randomUUID4())
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteUserAlreadyDeleted(self):
        deleteUserResponce = helper().deleteUser(self.userID)
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.NO_CONTENT)
        deleteUserResponce = helper().deleteUser(self.userID)
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteUserEmptyUserId(self):
        deleteUserResponce = helper().deleteUser('')
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def testDeleteUserIdAsString(self):
        deleteUserResponce = helper().deleteUser(randomWord(17))
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUserIdAsInt(self):
        deleteUserResponce = helper().deleteUser(randomNumber(1,100))
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUserIdAsDic(self):
        deleteUserResponce = helper().deleteUser({"Ania", "10"})
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUserIdAsArray(self):
        deleteUserResponce = helper().deleteUser(["Ania"])
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteUserIdAsBoolen(self):
        deleteUserResponce = helper().deleteUser(True)
        compareStatusCodes(self, deleteUserResponce.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        helper().deleteUser(self.userID)