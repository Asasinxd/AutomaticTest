from ..TestsUtils.mainValidator import MainValidator
from .constants import *

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

    def back(self):
        return self.parent