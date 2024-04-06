import requests
import pytest

from core.AdminApiService import AdminApiService
from util.YamlUtil import YamlUtil
from util.read import base_data


# def get_data():
#     return base_data.read_data()


# 旧获取token方法
# @pytest.fixture(scope="function")
# def login_token():
#     header = {
#         "Content-Type": "application/json"
#     }
#     data = {
#         "username": "fyx",
#         "password": "123456"
#     }
#     login_info = requests.post(url='http://localhost:8080/admin/employee/login', json=data, headers=header).json()
#     token_value = login_info['data']['token']
#     headers = {"token": token_value}
#     return headers

# 从token的yaml里获取token的方法
@pytest.fixture(scope="function")
def fetch_token():
    # 从获取yaml里token
    token = YamlUtil().read_token_yaml()
    return token
