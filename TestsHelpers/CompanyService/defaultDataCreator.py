from json import load

def Company():
    data = dict()
    with open('TestsHelpers/CompanyService/JsonFiles/Company.json') as data_file:
        data = load(data_file)

    return data

def CompanyUpdate():
    data = dict()
    with open('TestsHelpers/CompanyService/JsonFiles/CompanyUpdate.json') as data_file:
        data = load(data_file)

    return data
