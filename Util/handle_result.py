# coding=utf-8

import json
import os
import sys

from deepdiff import DeepDiff

base_path = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_path)
sys.path.append(parent_dir)
from Util.handle_json import get_value


file_name = "/config/code_message.json"

def handle_result(url, code):
    """
    获取message中的返回
    :param url: url
    :param code: message code
    :return: str
    """
    # 获取预期接口的响应信息
    code_value = get_value(url, file_name)
    # 对响应信息进行是否为空判断
    if code_value is not None:
        # 获取接口的 message信息
        for i in code_value:
            message = i.get(str(code))
            if message:
                return message
    return None


def handle_result_json(dict1, url):
    """
    接口返回结果和预期结果进行比较
    :param dict1: execel 中的预期结果
    :param url: 接口响应返回接口
    :return: bool
    """
    # 调用get_value 获取接口返回的data数据
    dict2 = get_value(url)
    # 将excel 用例中获取的预期结果转换成字典格式
    if type(dict1) == str:
        dict1 = json.loads(dict1)
    # 使用DeepDiff 方法对比接口返回数据和execel用例中预期的返回数据
    cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()

    # dictionary_item_added、dictionary_item_removed为 DeepDiff 方法中的判断
    # 包含以上两个字段则表示data数据较预期有所改动
    if cmp_dict.get('dictionary_item_added'):
        return False
    elif cmp_dict.get('dictionary_item_removed'):
        return False
    else:
        return True
