from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as UserServiceHelper
from ....TestsHelpers.Service.comparator import UserResponse as Comaprator
from ....TestsHelpers.Service.validator import UserResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomNumber, randomUUID4, randomWord


class TestPostUser(TestCase):

    def setUp(self):
        self.createUserData = defaultDataCreator.User()
        self.userID = None
        self.createUserData[constants.email] = f"{randomWord(17)}@{randomWord(17)}.com"

    def testPostUsers(self):
        """Post User"""
        createUserResponse = UserServiceHelper().createUser(self.createUserData)
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
        """Post User. Email Already Exist"""
        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CONFLICT)

    def testPostWithoutEmail(self):
        """Post User. No Email Given"""
        del self.createUserData[constants.email]

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostEmailAsString(self):
        """Post User. Email As String Type"""
        self.createUserData[constants.email] = randomWord(17)

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostEmailAsInt(self):
        """Post User. Email As Integer Type"""
        self.createUserData[constants.email] = randomNumber(1, 100)

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostEmailAsBool(self):
        """Post User. Email As Bool Type"""
        self.createUserData[constants.email] = True

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostEmailAsArray(self):
        """Post User. Email As Array Type"""
        self.createUserData[constants.email] = ["Ania"]

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostEmailAsDic(self):
        """Post User. Email As Dictionary Type"""
        self.createUserData[constants.email] = {"Ania": "10"}

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostWithoutFirstName(self):
        """Post User. No First Name Given"""
        del self.createUserData[constants.firstName]

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostFirstNameAsString(self):
        """Post User. Name As String Type"""
        self.createUserData[constants.firstName] = randomWord(17)

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CREATED)

    def testPostFirstNameAsInt(self):
        """Post User. Name As Integer Type"""
        self.createUserData[constants.firstName] = randomNumber(1, 100)

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostFirstNameAsBool(self):
        """Post User. Name As Bool Type"""
        self.createUserData[constants.firstName] = True

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostFirstNameAsArray(self):
        """Post User. Name As Array Type"""
        self.createUserData[constants.firstName] = ["Ania"]

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostFirstNameAsDic(self):
        """Post User. Name As Dictionary Type"""
        self.createUserData[constants.firstName] = {"Ania": "10"}

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostWithoutLastName(self):
        """Post User. No Last Nama Given"""
        del self.createUserData[constants.lastName]

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostLastNameAsString(self):
        """Post User. Last Name As String Type"""
        self.createUserData[constants.lastName] = randomWord(17)

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CREATED)

    def testPostLastNameAsInt(self):
        """Post User. Last Name As Integer Type"""
        self.createUserData[constants.lastName] = randomNumber(1,100)

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)
    
    def testPostLastNameAsBool(self):
        """Post User. Last Name As Bool Type"""
        self.createUserData[constants.lastName] = True

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostLastNameAsArray(self):
        """Post User. Last Name As Array Type"""
        self.createUserData[constants.lastName] = ["Ania"]

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)
    
    def testPostLastNameAsDic(self):
        """Post User. Last Name As Dictionary Type"""
        self.createUserData[constants.lastName] = {"Ania": "10"}

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def tearDown(self):
        UserServiceHelper().deleteUser(self.userID)



