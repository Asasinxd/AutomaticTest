from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service import defaultDataCreator
from ....TestsHelpers.Service.helper import Helper as CompanyServiceHelper
from ....TestsHelpers.Service.comparator import CompanyResponse as Comaprator
from ....TestsHelpers.Service.validator import CompanyResponse as Validator
from ....TestsHelpers.Service import constants

 
from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes
from ....TestsHelpers.TestsUtils.randomStuff import randomWord

class TestGetAllCompanies(TestCase):

    def setUp(self):
        self.createCompanyData = defaultDataCreator.Company()
        self.createCompanyData[constants.name] = randomWord(17)
        self.createCompanyResponse = CompanyServiceHelper().createCompany(self.createCompanyData).json()
        self.companyID = self.createCompanyResponse[constants.companyID]

    def testGetAllCompanies(self):
        """Get All Companies"""
        getAllCompaniesResponse = CompanyServiceHelper().getCompanies()
        compareStatusCodes(self, getAllCompaniesResponse.status_code, HTTPStatus.OK)

    def testGetAllCompaniesLimitAndOffset(self):
        """Get All Companies. Limit And Offset given """
        getAllCompaniesResponse = CompanyServiceHelper().getCompanies(limit = 10 , offset = 2)
        compareStatusCodes(self, getAllCompaniesResponse.status_code, HTTPStatus.OK)

    def tearDown(self):
        CompanyServiceHelper().deleteCompany(self.companyID)
