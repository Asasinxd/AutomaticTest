from ..TestsUtils.mainComparator import MainComparator
from .constants import *

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

    def back(self):
        return self.parent