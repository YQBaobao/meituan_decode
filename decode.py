# -*- coding: utf-8 -*-
"""
@Author: yqbao
@GiteeURL: https://gitee.com/yqbao
@GitHub: https://github.com/YQBaobao
@name:XXX
@Date: 2019/11/26 15:41
@Version: v.0.0
"""
import re
import requests
import json
from fontTools.ttLib import TTFont


def get_font():
    """下载字体文件"""
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36',
    }
    home_url = 'https://h5.waimai.meituan.com/waimai/mindex/home'
    req = requests.get(url=home_url, headers=headers)
    font_url = "http:" + re.findall('@font-face.*?url.*?"(.*?)eot', req.text)[0] + "woff"
    print(font_url)
    name = re.findall('.*/(.*)', font_url)[0]
    with open('../fonts/' + name, 'wb') as f:
        f.write(requests.get(url=font_url).content)


def test_font():
    """
    分析字体文件,得出对应字形关系
    :return:
    """
    base_font = TTFont('fonts.woff')  # fonts.woff 为不变的部分
    base_fonts = {
        'uniF480': '6', 'uniE1F5': '9', 'uniEF27': '7', 'uniEF5B': '1', 'uniF2CF': '3',
        'uniEDF5': '0', 'uniF0CF': '8', 'uniE134': '2', 'uniF82C': '5', 'uniF72B': '4'}  # 基本的映射表
    number_encode = {}

    # 如发现解码结果为空字符串，请手动切换此处的字体文件，也可以自己修改，变成自动切换
    online_fonts = TTFont('./fonts/e8aa621b.woff')  # 下载的动态字体文件
    uni_list = online_fonts.getGlyphNames()[1:-1]  # 取中间部分的数字
    for uni in uni_list:  # 解析字体库
        online_glyph = online_fonts['glyf'][uni]  # 返回的是unicode对应信息的对象
        for fonts in base_fonts:
            base_glyph = base_font['glyf'][fonts]
            if online_glyph == base_glyph:
                number_encode[uni[3:].lower()] = base_fonts[fonts]
    return number_encode


def get_test():
    with open('data.jl', 'r', encoding='utf-8') as f:
        for lin in f.readlines():
            data = json.loads(lin)
            yield data


def get_data(number_encode):
    """
    解析数据，并调用解码
    :return: 解析结果
    """
    count = 1
    for lin in get_test():
        response = lin.get('data').get('shopList')
        shop_data_list = [{
            "month_sales": font_decode(number_encode, data.get('monthSalesTip')),
            "delivery_time": font_decode(number_encode, data.get('deliveryTimeTip')),
        } for data in response]
        count += len(shop_data_list)
        yield shop_data_list
    print("总个数：", count)


def font_decode(nu_encode, font):
    """
    解码
    :param nu_encode:
    :param font:加密数据
    :return: 解码数据
    """
    m = re.findall(r'&#x(.*?);', font)
    n = [str(j) for x in m for j, y in enumerate(nu_encode) if y == x]
    return "".join(n)


if __name__ == '__main__':
    n_encode = test_font()  # 解码数字关系
    for o in get_data(n_encode):  # 解码加密数据
        print(o)
