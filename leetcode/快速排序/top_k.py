'''
快排基础上修改支点，使支点不会出现在最大点或最小点，使最坏情况得到优化
方法：把列表分割成多个小组，每个小组5个元素
取所有小组的中位数成一个新列表
重复上诉操作，直到剩下一个支点
(还没进行优化)
'''


def Inorsort(arr, left, right):
    temp = arr[left:right + 1]
    temp.sort()
    arr[left:right + 1] = temp
    return (left + right + 1) >> 1


def GetMeanMark(arr, left, right):
    if right - left + 1 <= 5:
        return Inorsort(arr, left, right)
    sub_right = left - 1
    i = left
    while (i + 4 <= right):
        Inorsort(arr, i, i + 4)
        sub_right += 1
        arr[sub_right], arr[i + 2] = arr[i + 2], arr[sub_right]
        i += 5
    return GetMeanMark(arr, left, sub_right)


def GetPivotMark(arr, left, right, mean_mark):
    #快速排序写法
    arr[right], arr[mean_mark] = arr[mean_mark], arr[right]
    temp_mark = left
    for i in range(left, right):
        if arr[i] < arr[right]:
            arr[i], arr[temp_mark] = arr[temp_mark], arr[i]
            temp_mark += 1
    arr[right], arr[temp_mark] = arr[temp_mark], arr[right]
    return temp_mark


def bfprt_test(arr, left, right, k: int):
    mean_mark = GetMeanMark(arr, left, right)
    pivot_mark = GetPivotMark(arr, left, right, mean_mark)
    if pivot_mark == k:
        return pivot_mark
    if pivot_mark > k:
        return bfprt_test(arr, left, pivot_mark - 1, k)
    else:
        print(pivot_mark + 1, right)
        return bfprt_test(arr, pivot_mark + 1, right, k)

    
if __name__ == '__main__':
    arr = [0, 0, 1, 2, 4, 2, 2, 3, 1, 4]
    result = bfprt_test(arr, 0, len(arr) - 1, 8)
    print(arr[:result])
