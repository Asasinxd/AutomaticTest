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
    