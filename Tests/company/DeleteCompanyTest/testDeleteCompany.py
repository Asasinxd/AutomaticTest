from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as CompanyServiceHelper
from ....TestsHelpers.Service.comparator import CompanyResponse as Comaprator
from ....TestsHelpers.Service.validator import CompanyResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomWord, randomNumber, randomUUID4

class TestDeleteCompany(TestCase):

    def setUp(self):
        self.createCompanyData = defaultDataCreator.Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData).json()
        self.companyID = self.createCompanyResponse[constants.companyID]

    def testDeleteCompany(self):
        """Delete Company"""
        deleteCompanyResponse = CompanyServiceHelper().deleteCompany(companyID = self.companyID)
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.NO_CONTENT)

    def testDeleteCompanyAlreadyDeleted(self):
        """Delete Company. Already Deleted Company"""
        deleteCompanyResponse = CompanyServiceHelper().deleteCompany(companyID = self.companyID)
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.NO_CONTENT)
        deleteCompanyResponse = CompanyServiceHelper().deleteCompany(companyID = self.companyID)
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteCompanyDoesNotExist(self):
        """Delete User. Non Existing Company"""
        deleteCompanyResponse = CompanyServiceHelper().deleteCompany(companyID = randomUUID4())
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteCompanyWithEmptyId(self):
        """Delete User. Empty Company Id"""
        deleteCompanyResponse = CompanyServiceHelper().deleteCompany(companyID = '')
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def testDeleteCompanyIdAsString(self):
        """Delete User. Id Is String Type"""
        deleteCompanyResponse = CompanyServiceHelper().deleteCompany(companyID = randomWord(17))
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteCompanyIdAsInt(self):
        """Delete User. Id is Integer Type"""
        deleteCompanyResponse = CompanyServiceHelper().deleteCompany(companyID = randomNumber(1,100))
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteCompanyIdAsBoolen(self):
        """Delete User. Id Is Boolen Type"""
        deleteCompanyResponse = CompanyServiceHelper().deleteCompany(companyID = True)
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteCompanyIdAsArray(self):
        """Delete User. Id Is Array Type"""
        deleteCompanyResponse = CompanyServiceHelper().deleteCompany(companyID = ["Ania"])
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteCompanyIdAsDict(self):
        """Delete User. Id Is Dictionary Type"""
        deleteCompanyResponse = CompanyServiceHelper().deleteCompany(companyID = {"Ania" : "Bania"})
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        CompanyServiceHelper().deleteCompany(self.companyID)