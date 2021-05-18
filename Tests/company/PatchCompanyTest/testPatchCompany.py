from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.CompanyService import defaultDataCreator
from ....TestsHelpers.CompanyService.helper import Helper as CompanyServiceHelper
from ....TestsHelpers.CompanyService.comparator import CompanyResponse as Comaprator
from ....TestsHelpers.CompanyService.validator import CompanyResponse as Validator
from ....TestsHelpers.CompanyService import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomWord, randomUUID4

class TestPatchCompany(TestCase):

    def setUp(self):
        self.createCompanyData = defaultDataCreator.Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData).json()
        self.companyID = self.createCompanyResponse[constants.companyID]
        self.upadateCompany = defaultDataCreator.CompanyUpdate()

    def testPatchCompany(self):
        """Patch Company"""
        upadateCompanyResponse = CompanyServiceHelper().updateCompany(self.companyID, self.upadateCompany)
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
        """Patch Company. Non Existing Company"""
        upadateCompanyResponse = CompanyServiceHelper().updateCompany(randomUUID4(), self.upadateCompany)
        compareStatusCodes(self, upadateCompanyResponse.status_code, HTTPStatus.NOT_FOUND)

    def testPatchCompanyNameAlreadyExist(self):
        """Patch Company. Name Already Exist"""
        self.upadateCompany[constants.name] = self.createCompanyData[constants.name]
        upadateCompanyResponse = CompanyServiceHelper().updateCompany(self.companyID, self.upadateCompany)
        compareStatusCodes(self, upadateCompanyResponse.status_code, HTTPStatus.CONFLICT)

    def testPatchCompanyWithEmptyBody(self):
        """Patch Company. Empty Body Given"""
        upadateCompanyResponse = CompanyServiceHelper().updateCompany(self.companyID, data = {})
        compareStatusCodes(self, upadateCompanyResponse.status_code, HTTPStatus.OK)

        testing = upadateCompanyResponse.json()

        Comaprator(self, testing, self.createCompanyData)\
            .name()\
            .address()\
                .city()\
                .street()\
                .postalCode()\
                .back()

    def testPatchCompanyWithoutBody(self):
        """Patch Company. No Body Given"""
        upadateCompanyResponse = CompanyServiceHelper().updateCompany(self.companyID, data = None)
        compareStatusCodes(self, upadateCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        CompanyServiceHelper().deleteCompany(self.companyID)