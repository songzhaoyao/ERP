#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/10/21 13:54 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
第四次作业：
2. 完成任意整数序列的相加 -- range()- 生成一个整数序列，里面全是数字。求里面所有数字的和
3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。-
'''
# def  add_fun(num):
#     sum = 0
#     # num = int(input("input正数："))   # 字符串
#     for i in range(num):
#         sum += i
#     print(sum)
# add_fun(100)
# def function_len(object):
#     # if type(object)==dict or type(object)==list or type(object)== str:
#     if isinstance(object,str) or isinstance(object,list) or isinstance(object,dict):  # True--False
#         leng = len(object)
#         if leng >= 5:
#             print("True")
#         else:
#             print("False")
#     else:
#         print("数据类型不能计算长度！")   # 容错性友好
# function_len((1,2,3,4))   # 函数的调用--- 传入参数
import time
def login_page(username,password,driver):   # 形参   -参数化  --提高代码复用率
    driver.find_element_by_id("username").send_keys(username)  # 找到了有username这个id的元素--点击,输入内容
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
def open_url(url,driver):   # 打开网页
    driver.get(url)
    driver.maximize_window()

def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_page(username,password,driver)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    P_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    F_id = P_id+"-frame"
    driver.switch_to.frame(1)
    driver.find_element_by_id("searchNumber").send_keys(s_key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(1)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num   # 返回值

