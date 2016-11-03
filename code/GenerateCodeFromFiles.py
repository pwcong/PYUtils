#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
扫描文件夹内所有文件，生成代码。

:param filesDir: 文件夹路径
:param codePath: 代码文件路径

"""

import os

if __name__ == '__main__':

    filesDir = r"C:\filesDir"
    codePath = r"C:\code.txt"

    for root, dirs, files in os.walk(filesDir):

        with open(codePath, "a", encoding="utf-8") as o:

            for file in files:
                # 这里修改输出代码格式
                o.write('list.add("%s");\n' % file.split('.')[0])