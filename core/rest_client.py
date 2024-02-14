import json

import requests

from util.log_util import logger
from util.read import base_data

api_url = base_data.read_ini()['host']['api_url']


class RestClient:
    def __init__(self):
        self.api_url = api_url
        self.session = requests.Session()

    def do_request(self, url, method, **kwargs):
        # 获取返回结果
        response = self.request(url, method, **kwargs).json()
        logger.info("接口返回内容>>>\n{}".format(json.dumps(response, ensure_ascii=False, indent=2)))
        return response

    def request(self, url, method, **kwargs):
        self.request_log(url, method, **kwargs)
        if method == "GET":
            return self.session.get(self.api_url + url, **kwargs)
        if method == "POST":
            return self.session.post(self.api_url + url, **kwargs)
        if method == "PUT":
            return self.session.put(self.api_url + url, **kwargs)
        if method == "DELETE":
            return self.session.delete(self.api_url + url, **kwargs)

    def request_log(self, url, method, **kwargs):
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")

        logger.info("接口请求的地址>>>{}".format(self.api_url + url))
        logger.info("接口请求的方法>>>{}".format(method))
        if data is not None:
            logger.info("接口请求的data参数>>>\n{}".format(json.dumps(data, ensure_ascii=False, indent=2)))
        if json_data is not None:
            logger.info("接口请求的json参数>>>\n{}".format(json.dumps(json_data, ensure_ascii=False, indent=2)))
        if params is not None:
            logger.info("接口请求的params参数>>>\n{}".format(json.dumps(params, ensure_ascii=False, indent=2)))
        if headers is not None:
            logger.info("接口请求的headers参数>>>\n{}".format(json.dumps(headers, ensure_ascii=False, indent=2)))

