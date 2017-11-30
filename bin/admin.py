#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
管理员
"""

import os
import sys
import pickle

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from conf import settings
from lib import core


def create_teacher(admin_obj):
    """
    创建老师
    :return:
    """
    teacher_list = []
    # 循环添加老师，输入q退出
    while True:
        teacher_name = input("请输入教师姓名(输入q退出)：")
        if teacher_name == "q":
            break
        teacher_age = input("请输入教师年龄：")

        obj = core.Teacher(teacher_name, teacher_age, admin_obj)
        teacher_list.append(obj)

    # 如果文件已经存在，则把原文件添加到新添加的teacher_list中，并重新写入
    path = os.path.join(settings.TEACHERS_DB_PATH, "teacher_list")
    if os.path.exists(path):
        exists_list = pickle.load(open(path, "rb"))
        teacher_list.extend(exists_list)
    pickle.dump(teacher_list, open(path, "wb"))
    print("添加成功")


def create_course(admin_obj):
    """
    创建课程
    :param admin:
    :return:
    """
    # course_list = []
    # while True:
    #     course_name = input("请输入课程名：")
    path = os.path.join(settings.TEACHERS_DB_PATH, "teacher_list")
    teacher_list = pickle.load(open(path, "rb"))
    for index, item in enumerate(teacher_list, 1):
        print(index, item.name, item.age, item.create_admin.username, item.create_time)

    course_list = []
    while True:
        teacher_index = input("请选择课程任课教师序号(输入q退出)：")
        if teacher_index == "q":
            break
        course_name = input("请输入课程名称：")
        course_cost = input("请输入课时费用：")
        obj = core.Course(course_name, course_cost, teacher_list[int(teacher_index)-1], admin_obj)
        course_list.append(obj)

    # 如果文件已经存在，则把原文件添加到新添加的teacher_list中，并重新写入
    path = os.path.join(settings.COURSES_DB_PATH, "course_list")
    if os.path.exists(path):
        exists_list = pickle.load(open(path, "rb"))
        course_list.extend(exists_list)
    pickle.dump(course_list, open(path, "wb"))
    print("添加成功")



def login(user, pwd):
    """
    管理员登录
    :param user:
    :param pwd:
    :return:
    """
    path = os.path.join(settings.ADMIN_DB_PATH, user)
    result = os.path.exists(path)
    if result:
        admin_obj = pickle.load(open(path, "rb"))
        if admin_obj.login(user, pwd):
            print("登录成功")
            while True:
                select = input("1.创建教师；2.添加课程；q.退出\n>>>")
                if select == "1":
                    create_teacher(admin_obj)
                elif select == "2":
                    create_course(admin_obj)
                else:
                    break
        else:
            # 密码错误
            return 0
    else:
        # 用户不存在
        return 1


def register(user, pwd):
    """
    管理员注册
    :param user: 用户名
    :param pwd: 密码
    :return:
    """

    admin_obj = core.Admin()
    if admin_obj.register(user, pwd):
        print("注册成功")
    else:
        print("注册失败")


def main():
    """
    主函数
    :return: None
    """
    inp = input("1.管理员登录；2.管理员注册：\n>>>")
    user = input("请输入账户：")
    pwd = input("请输入密码：")

    if inp == "1":
        result = login(user, pwd)
        if result == 0:
            print("登录失败：密码错误！")
        elif result == 1:
            print("登录失败：该用户不存在！")

    elif inp == "2":
        register(user, pwd)
    else:
        print("输入有误！")


if __name__ == '__main__':
    main()
