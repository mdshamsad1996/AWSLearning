"""Test case for Http_respondse"""

import unittest
from src.http_response import HttpResponse


class TestGetResponse(unittest.TestCase):
    """Testing APIGateway for custom token authorization"""

    def test_get_http_reponse_status_code_for_valid_authorization(self):
        """Testing status code for allow value of authorization"""


        token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhkaTFtME1Ncm9KWjVqUXZzcFRnYSJ9.eyJpc3MiOiJodHRwczovL2Rldi1zOGsyaTI5aS5hdXRoMC5jb20vIiwic3ViIjoiRlRvNWZjQVc2SDYzNEk5d01sUnRUS24zVTFEMjZaSWFAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vYXV0aDAtand0LWF1dGhvcml6ZXIiLCJpYXQiOjE1ODk0OTA2NzgsImV4cCI6MTU4OTU3NzA3OCwiYXpwIjoiRlRvNWZjQVc2SDYzNEk5d01sUnRUS24zVTFEMjZaSWEiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.Z7e4_rdOLA9Uxf1U5dbZMnP54BYhcSEH7nG-DMTyhegfz0kDxy5GciCucwdQpz51PjqMqx6N7hnbye9UsC_rrvJakeidIvcSK2HAeBZb_WvuHnV_9ViyoVSD0ywxUX515s7h1vfy43Eul4c3AX3NGdVAJT9NcF7G8-IqAGV5HfQp19wHzXaUn9_CRWMuNbZQG9TxB0sGRcP3VIklXrA4SHl2Xy66NzupIngwYMyiHQLubH_k1f2Sha-qaQkG0d-KCp5F2AX-phdaCFlhMrHPfXVLjX8V2wMaYB8p1BvRc9xUn0lBDIicoE9rKds_am98pPRpUSQlFczOT1Bjq2izYg"
        resp = HttpResponse()

        http_response = resp.get_http_reponse(token)
        expected_status_code = 200
        received_status_code = http_response.status_code
        self.assertEqual(expected_status_code, received_status_code)



    def test_status_code_code_for_deny_value(self):
        """Testing status code for allow value of authorization"""

        resp = HttpResponse()
        http_response = resp.get_http_reponse()
        expected_status_code = 403
        received_status_code = http_response.status_code
        self.assertEqual(expected_status_code, received_status_code)
