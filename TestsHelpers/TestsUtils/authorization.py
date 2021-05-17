import jwt
from .randomStuff import *
from .mainCreator import MainCreator
from .authorizationConstants import *

class Authorization(MainCreator):
    def __init__(self, data = defaultPayload, key = "secret", algorithm = 'HS256', parent = None):
        self.data = data
        self.key = key
        self.algorithm = algorithm
        self.parent = parent

    def aud(self, value):
        return self.modify(aud, value)
    
    def aud(self, value):
        return self.modify(aud, value)
    
    def clientID(self, value):
        return self.modify(clientID, value)
    
    def companyID(self, value):
        return self.modify(companyID, value)
    
    def exp(self, value):
        return self.modify(exp, value)
    
    def iat(self, value):
        return self.modify(iat, value)
    
    def ip(self, value):
        return self.modify(ip, value)
    
    def iss(self, value):
        return self.modify(iss, value)
    
    def jti(self, value):
        return self.modify(jti, value)
    
    def scp(self, value):
        return self.modify(scp, value)
    
    def scope(self, value):
        return self.modify(scope, value)
    
    def storeID(self, value):
        return self.modify(storeID, value)
    
    def sub(self, value):
        return self.modify(sub, value)
    
    def userID(self, value):
        return self.modify(userID, value)
    
    def allUserRoles(self, value):
        return self.modify(userRoles, value)

    def addUserRole(self):
        return self.addArrayElement(userRoles, UserRoles)

    def changeUserRole(self, index):
        return self.changeArrayElement(userRoles, index, UserRoles)

    def removeUserRoles(self, index):
        return self.removeArrayElement(userRoles, index)

    def addUserRoleV2(self):
        return self.addArrayElement(userRoles, UserRolesV2)

    def changeUserRoleV2(self, index):
        return self.changeArrayElement(userRoles, index, UserRolesV2)
    
    def returnToken(self):
        token = jwt.encode(self.data, self.key, algorithm = self.algorithm)
        return token.decode('utf-8')

    def returnHeaders(self):
        return {'Authorization': 'Bearer ' + self.returnToken()}
            
    def back(self):
        return self.parent
    
class UserRoles(MainCreator):
    def __init__(self, data = defaultUserRoles, parent = None):
        self.data = data
        self.parent = parent
 
    def companyID(self, value):
        return self.modify(companyID, value)
    
    def roles(self, value):
        return self.modify(roles, value)
    
    def back(self):
        return self.parent

    
class UserRolesV2(MainCreator):
    def __init__(self, data = defaultUserRolesV2, parent = None):
        self.data = data
        self.parent = parent
 
    def companyIDs(self, value):
        return self.modify(companyIDs, value)
    
    def role(self, value):
        return self.modify(role, value)
    
    def back(self):
        return self.parent