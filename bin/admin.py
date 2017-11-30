#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
管理员
"""

import os
import sys
import pickle

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from conf import setting
from lib import moduls


def login(user, pwd):
    """
    管理员登录
    :param user:
    :param pwd:
    :return:
    """
    path = os.path.join(setting.ADMIN_DB_PATH, user)
    result = os.path.exists(path)
    if result:
        admin_obj = pickle.load(open(path, "rb"))
        result = admin_obj.login(user, pwd)
        if result:
            print("登录成功")
        else:
            print("用户名或密码错误！")
    else:
        print("登录失败：该用户不存在！")


def register(user, pwd):
    """
    管理员注册
    :param user: 用户名
    :param pwd: 密码
    :return:
    """

    admin_obj = moduls.Admin()
    result = admin_obj.register(user, pwd)
    if result:
        print("注册成功")
    else:
        print("注册失败")


def main():
    """
    主函数
    :return: None
    """
    inp = input("1、用户登录；2、用户注册：\n >>>")
    user = input("请输入账户：")
    pwd = input("请输入密码：")

    if inp == "1":
        login(user, pwd)
    elif inp == "2":
        register(user, pwd)


if __name__ == '__main__':
    main()
