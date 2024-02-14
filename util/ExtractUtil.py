from util.AssertUtil import AssertUtil
from util.YamlUtil import YamlUtil


class ExtractUtil:
    def __init__(self):
        self.jsonpath_util = AssertUtil()
        self.yaml_util = YamlUtil()

    def extract_data(self, response, extract):
        '''
        将接口返回内容例如（token）存入yaml内
        :param response:
        :param extract:
        :return:
        '''
        if extract:
            for key, expression in extract.items():
                value = self.jsonpath_util.extract_by_jsonpath(response, expression)
                # 写入value
                self.yaml_util.write_token_yaml({key: value})
