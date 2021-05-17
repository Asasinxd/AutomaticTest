class MainCreator():

    def modify(self, field, value):
        self.data[field] = value
        if value == None:
            del self.data[field]
        return self
    
    def addArrayElement(self, field, cre):
        self.data[field].append(dict())
        return cre(self.data[field][len(self.data[field]) -1], self)

    def changeArrayElement(self, field, index, cre):
        return cre(self.data[field][index], self)

    def modifyByCreator(self, field, cre):
        return cre(self.data[field], self)

    def removeArrayElement(self, field, index):
        del self.data[field][index]
        return self