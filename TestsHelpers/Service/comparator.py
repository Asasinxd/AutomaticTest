from ..TestsUtils.mainComparator import MainComparator
from .constants import *

class UserResponse(MainComparator):
    def __init__(self, test, testing, expected, parent = None):
        self.test = test
        self.testing = testing
        self.expected = expected
        self.parent = parent

    def allFields(self):
        return self.equalAll()

    def userID(self):
        return self.equal(userID)
    
    def relations(self):
        return self.equal(relations)
    
    def firstName(self):
        return self.equal(firstName)
    
    def lastName(self):
        return self.equal(lastName)
    
    def email(self):
        return self.equal(email)
    
    def back(self):
        return self.parent

class CompanyResponse(MainComparator):
    def __init__(self, test, testing, expected, parent = None):
        self.test = test
        self.testing = testing
        self.expected = expected
        self.parent = parent

    def allFileds(self):
        return self.equalAll()

    def name(self):
        return self.equal(name)

    def companyID(self):
        return self.equal(companyID)

    def address(self):
        return self.equalByComparator(address, Address)

    def back(self):
        return self.parent

class SiteResponse(MainComparator):
    def __init__(self, test, testing, expected, parent = None):
        self.test = test
        self.testing = testing
        self.expected = expected
        self.parent = parent

    def allFileds(self):
        return self.equalAll()

    def siteID(self):
        return self.equal(siteID)

    def companyID(self):
        return self.equal(companyID)

    def name(self):
        return self.equal(name)

    def address(self):
        return self.equalByComparator(address, Address)

class UnitResponse(MainComparator):
    def __init__(self, test, testing, expected, parent = None):
        self.test = test
        self.testing = testing
        self.expected = expected
        self.parent = parent

    def allFields(self):
        return self.equalAll()

    def unitID(self):
        return self.equal(unitID)

    def siteID(self):
        return self.equal(siteID)

    def name(self):
        return self.equal(name)        

class Address(MainComparator):

    def __init__(self, test, testing, expected, parent = None):
        self.test = test
        self.testing = testing
        self.expected = expected
        self.parent = parent

    def allFileds(self):
        return self.equalAll()
    
    def street(self):
        return self.equal(street)

    def city(self):
        return self.equal(city)

    def postalCode(self):
        return self.equal(postalcode)

    def country(self):
        return self.equal(country)

    def back(self):
        return self.parent
    