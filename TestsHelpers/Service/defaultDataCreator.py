from json import load
from . import constants
import string

def User():
    data = dict()
    with open('TestsHelpers/Service/JsonFiles/User.json') as data_file:
        data = load(data_file)
        
    return data

def UserUpdate():
    data = dict()
    with open('TestsHelpers/Service/JsonFiles/UserUpdate.json') as data_file:
        data = load(data_file)

    return data

def Company():
    data = dict()
    with open('TestsHelpers/Service/JsonFiles/Company.json') as data_file:
        data = load(data_file)

    return data

def CompanyUpdate():
    data = dict()
    with open('TestsHelpers/Service/JsonFiles/CompanyUpdate.json') as data_file:
        data = load(data_file)

    return data

def Site():
    data = dict()
    with open('TestsHelpers/Service/JsonFiles/Site.json') as data_file:
        data = load(data_file)

    return data

def SiteUpdate():
    data = dict()
    with open('TestsHelpers/Service/JsonFiles/SiteUpdate.json') as data_file:
        data = load(data_file)

    return data

def Unit():
    data = dict()
    with open('TestsHelpers/Service/JsonFiles/Unit.json') as data_file:
        data = load(data_file)

    return data

def UnitUpdate():
    data = dict()
    with open('TestsHelpers/Service/JsonFiles/UnitUpdate.json') as data_file:
        data = load(data_file)

    return data

def Reservation():
    data = dict()
    with open('TestsHelpers/Service/JsonFiles/Reservation.json') as data_file:
        data = load(data_file)

    return data

def ReservationUpdate():
    data = dict()
    with open('TestsHelpers/Service/JsonFiles/ReservationUpdate.json') as data_file:
        data = load(data_file)

    return data