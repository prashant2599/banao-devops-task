import requests
import unittest

class WebsiteTestCase(unittest.TestCase):
    def test_website_load(self):
        url = 'https://atg.world/'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, "Failed to load website: %s" % url)
        print("Received response with status code: %d" % response.status_code)


if __name__ == '__main__':
    unittest.main()
