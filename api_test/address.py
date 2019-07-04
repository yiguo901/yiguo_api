import requests
from unittest import TestCase

class AddressTest(TestCase):
    def test_add(self):
        url = 'http://10.35.162.24:8003/address/add/?token='+'b07a1df334054c5e8179ca89ff9197fc'
        data = {"data":[
            {'name': "disen"},
            {'address':'lirenkeji'}
        ]}
        resp = requests.post(url, json=data)
        print(resp.json())

