from unittest import TestCase
from http import HTTPStatus

from ....TestsHelpers.Service.helper import Helper as Helper

from ....TestsHelpers.TestsUtils.compareStatusCodes import compareStatusCodes

class TestGetVersion(TestCase):

    def testGetVersion(self):
        "Get Version"
        getVersionResponse = Helper().getVersion()
        compareStatusCodes(self, getVersionResponse.status_code, HTTPStatus.OK)