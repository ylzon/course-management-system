#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
学生
"""

import os
import sys
import pickle

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from conf import settings
from lib import core


def course_info(student_obj):
    """
    查看已选课信息
    :param student_obj:
    :return:
    """
    for item in student_obj.course_list:
        print(item.course_name, item.cost, item.teacher.name)


def course_select(student_obj):
    """
    选课
    :param admin:
    :return:
    """

    path = os.path.join(settings.COURSES_DB_PATH, "course_list")
    course_list = pickle.load(open(path, "rb"))
    for index, item in enumerate(course_list, 1):
        print(index, item.course_name, item.cost, item.teacher.name, item.create_time)

    while True:
        course_index = input("请选择课程序号(输入q退出)：")
        if course_index == "q":
            break

        obj = course_list[int(course_index) - 1]
        if student_obj.course_list != []:
            for item in student_obj.course_list:
                if item.course_name == obj.course_name:
                    print("添加失败：已选课程不能重复选择！")
                    break
            else:
                student_obj.course_list.append(obj)
                print("添加成功")
        else:
            student_obj.course_list.append(obj)
            print("添加成功")

    # 如果文件已经存在，则重新写入
    path = os.path.join(settings.STUDENTS_DB_PATH, student_obj.username)
    pickle.dump(student_obj, open(path, "wb"))
    print("选课成功")


def login(user, pwd):
    """
    学生登录
    :param user:
    :param pwd:
    :return:
    """
    path = os.path.join(settings.STUDENTS_DB_PATH, user)
    result = os.path.exists(path)
    if result:
        student_obj = pickle.load(open(path, "rb"))
        if student_obj.login(user, pwd):
            print("登录成功")
            while True:
                select = input("1.选课；2.上课；3.查看已选课程；q.退出\n>>>")
                if select == "1":
                    course_select(student_obj)
                elif select == "2":
                    pass
                elif select == "3":
                    course_info(student_obj)
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

    student_obj = core.Student()
    if student_obj.register(user, pwd):
        print("注册成功")
    else:
        print("注册失败")


def main():
    """
    主函数
    :return: None
    """
    inp = input("1.学生登录；2.学生注册：\n>>>")
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
