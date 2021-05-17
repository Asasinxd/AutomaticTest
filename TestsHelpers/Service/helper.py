import requests

from ..TestsUtils.printAll import *
from .setting import URL
from . import defaultDataCreator

class Helper():
    def __init__(self):
        self.url = URL

    def createUser(self, data = defaultDataCreator.User(), headers = dict()):
        #Create user
        url = f'{self.url}/v1/users'

        resp = requests.post(url, json = data, headers = headers)
        printAll(name = "createUser", response = resp, data = data)
        return resp

    def getUsers(self, companyID = None, siteID = None, limit = None, offset = None, headers = dict()):
        #Get users

        params = dict()
        if companyID != None: params["company_id"] = companyID
        if siteID != None: params["site_id"] = siteID
        if limit != None: params["limit"] = limit
        if offset != None: params["offset"] = offset
        url = f'{self.url}/v1/users'

        resp = requests.get(url, params = params, headers = headers)
        printAll(name = "getUsers", response = resp)
        return resp

    def getUser(self, userID, headers = dict()):
        #Get user
        url = f'{self.url}/v1/users/{userID}'

        resp = requests.get(url, headers = headers)
        printAll(name = "getUser", response = resp)
        return resp

    def updateUser(self, userID, data = defaultDataCreator.UserUpdate(), headers = dict()):
        #Update user
        url = f'{self.url}/v1/users/{userID}'

        resp = requests.patch(url, json = data, headers = headers)
        printAll(name = "updateUser", response = resp, data = data)
        return resp

    def deleteUser(self, userID, headers = dict()):
        #Delete user
        url = f'{self.url}/v1/users/{userID}'

        resp = requests.delete(url, headers = headers)
        printAll(name = "deleteUser", response = resp)
        return resp