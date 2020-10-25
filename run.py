#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/10/23 21:23 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
from python_class import lesson_06   # 导入函数文件
from test_data import test_date  # 导入测试数据 文件
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 调用函数  --1、 先参数取出来  2、 传参到函数调用里
url = test_date.url["url"]  # 取值 url
user = test_date.login_date["username"] # 取值登录用户名
pwd = test_date.login_date["password"] # 取值 登录的密码
s_key = test_date.s_key["s_key"] # 取值 搜索的 关键字
print(url,user,pwd,s_key)
# 函数的调用 传参
# 给函数定义了一个返回值-- 调用的时候用一个变量接受返回值：
result = lesson_06.search_key(driver=driver,url=url,username=user,password=pwd,s_key=s_key)
if s_key in result:
    print("搜索结果是正确的！")
else:
    print("用例测试不通过！")
