import requests

from ..TestsUtils.printAll import *
from .setting import URL
from . import defaultDataCreator

class Helper():
    def __init__(self):
        self.url = URL
        
    def createCompany(self, data =  defaultDataCreator.Company(), headers = dict()):
        url = f'{self.url}/v1/companies'

        resp = requests.post(url , json = data, headers = headers)
        printAll(name = "createCompany", response = resp, data = data)
        return resp

    def getCompanies(self, userID = None, limit = None, offset = None, headers = dict()):

        params =  dict()
        if userID != None: params["user_id"] = userID
        if limit != None: params["limit"] = limit
        if offset != None: params["offset"] = offset

        url = f'{self.url}/v1/companies'

        resp = requests.get(url, params = params, headers = headers)
        printAll(name = "getCompanies", response = resp)
        return  resp

    def getCompany(self, companyID,  headers = dict()):
        url = f'{self.url}/v1/companies/{companyID}'

        resp =  requests.get(url, headers = headers)
        printAll(name = "getCompany", response = resp)
        return resp

    def updateCompany(self, comapanyID, data = defaultDataCreator.CompanyUpdate(), headers = dict()):
        url = f'{self.url}/v1/companies/{comapanyID}'

        resp = requests.patch(url, json = data, headers = headers)
        printAll(name = "updateCompany", response = resp, data =  data)
        return resp

    def deleteCompany(self, companyID, headers = dict()):
        url = f'{self.url}/v1/companies/{companyID}'

        resp = requests.delete(url,  headers = dict())
        printAll(name = "deleteCompany", response = resp)
        return resp