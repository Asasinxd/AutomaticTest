from ..TestsUtils.mainValidator import MainValidator
from .constants import *

class UserResponse(MainValidator):
    def __init__(self, test, testing, parent = None):
        self.test = test
        self.testing = testing
        self.parent = parent

    def allFields(self, expected = None):
        return self.equalAll(expected)

    def userID(self, expected = None):
        return self.equal(expected, userID)
    
    def relations(self, expected = None):
        return self.equal(expected, relations)
    
    def firstName(self, expected = None):
        return self.equal(expected, firstName)
    
    def lastName(self, expected = None):
        return self.equal(expected, lastName)
    
    def email(self, expected = None):
        return self.equal(expected, email)
    
    def back(self):
        return self.parent

class CompanyResponse(MainValidator):
    def __init__(self, test, testing, parent = None):
        self.test = test
        self.testing = testing
        self.parent = parent

    def allFileds(self, expected = None):
        return self.equalAll(expected)

    def name(self, expected = None):
        return self.equal(expected, name)

    def companyID(self, expected = None):
        return self.equal(expected, companyID)

    def address(self):
        return self.equalByValidator(address, Address)

    def back(self):
        return self.parent

class SiteResponse(MainValidator):
    def __init__(self, test, testing, parent = None):
        self.test = test
        self.testing = testing
        self.parent = parent

    def allFields(self, expected = None):
        return self.equalAll(expected)

    def siteID(self, expected = None):
        return self.equal(expected, siteID)

    def units(self):
        return self.equalByValidator(units, UnitResponse)

    def companyID(self, expected = None):
        return self.equal(expected, companyID)

    def name(self, expected = None):
        return self.equal(expected, name)

    def address(self):
        return self.equalByValidator(address, Address)

class UnitResponse(MainValidator):
    def __init__(self, test, testing, parent = None):
        self.test = test
        self.testing = testing
        self.parent = parent

    def allFileds(self, expected = None):
        return self.equalAll(expected)

    def unitID(self, expected = None):
        return self.equal(expected, unitID)

    def siteID(self, expected = None):
        return self.equal(expected, siteID)

    def name(self, expected = None):
        return self.equal(expected, name)

class Address(MainValidator):

    def __init__(self, test, testing, parent = None):
        self.test = test
        self.testing = testing
        self.parent = parent

    def allFileds(self, expected = None):
        return self.equalAll(expected)
    
    def street(self, expected = None):
        return self.equal(expected, street)

    def city(self, expected = None):
        return self.equal(expected, city)

    def postalCode(self, expected = None):
        return self.equal(expected, postalcode)

    def country(self, expected = None):
        return self.equal(expected, country)

    def back(self):
        return self.parent
    