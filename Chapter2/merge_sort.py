# coding = utf-8

import random


"""
Mergesort O(nlogn)
"""
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = int(len(lst)/2)
    return merge(merge_sort(lst[0 : mid]), 
            merge_sort(lst[mid : len(lst)]))


def merge(left, right):
    i_left = 0
    i_right = 0
    left_len = len(left)
    right_len = len(right)
    result = []
    while (i_left < left_len and i_right < right_len):
        if (left[i_left] < right[i_right]):
            result.append(left[i_left])
            i_left += 1
        else:
            result.append(right[i_right])
            i_right += 1
    
    while (i_right < right_len ):
        result.append(right[i_right])
        i_right += 1

    while (i_left < left_len):
        result.append(left[i_left])
        i_left += 1

    return result



if __name__ == "__main__":
    lst1 = [ random.randint(1,100) for i in range(10) ]
    lst2 = [2, 3, 7, 1, 4, 9, 6, 8, 0]
    lst3 = [2]
    lst4 = []
    print("lst1 is ", lst1)
    print("after merge sort:")
    print("lst1 is ", merge_sort(lst1))
    print("+++++++++++++++++++++++++++++++++++")
    print("lst2 is ", lst2)
    print("after merge sort:")
    print("lst2 is ", merge_sort(lst2))
    print("+++++++++++++++++++++++++++++++++++")
    print("lst3 is ", lst3)
    print("after merge sort:")
    print("lst3 is ", merge_sort(lst3))
    print("+++++++++++++++++++++++++++++++++++")
    print("lst4 is ", lst4)
    print("after merge sort:")
    print("lst4 is ", merge_sort(lst4))
    print("+++++++++++++++++++++++++++++++++++")
