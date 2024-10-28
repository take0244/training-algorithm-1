## https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0167


# def bubble_sort(array: list):
#     for i in range(len(array)):
#         for j in range(0, len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array = swap(array, j, j + 1)


def swap(array: list, a: int, b: int):
    array[a], array[b] = array[b], array[a]
    return array


def count_bubble_sort_swap(array: list):
    result = 0
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array = swap(array, j, j + 1)
                result += 1

    return result


while True:
    print(arr)
    n = int(input())
    if n == 0:
        break
    arr = []
    for i in range(n):
        arr.append(int(input()))

    print(count_bubble_sort_swap(arr))
