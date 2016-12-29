#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


"""
扫描文件夹内所有文件，并转换编码

:param srcDir: 源文件文件夹路径
:param dstDir: 输出文件文件夹路径
:param in_encoding: 输入文件编码格式
:param out_encoding: 输出文件编码格式

"""

if __name__ == '__main__':

    srcDir = input("请输入源文件目录（例如：c:/src）：")

    if not os.path.exists(srcDir):
        print("源文件路径不存在！")
        exit()

    dstDir = input("请输入输出目录（例如：c:/dst）：")

    if not os.path.exists(dstDir):
        os.makedirs(dstDir)

    in_encoding = input("请输入源文件编码（例如：gbk）：")

    out_encoding = input("请输入输出文件编码（例如：utf8）：")

    try:

        for root, dirs, files in os.walk(srcDir):

            subDir = root.split(srcDir)[1]

            for file in files:

                with open(os.path.join(root, file), encoding=in_encoding) as i:

                    targetFileDir = dstDir

                    if subDir:
                        targetFileDir = dstDir + subDir

                    if not os.path.exists(targetFileDir):
                        os.makedirs(targetFileDir)

                    with open(os.path.join(targetFileDir, file), "w", encoding=out_encoding) as o:
                        o.write(i.read())
                        print("文件 " + file+" 编码转换成功")

        print("编码转换完成")
    except Exception as e:
        print(e)
