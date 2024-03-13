#coding=utf-8
import configparser
import os
import sys


class HandleInit:
    def __init__(self):
        """
        目录信息获取
        """
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.parent_dir = os.path.dirname(self.base_path)
        sys.path.append(self.parent_dir)

    def load_ini(self):
        """
        打开ini配置文件，获取配置文件内容
        :return:
        """
        ini_paht = self.parent_dir + '/config/server.ini'
        conf = configparser.ConfigParser()
        conf.read(ini_paht, encoding='utf-8')
        return conf

    def get_ini_value(self, key, node='server'):
        """
        通过node，key参数，获取ini文件的内容
        :param key: ini 文件对应的内容的名称
        :param node: ini 文件对应的内容的模块
        :return: str
        """
        conf = self.load_ini()
        try:
            ini_value = conf.get(node, key)
        except Exception:
            ini_value = None
        return ini_value

hand_ini = HandleInit()