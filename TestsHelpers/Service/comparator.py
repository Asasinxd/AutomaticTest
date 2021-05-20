from ..TestsUtils.mainComparator import MainComparator
from . import constants

class UserResponse(MainComparator):
    def __init__(self, test, testing, expected, parent = None):
        self.test = test
        self.testing = testing
        self.expected = expected
        self.parent = parent

    def allFields(self):
        return self.equalAll()

    def userID(self):
        return self.equal(constants.userID)
    
    def relations(self):
        return self.equal(constants.relations)
    
    def firstName(self):
        return self.equal(constants.firstName)
    
    def lastName(self):
        return self.equal(constants.lastName)
    
    def email(self):
        return self.equal(constants.email)
    
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
        return self.equal(constants.name)

    def companyID(self):
        return self.equal(constants.companyID)

    def address(self):
        return self.equalByComparator(constants.address, Address)

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
        return self.equal(constants.siteID)

    def companyID(self):
        return self.equal(constants.companyID)

    def name(self):
        return self.equal(constants.name)

    def address(self):
        return self.equalByComparator(constants.address, Address)

    def pricing(self):
        return self.equalByComparator(constants.pricing, Pricing)

class UnitResponse(MainComparator):
    def __init__(self, test, testing, expected, parent = None):
        self.test = test
        self.testing = testing
        self.expected = expected
        self.parent = parent

    def allFields(self):
        return self.equalAll()

    def unitID(self):
        return self.equal(constants.unitID)

    def siteID(self):
        return self.equal(constants.siteID)

    def name(self):
        return self.equal(constants.name)        

class Address(MainComparator):

    def __init__(self, test, testing, expected, parent = None):
        self.test = test
        self.testing = testing
        self.expected = expected
        self.parent = parent

    def allFields(self):
        return self.equalAll()
    
    def street(self):
        return self.equal(constants.street)

    def city(self):
        return self.equal(constants.city)

    def postalCode(self):
        return self.equal(constants.postalcode)

    def country(self):
        return self.equal(constants.country)

    def back(self):
        return self.parent
    

class Pricing(MainComparator):
    def __init__(self, test, testing, expected, parent = None):
        self.test = test
        self.testing = testing
        self.expected = expected
        self.parent = parent
    
    def allFields(self):
        return self.equalAll()

    def numberOfMinutes(self):
        return self.equal(constants.numberOfMinutes)

    def price(self):
        return self.equal(constants.price)

    def currency(self):
        return self.equal(constants.currency)
            
    def back(self):
        return self.parent