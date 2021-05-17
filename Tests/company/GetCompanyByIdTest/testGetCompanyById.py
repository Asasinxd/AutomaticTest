from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.CompanyService.defaultDataCreator import *
from ....TestsHelpers.CompanyService.helper import Helper as helper
from ....TestsHelpers.CompanyService.comparator import CompanyResponse as Comaprator
from ....TestsHelpers.CompanyService.validator import CompanyResponse as Validator
from ....TestsHelpers.CompanyService import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import *
from ....TestsHelpers.TestsUtils.randomStuff import *

class TestGetCompanyById(TestCase):

    def setUp(self):
        self.createCompanyData = Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.createCompanyResponse = helper().createCompany(self.createCompanyData).json()
        self.companyID = self.createCompanyResponse[constants.companyID]

    def testGetCompany(self):
        """Get Company"""
        getComanyResponse = helper().getCompany(companyID = self.companyID)
        compareStatusCodes(self, getComanyResponse.status_code, HTTPStatus.OK)

        testing = getComanyResponse.json()
        expected = self.createCompanyResponse

        Comaprator(self, testing, expected)\
            .companyID()\
            .name()\
            .address()\
                .allFileds()\
                .back()

    def testGetCompanyNonExistingCompany(self):
        """Get Company. Non Existing Company"""
        getCompanyResponse = helper().getCompany(companyID = randomUUID4())
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.NOT_FOUND)

    def testGetCompanyDeleted(self):
        """Get Company. Company Has Been Deleted"""
        helper().deleteCompany(self.companyID)
        getCompanyResponse = helper().getCompany(companyID = self.companyID)
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.NOT_FOUND)
    
    def testGetCompanyIdAsString(self):
        """Get Company. Company Id Is String"""
        getCompanyResponse = helper().getCompany(companyID = randomWord(17))
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetCompanyIdAsInt(self):
        """Get Company. Company Id Is Integer"""
        getCompanyResponse = helper().getCompany(companyID = randomNumber(1,100))
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetCompanyIdAsArray(self):
        """Get Company. Company Id Is Array"""
        getCompanyResponse = helper().getCompany(companyID = ["Ania"])
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
    
    def testGetCompanyIdAsDict(self):
        """Get Company. Company Id Is Dictionary"""
        getCompanyResponse = helper().getCompany(companyID = {"Ania": "Bania"})
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testGetCompanyIdAsBoolen(self):
        """Get Company. Company Id Is Boolen"""
        getCompanyResponse = helper().getCompany(companyID = True)
        compareStatusCodes(self, getCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        helper().deleteCompany(self.companyID)