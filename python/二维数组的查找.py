# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array)
        col = len(array[0])
        cur_row = 0
        cur_col = col - 1
        while (cur_row < row and cur_col >= 0):
            if(array[cur_row][cur_col] == target):
                return True
            elif (array[cur_row][cur_col] < target):
                cur_row = cur_row + 1
            else:
                cur_col = cur_col - 1
        return False