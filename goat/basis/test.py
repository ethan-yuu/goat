#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import partial

def fa(a,b,c): #定义一个相加的函数
    print("%s",a)
    print("%d",b)
    print("%s",c)
    return a+b+c

p=partial(fa,4,4)  #定义分部函数，其中第3个参数已固定

print(p(10))  # 初始化前两个参数
