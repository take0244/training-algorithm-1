# # https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_C&lang=ja
import copy


def swap(arr: list, i, j: int) -> list:
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def partition(arr: list, start, end: int, listGetter) -> (list, int):
    pivot = listGetter(arr, end)
    p = start
    for i in range(start, end):
        if listGetter(arr, i) <= pivot:
            swap(arr, p, i)
            p += 1

    return swap(arr, p, end), p


def quick_sort(arr: list, start, end: int, listGetter):
    if start < end:
        # print(arr, start, end, ":", arr[start:end + 1], end="->")
        _, p = partition(arr, start, end, listGetter)
        # print(arr[start:end + 1], "left:", arr[start:p], "right:", arr[p + 1:end + 1], p)
        quick_sort(arr, start, p - 1, listGetter)
        quick_sort(arr, p + 1, end, listGetter)
    return arr


class Value:
    value: int
    key: str

    def __init__(self, value: int, key: str):
        self.value = value
        self.key = key


if __name__ == '__main__':
    arr = []
    n = int(input())

    for i in range(n):
        kv = input().split(" ")
        arr.append(Value(key=kv[0], value=int(kv[1])))

    stabled = sorted(copy.deepcopy(arr), key=lambda x: x.value)
    quick_sort(arr, 0, len(arr) - 1, lambda a, i: a[i].value)

    isStable = True
    for i, v in enumerate(stabled):
        if arr[i].key != v.key or arr[i].value != v.value:
            isStable = False
            break

    print("Stable" if isStable else "Not stable")
    for v in arr:
        print(v.key, v.value)
