from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.CompanyService.defaultDataCreator import *
from ....TestsHelpers.CompanyService.helper import Helper as helper
from ....TestsHelpers.CompanyService.comparator import CompanyResponse as Comaprator
from ....TestsHelpers.CompanyService.validator import CompanyResponse as Validator
from ....TestsHelpers.CompanyService import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import *
from ....TestsHelpers.TestsUtils.randomStuff import *

class TestDeleteCompany(TestCase):

    def setUp(self):
        self.createCompanyData = Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.createCompanyResponse = helper().createCompany(self.createCompanyData).json()
        self.companyID = self.createCompanyResponse[constants.companyID]

    def testDeleteCompany(self):
        deleteCompanyResponse = helper().deleteCompany(companyID = self.companyID)
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.NO_CONTENT)

    def testDeleteCompanyAlreadyDeleted(self):
        deleteCompanyResponse = helper().deleteCompany(companyID = self.companyID)
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.NO_CONTENT)
        deleteCompanyResponse = helper().deleteCompany(companyID = self.companyID)
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteCompanyDoesNotExist(self):
        deleteCompanyResponse = helper().deleteCompany(companyID = randomUUID4())
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.NOT_FOUND)

    def testDeleteCompanyWithEmptyId(self):
        deleteCompanyResponse = helper().deleteCompany('')
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def testDeleteCompanyIdAsString(self):
        deleteCompanyResponse = helper().deleteCompany(companyID = randomWord(17))
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteCompanyIdAsInt(self):
        deleteCompanyResponse = helper().deleteCompany(companyID = randomNumber(1,100))
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteCompanyIdAsBoolen(self):
        deleteCompanyResponse = helper().deleteCompany(companyID = True)
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteCompanyIdAsArray(self):
        deleteCompanyResponse = helper().deleteCompany(companyID = ["Ania"])
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def testDeleteCompanyIdAsDict(self):
        deleteCompanyResponse = helper().deleteCompany(companyID = {"Ania" : "Bania"})
        compareStatusCodes(self, deleteCompanyResponse.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)

    def tearDown(self):
        helper().deleteCompany(self.companyID)