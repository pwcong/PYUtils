#!/usr/lib/env python3
# -*- coding: utf-8 -*-

"""
扫描文件夹内所有文件，并重新命名

:param filesDir: 文件夹路径

"""

import os

if __name__ == '__main__':

    filesDir = r"C:\pixiv"

    for root, dirs, files in os.walk(filesDir):

        for file in files:
            # 这里修改文件命名逻辑
            os.rename(os.path.join(root, file), os.path.join(root, file.split(".")[0] + ".jpg"))


