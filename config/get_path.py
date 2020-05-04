# -*- coding: utf-8 -*-
# @Author: ChenYuan
# @Date  : 2020/4/30 11:06
import os


folder_path = os.path.realpath(__file__)
# print(folder_path)

path = os.path.split(os.path.split(folder_path)[0])[0]
# print(path)

# excel路径
excel_path = os.path.join(path, 'data', '接口测试用例.xlsx')
# print(excel_path)

# html 路径
html_path = os.path.join(path,'result','html')
# print(html_path)

# log 路径
log_path = os.path.join(path,'result','log')

# mail 配置路径
mail_path = os.path.join(path,'config','mail.ini')