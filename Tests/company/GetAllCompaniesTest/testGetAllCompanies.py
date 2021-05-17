from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.CompanyService.defaultDataCreator import *
from ....TestsHelpers.CompanyService.helper import Helper as helper
from ....TestsHelpers.CompanyService.comparator import CompanyResponse as Comaprator
from ....TestsHelpers.CompanyService.validator import CompanyResponse as Validator
from ....TestsHelpers.CompanyService import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import *
from ....TestsHelpers.TestsUtils.randomStuff import *

class TestGetAllCompanies(TestCase):

    def setUp(self):
        self.createCompanyData = Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.createCompanyResponse = helper().createCompany(self.createCompanyData).json()
        self.companyID = self.createCompanyResponse[constants.companyID]

    def testGetAllCompanies(self):
        """Get All Companies"""
        getAllCompaniesResponse = helper().getCompanies()
        compareStatusCodes(self, getAllCompaniesResponse.status_code, HTTPStatus.OK)

    def testGetAllCompaniesLimitAndOffset(self):
        """Get All Companies. Limit and offset given """
        getAllCompaniesResponse = helper().getCompanies(limit = 10 , offset = 2)
        compareStatusCodes(self, getAllCompaniesResponse.status_code, HTTPStatus.OK)

    def tearDown(self):
        helper().deleteCompany(self.companyID)
