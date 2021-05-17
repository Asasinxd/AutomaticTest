from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service.defaultDataCreator import *
from ....TestsHelpers.Service.helper import *
from ....TestsHelpers.Service.comparator import UserResponse as Comaprator
from ....TestsHelpers.Service.validator import UserResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import *
from ....TestsHelpers.TestsUtils.randomStuff import *


class TestPostUser(TestCase):

    def setUp(self):
        self.createUserData = User()
        self.userID = None
        self.createUserData[constants.email] = f"{randomWord(17)}@{randomWord(17)}.com"

    def testPostUsers(self):
        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CREATED)


        testing = createUserResponse.json()
        expected = self.createUserData

        Validator(self, testing)\
            .userID()\
            .relations()

        self.userID = testing[constants.userID]

        Comaprator(self, testing, expected)\
            .firstName()\
            .lastName()\
            .email()

    def testPostEmailExistUser(self):
        createUserResponse = Helper().createUser(self.createUserData)
        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CONFLICT)

    def testPostWithoutEmail(self):
        del self.createUserData[constants.email]

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostEmailAsString(self):
        self.createUserData[constants.email] = randomWord(17)

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostEmailAsInt(self):
        self.createUserData[constants.email] = randomNumber(1, 100)

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostEmailAsBool(self):
        self.createUserData[constants.email] = True

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostEmailAsArray(self):
        self.createUserData[constants.email] = ["Ania"]

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostEmailAsDic(self):
        self.createUserData[constants.email] = {"Ania": "10"}

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostWithoutFirstName(self):
        del self.createUserData[constants.firstName]

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostFirstNameAsString(self):
        self.createUserData[constants.firstName] = randomWord(17)

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CREATED)

    def testPostFirstNameAsInt(self):
        self.createUserData[constants.firstName] = randomNumber(1, 100)

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostFirstNameAsBool(self):
        self.createUserData[constants.firstName] = True

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostFirstNameAsArray(self):
        self.createUserData[constants.firstName] = ["Ania"]

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostFirstNameAsDic(self):
        self.createUserData[constants.firstName] = {"Ania": "10"}

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostWithoutLastName(self):
        del self.createUserData[constants.lastName]

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostLastNameAsString(self):
        self.createUserData[constants.lastName] = randomWord(17)

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CREATED)

    def testPostLastNameAsInt(self):
        self.createUserData[constants.lastName] = randomNumber(1,100)

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)
    
    def testPostLastNameAsBool(self):
        self.createUserData[constants.lastName] = True

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostLastNameAsArray(self):
        self.createUserData[constants.lastName] = ["Ania"]

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)
    
    def testPostLastNameAsDic(self):
        self.createUserData[constants.lastName] = {"Ania": "10"}

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def tearDown(self):
        Helper().deleteUser(self.userID)



