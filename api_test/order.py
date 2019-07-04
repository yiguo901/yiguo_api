import requests
from unittest import TestCase


class TOrder(TestCase):
    def test_add_order(self):
        url = 'http://10.35.162.136:8003/order/'
        form_data = {
            'user_id': 10001
        }
        resp = requests.post(url, data=form_data)
        print(resp.json())
