from ..TestsUtils.mainValidator import MainValidator
from . import constants

class UserResponse(MainValidator):
    def __init__(self, test, testing, parent = None):
        self.test = test
        self.testing = testing
        self.parent = parent

    def allFields(self, expected = None):
        return self.equalAll(expected)

    def userID(self, expected = None):
        return self.equal(expected, constants.userID)
    
    def relations(self, expected = None):
        return self.equal(expected, constants.relations)
    
    def firstName(self, expected = None):
        return self.equal(expected, constants.firstName)
    
    def lastName(self, expected = None):
        return self.equal(expected, constants.lastName)
    
    def email(self, expected = None):
        return self.equal(expected, constants.email)
    
    def back(self):
        return self.parent

class CompanyResponse(MainValidator):
    def __init__(self, test, testing, parent = None):
        self.test = test
        self.testing = testing
        self.parent = parent

    def allFields(self, expected = None):
        return self.equalAll(expected)

    def name(self, expected = None):
        return self.equal(expected, constants.name)

    def companyID(self, expected = None):
        return self.equal(expected, constants.companyID)

    def address(self):
        return self.equalByValidator(constants.address, Address)

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
        return self.equal(expected, constants.siteID)

    def units(self):
        return self.equalByValidator(constants.units, UnitResponse)

    def companyID(self, expected = None):
        return self.equal(expected, constants.companyID)

    def name(self, expected = None):
        return self.equal(expected, constants.name)

    def address(self):
        return self.equalByValidator(constants.address, Address)

    def pricing(self):
        return self.equalByValidator(constants.pricing, Pricing)

class UnitResponse(MainValidator):
    def __init__(self, test, testing, parent = None):
        self.test = test
        self.testing = testing
        self.parent = parent

    def allFields(self, expected = None):
        return self.equalAll(expected)

    def unitID(self, expected = None):
        return self.equal(expected, constants.unitID)

    def siteID(self, expected = None):
        return self.equal(expected, constants.siteID)

    def name(self, expected = None):
        return self.equal(expected, constants.name)
    
    def back(self):
        return self.parent

class Address(MainValidator):

    def __init__(self, test, testing, parent = None):
        self.test = test
        self.testing = testing
        self.parent = parent

    def allFields(self, expected = None):
        return self.equalAll(expected)
    
    def street(self, expected = None):
        return self.equal(expected, constants.street)

    def city(self, expected = None):
        return self.equal(expected, constants.city)

    def postalCode(self, expected = None):
        return self.equal(expected, constants.postalcode)

    def country(self, expected = None):
        return self.equal(expected, constants.country)

    def back(self):
        return self.parent

class Pricing(MainValidator):
    def __init__(self, test, testing, parent = None):
        self.test = test
        self.testing = testing
        self.parent = parent

    def allFields(self, expected = None):
        return self.equalAll(expected)

    def numberOfMinutes(self, expected = None):
        return self.equal(expected, constants.numberOfMinutes)

    def price(self, expected = None):
        return self.equal(expected, constants.currency)

    def back(self):
        return self.parent    