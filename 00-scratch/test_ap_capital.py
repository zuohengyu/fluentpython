
import requests
import pytest

def test_baidu_homepage():
    r = requests.get('https://www.baidu.com')
    assert r.status_code == 200, "request successful"


