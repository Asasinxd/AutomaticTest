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
        self.updateData = UserUpdate()

    def testPatchUser(self):
        updateUserResponse = helper().updateUser(self.userID, self.updateData)
        compareStatusCodes(self, updateUserResponse.status_code, HTTPStatus.OK)

        testing = updateUserResponse.json()
        expected = self.updateData

        Validator(self, testing)\
            .firstName()\
            .lastName()\
            .email()\

        Comaprator(self, testing, expected)\
            .firstName()\
            .lastName()\

    def testPatchUserNonExistingUser(self):
        updateUserResponse = helper().updateUser(randomUUID4(), self.updateData)
        compareStatusCodes(self, updateUserResponse.status_code, HTTPStatus.NOT_FOUND)


    def tearDown(self):
        helper().deleteUser(self.userID)