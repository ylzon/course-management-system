#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
全局配置文件
"""
import os
import sys

# 根目录路径
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

# 工具库路径
LIB_PATH = os.path.join(BASE_PATH, "lib")

# 配置路径
CONF_PATH = os.path.join(BASE_PATH, "conf")

# 数据存储路径
DB_PATH = os.path.join(BASE_PATH, "db")
ADMIN_DB_PATH = os.path.join(DB_PATH, "admin")
STUDENTS_DB_PATH = os.path.join(DB_PATH, "students")


# 日志路径
LOG_PATH = os.path.join(BASE_PATH, "log")


