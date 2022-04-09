import requests
from requests.api import head

from ..TestsUtils.printAll import *
from .setting import URL
from . import defaultDataCreator
from . import constants

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
        if companyID != None: params[constants.companyID] = companyID
        if siteID != None: params[constants.siteID] = siteID
        if limit != None: params[constants.limit] = limit
        if offset != None: params[constants.offset] = offset
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

    def createCompany(self, data =  defaultDataCreator.Company(), headers = dict()):
        #Create User
        url = f'{self.url}/v1/companies'

        resp = requests.post(url , json = data, headers = headers)
        printAll(name = "createCompany", response = resp, data = data)
        return resp

    def getCompanies(self, userID = None, limit = None, offset = None, headers = dict()):
        #Get All Companies

        params =  dict()
        if userID != None: params[constants.userID] = userID
        if limit != None: params[constants.limit] = limit
        if offset != None: params[constants.offset] = offset

        url = f'{self.url}/v1/companies'

        resp = requests.get(url, params = params, headers = headers)
        printAll(name = "getCompanies", response = resp)
        return  resp

    def getCompany(self, companyID,  headers = dict()):
        #Get Company

        url = f'{self.url}/v1/companies/{companyID}'

        resp =  requests.get(url, headers = headers)
        printAll(name = "getCompany", response = resp)
        return resp

    def updateCompany(self, comapanyID, data = defaultDataCreator.CompanyUpdate(), headers = dict()):
        #Update User

        url = f'{self.url}/v1/companies/{comapanyID}'

        resp = requests.patch(url, json = data, headers = headers)
        printAll(name = "updateCompany", response = resp, data =  data)
        return resp

    def deleteCompany(self, companyID, headers = dict()):
        #Delete Company

        url = f'{self.url}/v1/companies/{companyID}'

        resp = requests.delete(url,  headers = dict())
        printAll(name = "deleteCompany", response = resp)
        return resp

    def createSite(self, data = defaultDataCreator.Site(), headers = dict()):
        #Create site
        url = f'{self.url}/v1/sites'

        resp = requests.post(url, json = data, headers = headers)
        printAll(name = "createSite", response = resp, data = data)
        return resp

    def getSites(self, userID = None, companyID = None, limit = None, offset = None, headers = dict()):
        #Get sites

        params = dict()
        if companyID != None: params[constants.companyID] = companyID
        if userID != None: params[constants.userID] = userID
        if limit != None: params[constants.limit] = limit
        if offset != None: params[constants.offset] = offset
        url = f'{self.url}/v1/sites'

        resp = requests.get(url, params = params, headers = headers)
        printAll(name = "getSites", response = resp)
        return resp

    def getSite(self, siteID, headers = dict()):
        #Get site
        url = f'{self.url}/v1/sites/{siteID}'

        resp = requests.get(url, headers = headers)
        printAll(name = "getSite",  response = resp)
        return resp

    def updateSite(self, siteID, data = defaultDataCreator.SiteUpdate(), headers = dict()):
        #Update site
        url = f'{self.url}/v1/sites/{siteID}'

        resp = requests.patch(url, json = data, headers = headers)
        printAll(name = "updateSite", response = resp, data = data)
        return resp

    def deleteSite(self, siteID, headers = dict()):
        #Delete site
        url = f'{self.url}/v1/sites/{siteID}'
        
        resp = requests.delete(url, headers = headers)
        printAll(name = "deleteSite", response = resp)
        return resp

    def createUnit(self, data = defaultDataCreator.Unit(), headers = dict()):
        #Create unit
        url = f'{self.url}/v1/units'

        resp = requests.post(url, json = data, headers = headers)
        printAll(name = "createUnit", response = resp, data = data)
        return resp
    
    def getUnits(self, userID = None, siteID = None, limit = None, offset = None, headers = dict()):
        #Get Units

        params = dict()
        if userID != None: params[constants.userID] = userID
        if siteID != None: params[constants.siteID] = siteID
        if limit != None: params[constants.limit] = limit
        if offset != None: params[constants.offset] = offset
        url = f'{self.url}/v1/units'

        resp = requests.get(url, params = params, headers=headers)
        printAll(name = "getUnits", response = resp)
        return resp

    def getUnit(self, unitID, headers = dict()):
        #Get Unit
        url = f'{self.url}/v1/units/{unitID}'

        resp = requests.get(url, headers = headers)
        printAll(name = "getUnit", response = resp)
        return resp

    def updateUnit(self, unitID, data = defaultDataCreator.UnitUpdate(), headers = dict()):
        #Update Unit
        url = f'{self.url}/v1/units/{unitID}'

        resp = requests.patch(url, json = data, headers = headers)
        printAll(name = "updateUnit", response = resp, data = data)
        return resp

    def deleteUnit(self, unitID, headers = dict()):
        #Delete Uite
        url = f'{self.url}/v1/units/{unitID}'

        resp = requests.delete(url, headers = headers)
        printAll(name = "deleteUnit", response = resp)
        return resp

    def createReservation(self, data = defaultDataCreator.Reservation(), headers = dict()):
        #Create reservation
        url = f'{self.url}/v1/reservations'

        resp = requests.post(url, json = data, headers = headers)
        printAll(name = "createReservation", response = resp, data = data)
        return resp

    def getReservations(self, userID = None, unitID = None, limit = None, offset = None, headers = dict()):
        #Get reservations

        params = dict()

        if userID != None: params[constants.userID] = userID
        if unitID != None: params[constants.unitID] = unitID
        if limit != None: params[constants.limit] = limit
        if offset != None: params[constants.offset] = offset
        url = f'{self.url}/v1/reservations'

        resp = requests.get(url, params = params, headers = headers)
        printAll(name = "getReservations", response = resp)
        return resp

    def getReservation(self, reservationID, headers = dict()):
        #Get reservation
        url = f'{self.url}/v1/reservations/{reservationID}'

        resp = requests.get(url, headers = headers)
        printAll(name = "getReservation", response = resp)
        return resp

    def updateReservation(self, reservationID, data = defaultDataCreator.ReservationUpdate(), headers = dict()):
        #Update reservation
        url = f'{self.url}/v1/reservations/{reservationID}'

        resp = requests.patch(url, json = data, headers = headers)
        printAll(name = "updateReservation", response = resp)
        return resp

    def deleteReservation(self, reservationID, headers = dict()):
        #Delete reservation
        url = f'{self.url}/v1/reservation/{reservationID}'

        resp = requests.delete(url, headers = headers)
        printAll(name = "deleteReservation", response = resp)
        return resp

    def getVersion(self, headers = dict()):
        #Get Version
        url = f'{self.url}/v1/version'

        resp = requests.get(url, headers = headers)
        printAll(name = "getVersion", response = resp)
        return resp
    
    def getHealth(self, headers = dict()):
        #Get Health
        url = f'{self.url}/v1/health'

        resp = requests.get(url, headers = headers)
        printAll(name = "getHealth", response = resp)
        return resp