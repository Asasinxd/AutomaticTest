from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.CompanyService.defaultDataCreator import *
from ....TestsHelpers.CompanyService.helper import Helper as helper
from ....TestsHelpers.CompanyService.comparator import Address, CompanyResponse as Comaprator
from ....TestsHelpers.CompanyService.validator import CompanyResponse as Validator
from ....TestsHelpers.CompanyService import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import *
from ....TestsHelpers.TestsUtils.randomStuff import *

class TestPatchCompany(TestCase):

    def setUp(self):
        self.createCompanyData = Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.createCompanyResponse = helper().createCompany(self.createCompanyData).json()
        self.companyID = self.createCompanyResponse[constants.companyID]
        self.upadateCompany = CompanyUpdate()

    def testPatchCompany(self):
        upadateCompanyResponse = helper().updateCompany(self.companyID, self.upadateCompany)
        compareStatusCodes(self, upadateCompanyResponse.status_code, HTTPStatus.OK)

        testing = upadateCompanyResponse.json()
        expected = self.upadateCompany

        Validator(self, testing)\
            .name()\
            .address()\
                .street()\
                .city()\
                .postalCode()\
                .back()

        Comaprator(self, testing, expected)\
            .name()\
            .address()\
                .allFileds()\
                .back()

    def testPatchCompanyNonExistingCompany(self):
        upadateCompanyResponse = helper().updateCompany(randomUUID4(), self.upadateCompany)
        compareStatusCodes(self, upadateCompanyResponse.status_code, HTTPStatus.NOT_FOUND)

    def testPatchCompanyNameAlreadyExist(self):
        self.upadateCompany[constants.name] = self.createCompanyData[constants.name]
        upadateCompanyResponse = helper().updateCompany(self.companyID, self.upadateCompany)
        compareStatusCodes(self, upadateCompanyResponse.status_code, HTTPStatus.CONFLICT)

    def tearDown(self):
        helper().deleteCompany(self.companyID)