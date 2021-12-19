import os

from techprog3 import reading, minimum, summarize, large, prod
import time


def test_reading():
    assert reading('test1/1.txt') == "InvalidFile"
    assert reading('test1/2.txt') == [56, 554615, 65165, 1651, 5, 165, 1, 66, 51, 523.51515151, 26251.5415151515151, 526162, 51, 4444.26151]
    assert reading('test1/3.txt') == [51, 561, 5, 1, 1, 51561, 51, 51, 561, 561, 5, 15, 1, 5454]
    assert reading('test1/4.txt') == "InvalidFile"


def test_minimum():
    assert minimum(reading('test2/1.txt')) == "InvalidFile"
    assert minimum(reading('test2/2.txt')) == min([56, 554615, 65165, 1651, 5, 165, 1, 66, 51, 523.51515151, 26251.5415151515151,
                                      526162, 51, 4444.26151])
    assert minimum(reading('test2/3.txt')) == min([51, 561, 5, 1, 1, 51561, 51, 51, 561, 561, 5, 15, 1, 5454])
    assert minimum(reading('test2/4.txt')) == "InvalidFile"


def test_large():
    assert large(reading('test3/1.txt')) == "InvalidFile"
    assert large(reading('test3/2.txt')) == max(
        [56, 554615, 65165, 1651, 5, 165, 1, 66, 51, 523.51515151, 26251.5415151515151,
         526162, 51, 4444.26151])
    assert large(reading('test3/3.txt')) == max([51, 561, 5, 1, 1, 51561, 51, 51, 561, 561, 5, 15, 1, 5454])
    assert large(reading('test3/4.txt')) == "InvalidFile"


def test_summarize():
    assert summarize(reading('test4/1.txt')) == "InvalidFile"
    assert summarize(reading('test4/2.txt')) == sum(
        [56, 554615, 65165, 1651, 5, 165, 1, 66, 51, 523.51515151, 26251.5415151515151,
         526162, 51, 4444.26151])
    assert summarize(reading('test4/3.txt')) == sum([51, 561, 5, 1, 1, 51561, 51, 51, 561, 561, 5, 15, 1, 5454])
    assert summarize(reading('test4/4.txt')) == "InvalidFile"


def test_prod():
    assert prod(reading('test5/1.txt')) == "InvalidFile"
    assert prod(reading('test5/2.txt')) == 56 * 554615 * 65165 * 1651 * 5 * 165 * 1 * 66 * 51 * 523.51515151 * 26251.5415151515151 * 526162 * 51 * 4444.26151
    assert prod(reading('test5/3.txt')) == 51 * 561 * 5 * 1 * 1 * 51561 * 51 * 51 * 561 * 561 * 5 * 15 * 1 * 5454
    assert prod(reading('test5/4.txt')) == "InvalidFile"


def test_speed():
    tests = ['test6/1.txt', 'test6/2.txt', 'test6/3.txt', 'test6/4.txt']
    print('\n')
    print('Поиск минимума\n')
    for test in tests:
        t0 = time.time()
        minimum(reading(test))
        print(os.path.getsize(test), time.time() - t0)
    print('\n')
    print('Поиск максимума\n')
    for test in tests:
        t0 = time.time()
        large(reading(test))
        print(os.path.getsize(test), time.time() - t0)
    print('\n')
    print('Вычисление суммы\n')
    for test in tests:
        t0 = time.time()
        summarize(reading(test))
        print(os.path.getsize(test), time.time() - t0)
    print('\n')
    print('Вычисление произведения\n')
    for test in tests:
        t0 = time.time()
        prod(reading(test))
        print(os.path.getsize(test), time.time() - t0)
