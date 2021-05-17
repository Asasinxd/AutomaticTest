from json import load
from ..TestsUtils.randomStuff import *
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