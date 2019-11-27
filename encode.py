# -*- coding: utf-8 -*-
"""
@Author: yqbao
@GiteeURL: https://gitee.com/yqbao
@name:XXX
@Date: 2019/11/26 13:30
@Version: v.0.0
"""
import base64
import json
import zlib
from datetime import datetime


def decode_token(token):
    """
    解码token
    :param token:
    :return:
    """
    token_decode = base64.b64decode(token.encode())  # base64解码
    token_string = zlib.decompress(token_decode)  # 二进制解压
    return token_string


def encode_sign(uuid, lat, long):
    """生成sign"""
    data = {
        "geoType": "2",
        "multiFilterIds": "",
        "openh5_uuid": uuid,
        "optimusCode": "10",
        "originUrl": "https://h5.waimai.meituan.com/waimai/mindex/home"
                     "&partner=4&platform=3&rankTraceId=&riskLevel=71&sliderSelectCode="
                     "&sliderSelectMax=&sliderSelectMin=&sortId=0&startIndex=0&uuid={}"
                     "&wm_actual_latitude=0&wm_actual_longitude=0"
                     "&wm_latitude={}&wm_longitude={}".format(uuid, lat, long)
    }
    clean_data = {
        key: value
        for key, value in data.items()
        if key not in ["uuid", "platform", "partner"]
    }
    sign_data = []
    for key in sorted(clean_data.keys()):
        sign_data.append(key + "=" + str(clean_data[key]))
    sign_data = "&".join(sign_data)
    return compress_data(sign_data)


def compress_data(data):
    """编码函数"""
    json_data = json.dumps(data, separators=(',', ':')).encode("utf-8")
    compressed_data = zlib.compress(json_data)
    base64_str = base64.b64encode(compressed_data).decode()
    return base64_str


def encode_token(uuid, lat, long):
    """
    生成token
    :param uuid: UUID
    :param lat: 坐标值
    :param long: 坐标值
    :return:
    """
    ts = int(datetime.now().timestamp() * 1000)
    token_dict = {
        'rId': 101701,
        'ver': '1.0.6',
        'ts': ts,
        'cts': ts + 100 * 1000,
        'brVD': [376, 722],
        'brR': [[376, 722], [376, 722], 24, 24],
        'bI': ['https://h5.waimai.meituan.com/waimai/mindex/home', ''],
        'mT': [],
        'kT': [],
        'aT': [],
        'tT': [],
        'aM': '',
        'sign': encode_sign(uuid, lat, long)
    }
    encode = str(token_dict).encode()  # 二进制编码
    compress = zlib.compress(encode)  # 二进制压缩
    b_encode = base64.b64encode(compress)  # base64编码
    token = str(b_encode, encoding='utf-8')  # 转为字符串
    return token


if __name__ == '__main__':
    de_token = [  # 分析使用（此处放加密的token）
        "",
    ]
    for i in de_token:
        token1 = decode_token(i)
        print(token1)
