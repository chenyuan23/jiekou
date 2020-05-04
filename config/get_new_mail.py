# -*- coding: utf-8 -*-
# @Author: ChenYuan
# @Date  : 2020/4/30 14:38
from config.get_path import *
import os

lists = os.path.join(html_path) # 获取文件夹的名称
new= os.listdir(lists) # os.listdir 返回指定目录下的文件夹和文件列表
new_html = os.path.join(html_path,new[-1])
print(new_html)

f = open(new_html,'rb')
mail_body=f.read()
f.close()

