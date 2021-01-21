# 使用堆(heapq只生成了最小堆，并没有排序)


def getLeastNumbers(arr, k: int):
    import heapq
    if k == 0:
        return list()

    hp = [-x for x in arr[:k]]
    heapq.heapify(hp)
    print(hp)
    for i in range(k, len(arr)):
        if -hp[0] > arr[i]:
            heapq.heappop(hp)
            print(hp)
            heapq.heappush(hp, -arr[i])
            print(hp)
    ans = [-x for x in hp]
    return ans


if __name__ == '__main__':
    arr = [0, 0, 1, 2, 4, 2, 2, 3, 1, 4]
    print(getLeastNumbers(arr, 8))
