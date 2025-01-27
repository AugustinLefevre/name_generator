from main.web_client import web_client
import unittest

class test_web_client(unittest.TestCase):

    wc = web_client()

    def test_get_request(self):
        url = "https://www.larousse.fr/dictionnaires/francais/test/77497"
        response = self.wc.set_url(url).send_get_request().get_response()
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(self.wc.get_content())

if __name__ == '__main__':
    unittest.main()


