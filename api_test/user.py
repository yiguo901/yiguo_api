import requests
from unittest import TestCase


class TUser(TestCase):
    def test_regist_code(self):
        code_url = 'http://10.35.162.136:8003/msgcode/'
        resp = requests.post(code_url, json={
            'u_phone': '18691995899'
        })
        print(resp.json())

    def test_regist(self):
        url = 'http://10.35.162.136:8003/msglogin/'
        resp = requests.post(url, json={
            'u_phone': '18691995899',
            'msg_code': '117995'
        })
        print(resp.json())

    def test_login(self):
        url = 'http://10.35.162.136:8003/loginpwd/'
        params = {
            'u_phone': '18691995899',
            'u_auth_string': '123456'
        }
        resp = requests.post(url, json=params)
        print(resp.json())