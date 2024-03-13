# coding=utf-8
import os
import sys

import requests

base_path = os.getcwd()
sys.path.append(base_path)
from Util.handle_init import hand_ini
from Util.handle_json import get_value
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')


class BaseRequest:
    def send_post(self, url, data=None):
        """
        post请求封装
        """
        res = requests.post(url=url, data=data)
        return res

    def send_get(self, url, data=None):
        """
        get请求封装
        """
        res = requests.get(url=url, params=data)
        return res

    def run_main(self, method, url, data=None):
        # mock 数据
        return get_value(url)

        # 接收请求，判断method，调用对应的get或post方法
        method = method.upper()
        if 'http' not in url:
            url = hand_ini.get_ini_value('host') + url
        logging.info(url)
        if method == "GET":
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        try:
            return res.json()
        except:
            return res.text


# if __name__ == '__main__':
case_requests = BaseRequest()
