class MainValidator():
    def __init__(self, test):
        self.test = test

    def isExist(self, field, errorMsg = ""):
        self.test.assertIn(field, self.testing, f"Not existing {field} field. {errorMsg}")

    def validateIndex(self, field, index):
        self.test.assertTrue(index >= 0 and index < len(self.testing[field]), f"Index of {field} field out of range.")

    def equal(self, expected, field, errorMsg = ""):
        self.isExist(field)
        if expected != None:
            self.test.assertEqual(self.testing[field], expected, f"The {field} field was incorrect. {errorMsg}")
        return self

    def len(self, field, expectedLen, errorMsg = ""):
        self.isExist(field)
        fieldLen = len(self.testing[field])
        self.test.assertEqual(fieldLen, expectedLen, f"The '{field}' should have size {expectedLen} instead of {fieldLen}. {errorMsg}")
        return self
    
    def equalAll(self, expected, errorMsg = ""):
        self.test.assertEqual(self.testing, expected, f"Not Equal structures. {errorMsg}")
        return self

    def equalByValidator(self, field, val):
        return val(self.test, self.testing[field], self)

    def equalArrayByValidator(self, field, index, val):
        self.validateIndex(field, index)
        return val(self.test, self.testing[field][index], self)