from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as CompanyServiceHelper
from ....TestsHelpers.Service.comparator import CompanyResponse as Comaprator
from ....TestsHelpers.Service.validator import CompanyResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomUUID4, randomWord, randomNumber

class TestGetCompanyById(TestCase):

    def setUp(self):
        self.createCompanyData = defaultDataCreator.Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData).json()
        self.companyID = self.createCompanyResponse[constants.companyID]

    def testGetCompany(self):
        """Get Company"""
        getComanyResponse = CompanyServiceHelper().getCompany(companyID = self.companyID)
        compareStatusCodes(self, getComanyResponse.status_code, HTTPStatus.OK)

        testing = getComanyResponse.json()
        expected = self.createCompanyResponse

        Validator(self, testing)\
            .name()\
            .address()\
                .city()\
                .street()\
                .postalCode()\
                .country()\
                .back()

        Comaprator(self, testing, expected)\
            .companyID()\
            .name()\
            .address()\
                .city()\
                .street()\
                .postalCode()\
                .country()\
                .back()

    def testGetCompanyNonExistingCompany(self):
        """Get Company. Non Existing Company"""
        getCompanyResponse = CompanyServiceHelper().getCompany(companyID = randomUUID4())
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.NOT_FOUND)

    def testGetCompanyDeleted(self):
        """Get Company. Company Has Been Deleted"""
        CompanyServiceHelper().deleteCompany(self.companyID)
        getCompanyResponse = CompanyServiceHelper().getCompany(companyID = self.companyID)
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.NOT_FOUND)
    
    def testGetCompanyIdAsString(self):
        """Get Company. Company Id Is String Type"""
        getCompanyResponse = CompanyServiceHelper().getCompany(companyID = randomWord(17))
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetCompanyIdAsInt(self):
        """Get Company. Company Id Is Integer Type"""
        getCompanyResponse = CompanyServiceHelper().getCompany(companyID = randomNumber(1,100))
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetCompanyIdAsArray(self):
        """Get Company. Company Id Is Array Type"""
        getCompanyResponse = CompanyServiceHelper().getCompany(companyID = ["Ania"])
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
    
    def testGetCompanyIdAsDict(self):
        """Get Company. Company Id Is Dictionary Type"""
        getCompanyResponse = CompanyServiceHelper().getCompany(companyID = {"Ania": "Bania"})
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetCompanyIdAsBoolen(self):
        """Get Company. Company Id Is Boolen Type"""
        getCompanyResponse = CompanyServiceHelper().getCompany(companyID = True)
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        CompanyServiceHelper().deleteCompany(self.companyID)