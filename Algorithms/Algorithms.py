# Бинарный поиск


# def binary_search(n, lst):
#     low = 0
#     high = len(lst) - 1
#     while low <= high:
#         mid = (low + high)//2
#         guess = lst[mid]
#         if guess == n:
#             return mid
#         if guess < n:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None
#
# print(binary_search(50, [i for i in range(0,100,2)]))


# Сортировка с выбором


# lst = [-3, 5, 0, -8, 1, 10]
#
# def sorting(arr):
#     lst = []
#     for i in range(len(arr)):
#         smallest = arr.index(min(arr))
#         lst.append(arr.pop(smallest))
#     return lst
#
# print(sorting(lst))


# Сортирвка с выбором двойной

# lst = [-3, 5, 0, -8, 1, 10]
#
# def sorting_1(lst):
#     count = len(lst)
#     for i in range(count-1):
#         mini = lst[i]
#         index = i
#         for j in range(i+1, count):
#             if mini > lst[j]:
#                 mini = lst[j]
#                 index = j
#         if index != i:
#             lst[i], lst[index] = lst[index], lst[i]
#
#
# sorting_1(lst)
# print(lst)


# Сумма массива с помощью рекурсии

# lst = [1,2,5,7,8,3,2]
#
# def summ(lst):
#     if lst:
#         return lst[0] + summ(lst[1:])
#     else:
#         return 0
#
# print(summ(lst))


# Бинарный поиск с помощью рекурсии

# lst = [i for i in range(0,100, 2)]
# def binar(lst, mini, maxi, n):
#
#     mid = (mini + maxi)//2
#     guess = lst[mid]
#     if guess > n:
#         return binar(lst, mini, maxi-1, n)
#     elif guess < n:
#         return binar(lst, mini, maxi+1, n)
#     elif guess == n:
#         return mid
#     else:
#         return None
#
# print(binar(lst, 0, len(lst)-1, 56))


# Быстрая сортировка

def qsort(lst):
    if len(lst) < 2:
        return lst

    point = lst[0]

    left = list(filter(lambda x:x<point, lst))
    mid = [i for i in lst if i == point]
    right = [i for i in lst if i > point]

    return qsort(left) + mid + qsort(right)

lst = [2,6,9,45,345,9,4,237,9,0,34,68,2,46,872,35,7,4234,6,8465,8,3,56,82,345,7]

print(qsort(lst))


# Алгоритм Евклида

# n1 = int(input())
# n2 = int(input())
#
# while n1 != n2:
#     if n1 > n2:
#         n1 -= n2
#     else:
#         n2 -= n1
#
# print(n1)


# Алгоритм Евклида 1

# n1 = int(input())
# n2 = int(input())
#
# while n2 > 0:
#     n1, n2 = n2, n1 % n2
#
# print(n1)


# Слияние списков и сортировка слияния

# def merge_lst(lst1, lst2):
#     a = len(lst1)
#     b = len(lst2)
#     i = j = 0
#     lst3 = []
#     while i < a and j < b:
#         if lst1[i] > lst2[j]:
#             lst3.append(lst2[j])
#             j+=1
#         else:
#             lst3.append(lst1[i])
#             i+=1
#     while i < a:
#         lst3.append(lst1[i])
#         i += 1
#     while j < b:
#         lst3.append(lst2[j])
#         j += 1
#     return lst3
#
#
# def merge_sort(s):
#     if len(s) == 1:
#         return s
#     mid = len(s) // 2
#     right = merge_sort(s[mid:])
#     left = merge_sort(s[:mid])
#     return merge_lst(right, left)
#
# print(merge_sort([4,7,8,93,1,3,5,7,4,2,5,45,657,4,34,2]))


# Сортировка пузырьком

# def buble(lst, n):
#     for j in range(n-1):
#         for i in range(n-1-j):
#             if lst[i] > lst[i+1]:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#     return lst
#
# print(buble([5,7,4,3,8,2], 6))