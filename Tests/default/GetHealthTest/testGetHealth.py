from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service.helper import Helper as Helper

from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes

class TestGetHealth(TestCase):

    def testGetHealth(self):
        "Get Health"
        getHealthResponse = Helper().getHealth()
        compareStatusCodes(self, getHealthResponse.status_code, HTTPStatus.OK)