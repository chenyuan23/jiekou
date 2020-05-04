# -*- coding: utf-8 -*-
# @Author: ChenYuan
# @Date  : 2020/4/30 12:51
from case.loginCase import TestLogin
import datetime,HTMLTestRunner_CY
from config.get_path import *
import unittest,logging
from common.mail_data import GetMail


class Run(unittest.TestCase):
    def test_run(self):
        # suite = unittest.TestSuite()
        # suite.addTest(unittest.makeSuite(TestLogin))
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        hp = html_path + '/' + now + r'test.html'
        with open(hp, 'wb') as f:
            runner = HTMLTestRunner_CY.HTMLTestRunner(stream=f, verbosity=1, title=None, description=None)
            # runner.run(suite)

        logging.basicConfig(filename=log_path + '/' + now + r'result.log',
                            filemode='w',
                            format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',  #时间、代码所在文件名、代码行号、日志级别名字、日志信息
                            datefmt='%Y-%m-%d_%H_%M_%S',
                            level=logging.DEBUG
                            )

        logger = logging.getLogger('test')  # 创建日志收集器
        logger.info(self)

        #  发送邮件
        GetMail.mail_data(self)

if __name__ == '__main__':
    unittest.main()