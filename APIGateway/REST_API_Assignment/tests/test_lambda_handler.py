"""Test case for Http_respondse"""

import unittest
from src.http_response import HttpResponse


class TestGetResponse(unittest.TestCase):
    """Testing APIGateway for custom token authorization"""

    def test_get_http_reponse_status_code_for_valid_authorization(self):
        """Testing status code for allow value of authorization"""

        resp = HttpResponse()

        http_response = resp.get_http_reponse('allow')
        expected_status_code = 200
        received_status_code = http_response.status_code
        self.assertEqual(expected_status_code, received_status_code)

    def test_message_for_valid_authorization(self):
        """Testing message for allow value of authorization"""

        resp = HttpResponse()

        http_response = resp.get_http_reponse('allow')
        expected_message = 'Hello World!'
        received_message = http_response.text

        self.assertEqual(expected_message, received_message)

    def test_status_code_code_for_deny_value(self):
        """Testing status code for allow value of authorization"""

        resp = HttpResponse()
        http_response = resp.get_http_reponse('deny')
        expected_status_code = 403
        received_status_code = http_response.status_code
        self.assertEqual(expected_status_code, received_status_code)

    def test_status_code_code_for_invalid_authorization_value(self):

        """Testing status code for allow value of authorization"""

        resp = HttpResponse()
        http_response = resp.get_http_reponse('shshh')
        expected_status_code = 401
        received_status_code = http_response.status_code
        self.assertEqual(expected_status_code, received_status_code)

    def test_status_code_code_for_empty_authorization_value(self):
        """Testing status code for allow value of authorization"""

        resp = HttpResponse()
        http_response = resp. get_http_reponse()
        expected_status_code = 401
        received_status_code = http_response.status_code
        self.assertEqual(expected_status_code, received_status_code)
