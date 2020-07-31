## 函数式编程



# >>> ccc
# [(1, 4), (2, 5), (3, 6)]
# >>> cc_=lambda *a:a  ## lambda  也能用 *，** 来接收 不定长参数。
# >>> cc_(*ccc)        ##  这里是 拆解。
# ((1, 4), (2, 5), (3, 6))


'''
bigmuls = lambda xs,ys: filter(lambda (x,y):x*y > 25, combine(xs,ys))    ## (x,y) 在 lambda 中是一个 整体
combine = lambda xs,ys: map(None, xs*len(ys), dupelms(ys,len(xs)))       ##  None 在 map 中 就会 组合两者。构成set.  其实 None 就是什么都没做
dupelms = lambda lst,n: reduce(lambda s,t:s+t, map(lambda l,n=n: [l]*n, lst))  ## 可以在 lmabda 中传 参数， 也能传函数。 

print bigmuls([1,2,3,4],[10,15,3,22])

[(3, 10), (4, 10), (2, 15), (3, 15), (4, 15), (2, 22), (3, 22), (4, 22)]
'''

'''combine: map(None,aaa,bbb)

>>> aaa = [10, 10, 10, 10, 15, 15, 15, 15, 3, 3, 3, 3, 22, 22, 22, 22]
>>> bbb = [1,2,3,4] * 4
>>> map(None,aaa,bbb)
[(10, 1), (10, 2), (10, 3), (10, 4), (15, 1), (15, 2), (15, 3), (15, 4), (3, 1), (3, 2), (3, 3), (3, 4), (22, 1), (22, 2), (22, 3), (22, 4)]
>>> bbb
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> map(None,bbb)
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
'''

"""  
while_FP = lambda: <condition> and (while_block() or while_FP())
while_FP()

<condition> 为 true  时 跳出循环


# statement-based while loop
while <condition>:
    <pre-suite>
    if <break_condition>:
        break
    else:
        <suite>

# Equivalent FP-style recursive while loop
def while_block():
    <pre-suite>
    if <break_condition>:
        return 1
    else:
        <suite>
    return 0
 
while_FP = lambda: <condition> and (while_block()  or  while_FP())
while_FP()

这里的难点在于，函数式while_FP循环采用了递归的概念。当<condition>为true时，进入循环体，执行while_block()；若<break_condition>为true时，返回1，while_FP()调用结束；若<break_condition>为false时，返回0，会继续执行or右侧的while_FP()，从而实现递归调用；若<break_condition>始终为false，则会持续递归调用while_FP()，这就实现了while语句中同样的功能


为了对函数式的while循环有更深刻的理解，可以再看下如下示例。这个例子是在网上找的，实现的是echo功能：输入任意非”quit”字符时，打印输入的字符；输入”quit”字符时，退出程序。

➜  PythonFP python pyecho.py
IMP -- 1
1
IMP -- 2
2
IMP -- abc
abc
IMP -- 1 + 1
1 + 1
IMP -- quit
quit
➜  PythonFP
如下便是分别采用过程式和函数式语句实现的”echo”功能。

# imperative version of "echo()"
def echo_IMP():
    while 1:
        x = raw_input("IMP -- ")
        print x
        if x == 'quit':
            break

echo_IMP()
def monadic_print(x):
    print x
    return x

# FP version of "echo()"
echo_FP = lambda: monadic_print(raw_input("FP -- "))=='quit' or echo_FP()       ## 这里就是 在 lambda 中出传递 函数。
echo_FP()

"""

'''递归 调用自己


>>> a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
>>> flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
>>> flatten(a)
[1, 2, 3, 4, 5, 6, 7, 8]
'''


'''flattening list
>>> a = [[1, 2], [3, 4], [5, 6]]
>>> sum(a, [])
[1, 2, 3, 4, 5, 6]

>>> reduce(lambda x,y : x+y,a)
[1, 2, 3, 4, 5, 6]



'''


# import copy
# import time


# def time_exec(fun):
#     start = time.time()
#     for _ in range(10):
#         fun
#     print "### time is ",time.time() - start

# a = range(1000)
# time_exec(copy.copy(a))
# time_exec(copy.deepcopy(a))   ## 这个 慢了一个 数量级



# def variable_tuple_unpack(*a):
#     print a

# ee = [1,2,3,4,5]
# variable_tuple_unpack(*ee)



# import time
# from contextlib import contextmanager


# @contextmanager
# def test_daiyi(aaa):
#     blist = ["this is a test for with: ", "2"]
#     blist = [2,4]
#     try:
#         yield
#     finally:
#         print('{}:  list is {}'.format(time.time(),
#                                        blist.append(j**2 for j in aaa)))
#         # print('{}:  list is {}'.format(time.time(), blist))


# alist = [1, 2, 3, 4]

# with test_daiyi(aaa=alist):
#     print [i**2 for i in alist if i % 2 == 0]



class Foo():
    def __get__(self, instance, owner):
        print('触发get')
    def __set__(self, instance, value):
        print('触发set')
    def __delete__(self, instance):
        print('触发delete')