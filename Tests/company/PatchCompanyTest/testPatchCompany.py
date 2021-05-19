from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper
from ....TestsHelpers.Service.comparator import CompanyResponse as Comaprator
from ....TestsHelpers.Service.validator import CompanyResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomWord, randomUUID4

class TestPatchCompany(TestCase):

    def setUp(self):
        self.createCompanyData = defaultDataCreator.Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.createCompanyResponse = Helper().createCompany(self.createCompanyData).json()
        self.companyID = self.createCompanyResponse[constants.companyID]
        self.upadateCompany = defaultDataCreator.CompanyUpdate()

    def testPatchCompany(self):
        """Patch Company"""
        upadateCompanyResponse = Helper().updateCompany(self.companyID, self.upadateCompany)
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
        upadateCompanyResponse = Helper().updateCompany(randomUUID4(), self.upadateCompany)
        compareStatusCodes(self, upadateCompanyResponse.status_code, HTTPStatus.NOT_FOUND)

    def testPatchCompanyNameAlreadyExist(self):
        """Patch Company. Name Already Exist"""
        self.upadateCompany[constants.name] = self.createCompanyData[constants.name]
        upadateCompanyResponse = Helper().updateCompany(self.companyID, self.upadateCompany)
        compareStatusCodes(self, upadateCompanyResponse.status_code, HTTPStatus.CONFLICT)

    def testPatchCompanyWithEmptyBody(self):
        """Patch Company. Empty Body Given"""
        upadateCompanyResponse = Helper().updateCompany(self.companyID, data = {})
        compareStatusCodes(self, upadateCompanyResponse.status_code, HTTPStatus.OK)

    def testPatchCompanyWithoutBody(self):
        """Patch Company. No Body Given"""
        upadateCompanyResponse = Helper().updateCompany(self.companyID, data = None)
        compareStatusCodes(self, upadateCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        Helper().deleteCompany(self.companyID)