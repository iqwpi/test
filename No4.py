# -*- coding:utf-8 -*-
import os
import time

def file_count(filePath):
    counts=open(filePath,encoding='utf8').read()
    count_a=count_z=count_o=count_s=0
    for i in counts:
        if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):#英文字母
            count_a=count_a+1
        elif ord(i)>=48 and ord(i)<=57:#数字
            count_z=count_z+1
        elif ord(i)==32:#空格
            count_s=count_s+1
        else:#其他字符
            count_o=count_o+1
    print("字符总个数: %d个"%len(counts))
    print("英文字母个数：%d个"%count_a)
    print ("数字个数：%d个"%count_z )
    print ("其他字符个数：%d个"%count_o )
    print ("空格个数：%d个"%count_s)


def TimeStampToTime(timestamp):#时间戳转时间
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def get_FileSize(filePath):#获取文件大小
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024*1024)
    return round(fsize,2)

def get_FileCreateTime(filePath):#获取文件创建时间
    ct = os.path.getctime(filePath)
    return TimeStampToTime(ct)