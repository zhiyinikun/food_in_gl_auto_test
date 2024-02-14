import allure

from util.AssertUtil import AssertUtil

from core.rest_client import RestClient
from util.ExtractUtil import ExtractUtil


class AdminApiService:
    def __init__(self):
        self.restClient = RestClient()
        self.assertUtil = AssertUtil()
        self.extract = ExtractUtil()

    def handle_case(self, data, login_token=None):
        # 获取title
        allure_title = data["request_info"]["case_title"]
        # 给allure动态的定义用例标题
        allure.dynamic.title(allure_title)
        # 获取url
        url = data["request_info"]["url"]
        # 获取method
        method = data["request_info"]["method"]
        # 获取headers
        headers = data["request_info"]["headers"]
        if login_token:
            #  headers.update(login_token)：加入login_toke返回的字典
            headers.update(login_token)
        # 获取case_info
        case_info = data["case_info"]
        # 获取validate 去除了validate就只剩下json
        validate = case_info.pop("validate", None)
        # 获取extract,取得token或其他返回的的参数
        extract = case_info.pop("extract", None)
        # 返回值
        response = self.restClient.do_request(url=url, method=method, headers=headers, **case_info)
        # 将token写入yaml
        self.extract.extract_data(response, extract)
        # 逻辑断言
        self.assertUtil.validate_response(response,validate)
        return response
