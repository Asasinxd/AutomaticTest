from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.CompanyService.defaultDataCreator import *
from ....TestsHelpers.CompanyService.helper import Helper as helper
from ....TestsHelpers.CompanyService.comparator import CompanyResponse as Comaprator
from ....TestsHelpers.CompanyService.validator import CompanyResponse as Validator
from ....TestsHelpers.CompanyService import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import *
from ....TestsHelpers.TestsUtils.randomStuff import *

class TestPostCompany(TestCase):

    def setUp(self):
        self.createCompanyData = Company()
        self.companyID = None
        self.createCompanyData[constants.name] = randomWord(17)
    
    def testPostCompany(self):
        
        createCompanyResponse = helper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.CREATED)

        testing = createCompanyResponse.json()
        expected = self.createCompanyData

        Validator(self, testing)\
            .companyID()

        self.companyID = testing[constants.companyID]

        Comaprator(self, testing, expected)\
            .name()\
            .address()\
                .allFileds()\
                .back()

    def testPostCompanyAlreadyExist(self):
        createCompanyResponse = helper().createCompany(self.createCompanyData)
        createCompanyResponse = helper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.CONFLICT)

    def testPostCompanyWithoutName(self):
        del self.createCompanyData[constants.name]

        createCompanyResponse = helper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
    
    def testPostCompanyNameAsInt(self):
        self.createCompanyData[constants.name] = randomNumber(1,100)

        createCompanyResponse = helper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostCompanyNameAsArray(self):
        self.createCompanyData[constants.name] = ["ania"]

        createCompanyResponse = helper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostCompanyNameAsDict(self):
        self.createCompanyData[constants.name] = {"bania":"10"}

        createCompanyResponse = helper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.BAD_REQUEST)

    def testPostCompanyNameAsBoolen(self):
        self.createCompanyData[constants.name] = True

        createCompanyResponse = helper().createCompany(self.createCompanyData)
        compareStatusCodes(self, createCompanyResponse.status_code, HTTPStatus.BAD_REQUEST)

    def tearDown(self):
        helper().deleteCompany(self.companyID)