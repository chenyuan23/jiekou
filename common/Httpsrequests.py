# -*- coding: utf-8 -*-
# @Author: ChenYuan
# @Date  : 2020/4/30 11:26
import requests


class GetHttpRequests():
    def getRequests(self, url, method, data, headers):
        if method == 'get':
            res = requests.get(url,data,headers=headers)
            return res
        else:
            if method == 'post':
                res = requests.post(url,data,headers=headers)
        return res