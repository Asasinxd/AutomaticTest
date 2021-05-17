from socket import gethostbyname, gethostname
from datetime import datetime, timedelta
from os import getenv
from .randomStuff import *

USER_ROLES = ["super-admin", "retailer-admin", "retailer-store-admin", "retailer-sales", "brand-admin", "device-manufacturer-admin", "developer"] 
aud = "aud"
clientID = "client_id"
companyID = "company_id"
exp = "exp"
iat = "iat"
ip = "ip"
iss = "iss"
jti = "jti"
scp = "scp"
scope = "scope"
storeID = "store_id"
sub = "sub"
userID = "user_id"
userRoles = "user_roles"
roles = "roles"
role = "role"
companyIDs = "company_ids"

defaultUserRoles = {
  companyID: randomUUID4(),
  roles: USER_ROLES
}

defaultPayload = {
  aud: [
    "http://hp-miniappinapp-service.hp"
  ],
  clientID: randomUUID4(),
  companyID: randomUUID4(),
  exp: datetime.utcnow() + timedelta(seconds=60),
  iat: datetime.utcnow(),
  ip: str(gethostbyname(gethostname())),
  iss: str(getenv('host')),
  jti: randomUUID4(),
  scp: [],
  scope: [],
  storeID: randomUUID4(),
  sub: "",
  userID: randomUUID4(),
  userRoles: [defaultUserRoles]
}

defaultUserRolesV2 = {
  companyIDs: [randomUUID4()],
  role: USER_ROLES[0]
}

defaultPayloadV2 = {
  aud: [
    "http://hp-miniappinapp-service.hp"
  ],
  clientID: randomUUID4(),
  companyID: randomUUID4(),
  exp: datetime.utcnow() + timedelta(seconds=60),
  iat: datetime.utcnow(),
  ip: str(gethostbyname(gethostname())),
  iss: str(getenv('host')),
  jti: randomUUID4(),
  scp: [],
  scope: [],
  storeID: randomUUID4(),
  sub: "",
  userID: randomUUID4(),
  userRoles: [defaultUserRolesV2]
}