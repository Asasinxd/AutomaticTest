from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper
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
        createUserResponse = Helper().createUser(self.createUserData)
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

        getUserResponse = Helper().getUser(self.userID)
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
        createUserResponse = Helper().createUser(self.createUserData)
        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CONFLICT)

    def testPostUserWithoutEmail(self):
        """Post User. No Email Given"""
        del self.createUserData[constants.email]

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserEmailAsNone(self):
        """Post User. Email As None"""
        self.createUserData[constants.email] = None

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserEmailAsInvalidSyntax(self):
        """Post User. Email As Invalid Syntax"""
        self.createUserData[constants.email] = randomWord(17)

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserEmailAsInt(self):
        """Post User. Email As Integer Type"""
        self.createUserData[constants.email] = randomNumber(1, 100)

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserEmailAsBool(self):
        """Post User. Email As Bool Type"""
        self.createUserData[constants.email] = True

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserEmailAsArray(self):
        """Post User. Email As Array Type"""
        self.createUserData[constants.email] = ["Ania"]

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserEmailAsDic(self):
        """Post User. Email As Dictionary Type"""
        self.createUserData[constants.email] = {"Ania": "10"}

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserWithoutFirstName(self):
        """Post User. No First Name Given"""
        del self.createUserData[constants.firstName]

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserFirstNameAsNone(self):
        """Post User. Fist Name As None"""
        self.createUserData[constants.firstName] = None

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserFirstNameAsString(self):
        """Post User. Name As String Type"""
        self.createUserData[constants.firstName] = randomWord(17)

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CREATED)

    def testPostUserFirstNameAsInt(self):
        """Post User. Name As Integer Type"""
        self.createUserData[constants.firstName] = randomNumber(1, 100)

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserFirstNameAsBool(self):
        """Post User. Name As Bool Type"""
        self.createUserData[constants.firstName] = True

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserFirstNameAsArray(self):
        """Post User. Name As Array Type"""
        self.createUserData[constants.firstName] = ["Ania"]

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserFirstNameAsDic(self):
        """Post User. Name As Dictionary Type"""
        self.createUserData[constants.firstName] = {"Ania": "10"}

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserWithoutLastName(self):
        """Post User. No Last Nama Given"""
        del self.createUserData[constants.lastName]

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserLastNameAsNone(self):
        """Post User. Last Name As None"""
        self.createUserData[constants.lastName] = None

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserLastNameAsString(self):
        """Post User. Last Name As String Type"""
        self.createUserData[constants.lastName] = randomWord(17)

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.CREATED)

    def testPostUserLastNameAsInt(self):
        """Post User. Last Name As Integer Type"""
        self.createUserData[constants.lastName] = randomNumber(1,100)

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)
    
    def testPostUserLastNameAsBool(self):
        """Post User. Last Name As Bool Type"""
        self.createUserData[constants.lastName] = True

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserLastNameAsArray(self):
        """Post User. Last Name As Array Type"""
        self.createUserData[constants.lastName] = ["Ania"]

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)
    
    def testPostUserLastNameAsDic(self):
        """Post User. Last Name As Dictionary Type"""
        self.createUserData[constants.lastName] = {"Ania": "10"}

        createUserResponse = Helper().createUser(self.createUserData)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostUserNoBody(self):
        """Post User. No Body Given"""
        createUserResponse = Helper().createUser(data = None)
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostUserEmptyBody(self):
        """Post User. Empty Body Given"""
        createUserResponse = Helper().createUser(data = {})
        compareStatusCodes(self, createUserResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        Helper().deleteUser(self.userID)



