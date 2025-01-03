#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
        return ax


def lazy_sum(*args):
    def inner_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return inner_sum()


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s:' % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator

@log('execute')
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

# @log('execute')
# def count():
#     print("1")