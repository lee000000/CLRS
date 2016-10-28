# coding: utf-8

"""
Input: A sequence of n numbers a1 a2...ani.
Output: A permutation (reordering) a1' a2' a3',...,ai'
where ai <= ai+1 for all ai 
"""
def insertion_sort(a):
    j = 0
    while j < len(a):
        key = a[j]
        i = j - 1
        while i > -1 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
        j += 1
    return a


def binary_insertion_sort(a):
    j = 1 
    while j < len(a):
        key = a[j]
        k = j - 1
        if  k < 0:
            j += 1
            continue
        # assuming a[0: j - 1] is sorted
        # return the index for insertion
        i = binary_search(a, key, 0, k)
        while i <= k:
            a[k+1] = a[k]
            k -= 1
        a[k + 1] = key
        j += 1 
    return a


def binary_search(lst, result, low, high):
    if (high <= low ):
        if lst[low] < result:
            return low + 1 
        else:
            return low
    mid = int(( high + low ) / 2)
    if ( result == lst[mid] ):
        return mid
    if (result < lst[mid] ):
        high = mid - 1
    else:
        low = mid + 1
    return binary_search(lst, result, low, high)
        

if __name__ == "__main__":
    lst1 = [5, 2, 4, 6, 1, 3]
    lst2 = [1]
    lst3 = []
    lst4 = [5, 5, 3, 1, 4, 2]

    print("lst1 is ", lst1)
    print("lst2 is ", lst2)
    print("lst3 is ", lst3)
    print("lst4 is ", lst4)

    print("After sorting: ")
    print("sorted_lst1 is ", binary_insertion_sort(lst1))
    print("sorted_lst2 is ", binary_insertion_sort(lst2))
    print("sorted_lst3 is ", binary_insertion_sort(lst3))
    print("sorted_lst4 is ", binary_insertion_sort(lst4))
