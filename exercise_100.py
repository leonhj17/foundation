# _*_ encoding:utf-8 _*_

"""
    1.将元组(1,2,3)和集合{4,5,6}合并成一个列表
    2.在列表[1,2,3,4,5,6]首尾分别添加整型元素7和0
    3.反转列表[0,1,2,3,4,5,6,7]
    4.反转列表[0,1,2,3,4,5,6,7]后给出中元素5的索引号
    5.分别统计列表[True, False, 0, ,1, 2]中True，False，0,1,2的元素个数，发现了什么？
    6.从列表[True,1,0,'x',None,'x',Falue,2,True]中删除元素'x'
    7.从列表[True,1,0,'x',None,'x',Falue,2,True]中删除索引号为4的元素
    8.删除列表中索引号为奇数（或偶数）的元素
    9.清空列表中的所有元素
    10.对列表[3,0,8,5,7]分别做升序和降序排列
"""


def exe1():
    tp = (1, 2, 3)
    st = {4, 5, 6}
    tp = list(tp)
    st = list(st)
    tp.extend(st)
    # new_list = tp + st
    return tp


def exe2():
    l = [1, 2, 3, 4, 5, 6]
    l.insert(0, 7)
    l.append(0)
    return l


def exe3():
    l = [0, 1, 2, 3, 4, 5, 6, 7]
    # l.reverse()
    l.sort(reverse=True)
    return l


def exe4():
    l = [0, 1, 2, 3, 4, 5, 6, 7]
    l.reverse()
    return l.index(5)


def exe5():
    l = [True, False, 0, 1, 2]
    n_true = l.count(True)
    n_false = l.count(False)
    n_0 = l.count(0)
    n_1 = l.count(1)
    n_2 = l.count(2)
    return n_true, n_false, n_0, n_1, n_2


def exe6():
    l = [True, 1, 0, 'x', None, 'x', False, 2, True]
    while 'x' in l:
        l.remove('x')
    return l


def exe7():
    l = [True, 1, 0, 'x', None, 'x', False, 2, True]
    del l[4]
    return l


def exe8():
    l = [True, 1, 0, 'x', None, 'x', False, 2, True]
    del l[1::2]
    # del l[::2]
    return l


def exe9():
    l = [True, 1, 0, 'x', None, 'x', False, 2, True]
    del l[:]
    return l


def exe10():
    l = [3, 0, 8, 5, 7]
    l.sort(reverse=False)
    return l


if __name__ == "__main__":
    print(exe10())
