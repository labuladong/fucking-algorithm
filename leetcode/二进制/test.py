
# -*- coding: utf-8 -*-
class bigmap(object):
    def __init__(self,_max):
        self._max = _max
        self.size = self.calcElemIndex(_max,True)
        self.array = [0 for i in range(self.size)]

    def calcElemIndex(self,num, up=False):
        if up:
            return int((num + 31 -1)/31)
        else:
            return num/31
    
    def calcBitIndex(self,num):
        return num % 31

    def set(self,num):
        elem_index = self.calcElemIndex(num)
        byte_idex = self.calcBitIndex(num)
        elem = self.array[elem_index]
        # print "### ",elem_index,'  elem=',elem ,'  byte_idex=', byte_idex, (1 << byte_idex),elem | (1 << byte_idex), '  num=',num
        self.array[elem_index] = elem | (1 << byte_idex)        ## 或运算 求和
    
    def clean(self, num):
        elem_index = self.calcElemIndex(num)
        byte_idex = self.calcBitIndex(num)
        elem = self.array[elem_index]
        self.array[elem_index] = elem & (~(1 << byte_idex))     ## 先取反， 与 运算

    def test(self, num):
        elem_index = self.calcElemIndex(num)
        byte_idex = self.calcBitIndex(num)
        elem = self.array[elem_index]
        # print "### ",elem_index,'  elem=',elem ,'  byte_idex=', byte_idex, (1 << byte_idex),elem | (1 << byte_idex), '  num=',num
        if elem & (1 << byte_idex):   ## 
            return True
        else:
            return False
    
    def sort(self,_list):
        _res = []
        for i in _list:
            self.set(i)
        for i in range(self._max+1):
            if self.test(i):
                _res.append(i)
        return _res

if __name__ == '__main__':
    _max = 200
    _bit = bigmap(_max)
    _array = [45,3,56,76,23,114,156,12,34,155]
    result = _bit.sort(_array)
    print '**result=', result
"""


















"""

