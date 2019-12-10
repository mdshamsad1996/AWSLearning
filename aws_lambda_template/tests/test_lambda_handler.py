"""
    Testing of lambda_handler.py

"""
import unittest
from src.lambda_handler import get_response


class TestGetResponse(unittest.TestCase):
    '''
    TestingForResponse class
    '''
    def test_get_response_for_existing_url(self):
        '''
         testing for existence url
        '''

        expected_response = 'Success!'
        received_response = get_response("https://www.google.com/")

        self.assertEqual(expected_response, received_response)

    def test_get_response_for_nonexisting_url(self):
        '''
         Testing for non existence url
        '''
        url = "https://github.com/kohli/python-unittest-classroom"
        expected_response = 'HTTP error occurred: 404 Client Error: Not Found for url: ' + url
        received_response = get_response(url)  # pylint: disable=W0703

        self.assertEqual(expected_response, received_response)

    def test_get_response_for_invalid_url(self):
        '''
         Testing for invalid url
        '''
        url = "httlsps://github.com/python-unittest-classroom"

        expected_response = "Other error occurred: No connection adapters were found for " + "'" + url + "'"              # pylint: disable=C0301
        received_response = get_response(url)

        self.assertEqual(expected_response, received_response)
