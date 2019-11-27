# -*- coding: utf-8 -*-
"""
@Author: yqbao
@GiteeURL: https://gitee.com/yqbao
@name:XXX
@Date: 2019/11/26 14:10
@Version: v.0.0
"""
import time
import requests
from encode import encode_token
from datetime import datetime


class MeiTuan:
    def __init__(self):
        self.headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '',
            'Host': 'i.waimai.meituan.com',
            'Origin': 'https://h5.waimai.meituan.com',
            'Pragma': 'no-cache',
            'Referer': '',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36',
        }

    def get_shop_list(self, _token, index, uuid, lat, long):
        ts = int(datetime.now().timestamp() * 1000)
        url = 'https://i.waimai.meituan.com/openh5/homepage/poilist?_={}'.format(ts)
        self.headers['Referer'] = 'https://h5.waimai.meituan.com/waimai/mindex/home'
        self.headers[
            'Cookie'] = 'wm_order_channel=default; utm_source=; _lxsdk_cuid=16e91cd426fc8-08144719b20fd4-277e2849-42470-16e91cd4270c8; terminal=i; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; iuuid=98EEDC66C00A8F57FDFCB92457B5BBE28F1D85DB14905CC7F95CB37CCD737C55; token=gv3ZqdQIPKpZMeXBVStu2tptS9sAAAAAgQkAAEMtH5ymOViHC2MtX9gIrD-frjhji2gpLk64oEfTfm5URB23TsdwOzwDaweVxmZPsA; mt_c_token=gv3ZqdQIPKpZMeXBVStu2tptS9sAAAAAgQkAAEMtH5ymOViHC2MtX9gIrD-frjhji2gpLk64oEfTfm5URB23TsdwOzwDaweVxmZPsA; oops=gv3ZqdQIPKpZMeXBVStu2tptS9sAAAAAgQkAAEMtH5ymOViHC2MtX9gIrD-frjhji2gpLk64oEfTfm5URB23TsdwOzwDaweVxmZPsA; userId=281544318; _lxsdk=98EEDC66C00A8F57FDFCB92457B5BBE28F1D85DB14905CC7F95CB37CCD737C55; w_token=gv3ZqdQIPKpZMeXBVStu2tptS9sAAAAAgQkAAEMtH5ymOViHC2MtX9gIrD-frjhji2gpLk64oEfTfm5URB23TsdwOzwDaweVxmZPsA; openh5_uuid=98EEDC66C00A8F57FDFCB92457B5BBE28F1D85DB14905CC7F95CB37CCD737C55; igateApp=%3C%25%3D%20htmlWebpackPlugin.options.iGateAppKey%20%25%3E; w_uuid=HJctRUBLTg4lT8oSgJjf4kvfK3lGmgDSHxu4FkB9FIl17x_DdYYCZMbgaGJ9dncS; IJSESSIONID=1ef3to3nv2d2q1ea9ty7gjok3s; isid=87C59C97792FB768FECAF90465337621; logintype=normal; u=281544318; latlng=30.68711%2C103.965125%2C1574673649586; ci=59; cityname=%E6%88%90%E9%83%BD; webp=1; i_extend=H__a100038__b1; __utmc=74597006; __utma=74597006.1942812594.1574673653.1574673653.1574673653.1; __utmz=74597006.1574673653.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); au_trace_key_net=default; openh5_uuid=98EEDC66C00A8F57FDFCB92457B5BBE28F1D85DB14905CC7F95CB37CCD737C55; uuid=98EEDC66C00A8F57FDFCB92457B5BBE28F1D85DB14905CC7F95CB37CCD737C55; w_latlng=30678132,104028975; _lx_utm=utm_source%3D; w_visitid=3bb82c91-a812-4057-b663-eab0ddb9b910; cssVersion=e8aa621b; _lxsdk_s=16eac4bc66f-9f4-dd7-9b6%7C%7C19'  # 若不添加cookie将只能查看前5页
        form_data = [{
            'startIndex': x,
            'sortId': 0,
            'multiFilterIds': '',
            'sliderSelectCode': '',
            'sliderSelectMin': '',
            'sliderSelectMax': '',
            'geoType': 2,
            'rankTraceId': '',
            'uuid': uuid,
            'platform': 3,
            'partner': 4,
            'originUrl': self.headers['Referer'],
            'riskLevel': 71,
            'optimusCode': 10,
            'wm_latitude': lat,
            'wm_longitude': long,
            'wm_actual_latitude': '',
            'wm_actual_longitude': '',
            'openh5_uuid': uuid,
            '_token': _token
        } for x in range(index)]
        for data in form_data:
            response = requests.post(url=url, headers=self.headers, data=data)
            with open('data.jl', 'a', encoding='utf-8') as f:
                f.write(response.text + "\n")
            print('a--b--c--d--e--f--g--h--i--j--k--l--m--n')
            time.sleep(10)


if __name__ == '__main__':
    meituan = MeiTuan()
    pag = 100  # 页码
    latitude = ''  # 坐标值
    longitude = ''  # 坐标值
    uid = ""  # uuid
    en_token = encode_token(uid, latitude, longitude)
    meituan.get_shop_list(en_token, pag, uid, latitude, longitude)
