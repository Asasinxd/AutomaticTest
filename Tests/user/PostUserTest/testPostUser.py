from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as UserServiceHelper
from ....TestsHelpers.Service.comparator import UserResponse as Comaprator
from ....TestsHelpers.Service.validator import UserResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomNumber, randomWord


class TestPostUser(TestCase):

    def setUp(self):
        self.createUserData = defaultDataCreator.User()
        self.userID = None
        self.createUserData[constants.email] = f"{randomWord(17)}@{randomWord(17)}.com"

    def testPostUser(self):
        """Post User"""
        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CREATED)


        testing = createUserResponse.json()
        expected = self.createUserData

        Validator(self, testing)\
            .userID()\
            .relations()\
            .firstName()\
            .lastName()\
            .email()

        self.userID = testing[constants.userID]

        Comaprator(self, testing, expected)\
            .firstName()\
            .lastName()\
            .email()

        getUserResponse = UserServiceHelper().getUser(self.userID)
        compareStatusCodes(self, getUserResponse.status_code, HTTPStatus.OK)

        testing = getUserResponse.json()

        Validator(self, testing)\
            .userID()\
            .relations()\
            .firstName()\
            .lastName()\
            .email()

        Comaprator(self, testing, expected)\
            .firstName()\
            .lastName()\
            .email()
        

    def testPostUserEmailExistUser(self):
        """Post User. Email Already Exist"""
        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CONFLICT)

    def testPostUserWithoutEmail(self):
        """Post User. No Email Given"""
        del self.createUserData[constants.email]

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserEmailAsString(self):
        """Post User. Email As String Type"""
        self.createUserData[constants.email] = randomWord(17)

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserEmailAsInt(self):
        """Post User. Email As Integer Type"""
        self.createUserData[constants.email] = randomNumber(1, 100)

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserEmailAsBool(self):
        """Post User. Email As Bool Type"""
        self.createUserData[constants.email] = True

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserEmailAsArray(self):
        """Post User. Email As Array Type"""
        self.createUserData[constants.email] = ["Ania"]

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserEmailAsDic(self):
        """Post User. Email As Dictionary Type"""
        self.createUserData[constants.email] = {"Ania": "10"}

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserWithoutFirstName(self):
        """Post User. No First Name Given"""
        del self.createUserData[constants.firstName]

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserFirstNameAsString(self):
        """Post User. Name As String Type"""
        self.createUserData[constants.firstName] = randomWord(17)

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CREATED)

    def testPostUserFirstNameAsInt(self):
        """Post User. Name As Integer Type"""
        self.createUserData[constants.firstName] = randomNumber(1, 100)

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserFirstNameAsBool(self):
        """Post User. Name As Bool Type"""
        self.createUserData[constants.firstName] = True

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserFirstNameAsArray(self):
        """Post User. Name As Array Type"""
        self.createUserData[constants.firstName] = ["Ania"]

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserFirstNameAsDic(self):
        """Post User. Name As Dictionary Type"""
        self.createUserData[constants.firstName] = {"Ania": "10"}

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserWithoutLastName(self):
        """Post User. No Last Nama Given"""
        del self.createUserData[constants.lastName]

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserLastNameAsString(self):
        """Post User. Last Name As String Type"""
        self.createUserData[constants.lastName] = randomWord(17)

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CREATED)

    def testPostUserLastNameAsInt(self):
        """Post User. Last Name As Integer Type"""
        self.createUserData[constants.lastName] = randomNumber(1,100)

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)
    
    def testPostUserLastNameAsBool(self):
        """Post User. Last Name As Bool Type"""
        self.createUserData[constants.lastName] = True

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserLastNameAsArray(self):
        """Post User. Last Name As Array Type"""
        self.createUserData[constants.lastName] = ["Ania"]

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)
    
    def testPostUserLastNameAsDic(self):
        """Post User. Last Name As Dictionary Type"""
        self.createUserData[constants.lastName] = {"Ania": "10"}

        createUserResponse = UserServiceHelper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserNoBody(self):
        """Post User. No Body Given"""
        createUserResponse = UserServiceHelper().createUser(data = None)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserEmptyBody(self):
        """Post User. Empty Body Given"""
        createUserResponse = UserServiceHelper().createUser(data = {})
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        UserServiceHelper().deleteUser(self.userID)



