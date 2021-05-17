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
    