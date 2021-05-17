class MainComparator():
    def __init__(self, test):
        self.test = test

    def isExist(self, field, errorMsg = ""):
        self.test.assertIn(field, self.testing, f"Not existing {field} field. {errorMsg}")

    def validateIndex(self, field, index):
        self.test.assertTrue(index >= 0 and index < len(self.testing[field]), f"Index of {field} field out of range.")

    def equal(self, field, errorMsg = ""):
        self.isExist(field, errorMsg)
        self.test.assertEqual(self.testing[field], self.expected[field], f"Incorrect {field} field. {errorMsg}")
        return self

    def equalAll(self, errorMsg = ""):
        self.test.assertEqual(self.testing, self.expected, f"Not Equal structures. {errorMsg}")
        return self

    def equalByComparator(self, field, cmp):
        return cmp(self.test, self.testing[field], self.expected[field], self)

    def equalArrayByComparator(self, field, index, cmp):
        self.validateIndex(field, index)
        return cmp(self.test, self.testing[field][index], self.expected[field][index], self)