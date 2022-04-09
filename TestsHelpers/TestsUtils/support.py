from . import constants

def checkResponseData(test, testing, count=1, limit=100):
    test.assertIn(constants.count, testing, "Fail count")
    test.assertIn(constants.limit, testing, "Fail limit")
    test.assertIn(constants.elements, testing, "Fail elements")

    test.assertEqual(testing[constants.count], count, "Fail count")
    test.assertEqual(testing[constants.limit], limit, "Fail limit")
    test.assertTrue(testing[constants.count] >= len(testing[constants.elements]), "Fail count or limit")