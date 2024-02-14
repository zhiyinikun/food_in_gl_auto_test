import os

import yaml


class YamlUtil:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data/")


    # 传入yaml的文件名
    def read_yaml_data(self, yaml_name, key_name=None):
        with open(self.data_path + yaml_name, mode='r', encoding='utf8') as f:
            value = yaml.safe_load(f)
            if key_name:
                return value[key_name]
            return value

    def extract_case(self, yaml_name, key_name):
        """获取yaml文件，遍历case_info的内容，做到重复测试多个数据"""
        case_value = self.read_yaml_data(yaml_name, key_name)[0]
        new_case = []
        for value in case_value['case_info']:
            new_case.append({"request_info": case_value['request_info'], "case_info": value})
        return new_case

    # def write_extra_yaml(self, data):
    #     """写入数据到yaml中，data为字典"""
    #     with open(self.data_path + "token.yaml", mode='a', encoding='utf8') as f:
    #         # 读取之前的yaml内容
    #         old_value = self.read_extract_yaml()
    #         if old_value:
    #             # 如果有老数据则清空数据
    #             self.clear_extract_yaml()
    #         yaml.dump(data=data, stream=f, allow_unicode=True)

    # def clear_extract_yaml(self):
    #     """清理extract.yaml"""
    #     with open(self.data_path + "extract.yaml", mode='w', encoding='utf8') as f:
    #         f.truncate()
    #
    # def read_extract_yaml(self):
    #     """只读取data下面的extract.yaml"""
    #     with open(self.data_path + "extract.yaml", mode='r', encoding='utf8') as f:
    #         value = yaml.safe_load(f)
    #         return value
    #


    def write_token_yaml(self, data):
        """写入数据到yaml中，data为字典"""
        with open(self.data_path + "token.yaml", mode='a', encoding='utf8') as f:
            # 读取token.yaml内容
            old_value = self.read_token_yaml()
            if old_value:
                # 如果有老数据则清空数据
                self.clear_token_yaml()
            yaml.dump(data=data, stream=f, allow_unicode=True)
    def read_token_yaml(self):
        """只读取data下面的token.yaml"""
        with open(self.data_path + "token.yaml", mode='r', encoding='utf8') as f:
            value = yaml.safe_load(f)
            return value

    def clear_token_yaml(self):
     """清理extract.yaml"""
     with open(self.data_path + "token.yaml", mode='w', encoding='utf8') as f:
         f.truncate()

