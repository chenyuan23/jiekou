# -*- coding: utf-8 -*-
# @Author: ChenYuan
# @Date  : 2020/4/30 11:30
from common.getExcelData import GetExcelData
from common.Httpsrequests import GetHttpRequests
from config.get_path import *
import unittest,datetime,logging
from ddt import ddt,data
import HTMLTestRunner_CY
import logging
logging.basicConfig(
    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',  #时间、代码所在文件名、代码行号、日志级别名字、日志信息
    datefmt='%Y-%m-%d_%H_%M_%S',
    level=logging.DEBUG
)

@ddt
class TestLogin(unittest.TestCase):
    ex_data = GetExcelData.getData(excel_path, 'login')  # 获取所有的测试用例

    @data(*ex_data)
    def test_api(self,item):
        global id
        id = item['case_id']
        print(item['method'])
        respon = GetHttpRequests.getRequests(self,item['url'], item['method'], eval(item['data']),headers=eval(item['headers']))
        print(respon.status_code)
        try:
            self.assertEqual(200,respon.status_code)
        except AssertionError as e:
            print('断言错误')
            raise e

    def tearDown(self):
        print('第{}条测试用例执行结束'.format(id))


if __name__ == '__main__':
    unittest.main()