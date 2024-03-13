import os
import sys

base_path = os.getcwd()
sys.path.append(base_path)
from base.base_request import base_requests
import json
import mock
import unittest


def read_json():
    with open(base_path + r'\config\user_data.json') as f:
        data = json.load(f)
    return data

def get_value(key):
    data = read_json()
    return data[key]

class Testcase(unittest.TestCase):
    def test_upper(self):
        url = "https://httpbin.org/cookies"

        mock_method = mock.Mock(return_value=get_value("/cookies")["data"])
        base_requests.run_main = mock_method

        res = base_requests.run_main(method='GET', url=url)
        self.assertEquals(res['cookie']['errorcode'], '1')


if __name__ == "__main__":
    unittest.main()
