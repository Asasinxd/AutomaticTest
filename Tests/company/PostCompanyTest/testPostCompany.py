from os import name
from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as CompanyServiceHelper
from ....TestsHelpers.Service.comparator import CompanyResponse as Comaprator
from ....TestsHelpers.Service.validator import CompanyResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomWord, randomNumber

class TestPostCompany(TestCase):

    def setUp(self):
        self.createCompanyData = defaultDataCreator.Company()
        self.companyID = None
        self.createCompanyData[constants.name] = randomWord(17)
    
    def testPostCompany(self):
        """Post Company"""
        createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.CREATED)

        testing = createCompanyResponse.json()
        expected = self.createCompanyData

        Validator(self, testing)\
            .companyID()\
            .name()\
            .address()\
                .city()\
                .street()\
                .postalCode()\
                .country()\
                .back()

        self.companyID = testing[constants.companyID]

        Comaprator(self, testing, expected)\
            .name()\
            .address()\
                .allFileds()\
                .back()

    def testPostCompanyAlreadyExist(self):
        """Post Company. Company Already Exist"""
        createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData)
        createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.CONFLICT)

    def testPostCompanyWithoutName(self):
        """Post Company. Without Name"""
        del self.createCompanyData[constants.name]

        createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
    
    def testPostCompanyNameAsInt(self):
        """Post Company. Name As Integer Type"""
        self.createCompanyData[constants.name] = randomNumber(1,100)

        createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostCompanyNameAsArray(self):
        """Post Company. Name As Array Type"""
        self.createCompanyData[constants.name] = ["ania"]

        createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostCompanyNameAsDict(self):
        """Post Company. Name As Dictionary Type"""
        self.createCompanyData[constants.name] = {"bania":"10"}

        createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostCompanyNameAsBoolen(self):
        """Post Company. Name As Bool Type"""
        self.createCompanyData[constants.name] = True

        createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostCompanyOnlyName(self):
        """Post Company. Only Name Given"""
        del self.createCompanyData[constants.address]

        createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostCompanyWithoutBody(self):
        """Post Company. No Body Given"""
        createCompanyResponse = CompanyServiceHelper().createCompany(data = {})
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testPostCompanyEmpty(self):
        """Post Company. Empty Body Given"""
        createCompanyResponse = CompanyServiceHelper().createCompany(data = None)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        CompanyServiceHelper().deleteCompany(self.companyID)