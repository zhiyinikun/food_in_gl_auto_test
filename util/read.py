import configparser
import os
import yaml


class FileRead:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data",
                                      "admin_data.yaml")
        self.ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config",
                                     "settings.ini")

    def read_data(self):
        f = open(self.data_path, encoding="utf8")
        data = yaml.safe_load(f)
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf8')
        return config


base_data = FileRead()
print(base_data.read_ini())
