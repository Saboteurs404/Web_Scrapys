# # 追加：x
# x = 10
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a[len(a):] = [x]
# print(a)
# y = ['s', 'y', 'z']
# a[len(a):] = y
# print(a)
# y1 = 'sasd'
# a[len(a):] = y1
# print(a)
#
# y2 = {'as':1, 'asd':3}
# a[len(a):] = y2
# print(a)
#
# a[len(a):] = [y2]
# print(a)
import copy

# x = 10
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# a.insert(len(a), x)
# a.append(x)
# a[len(a):] = [x]
# a.extend([x])
# a.extend(x) # 'int' object is not iterable
# a.remove([10]) # ValueError: list.remove(x): x not in list
# a.pop(1)
# a.insert(1, 2)

# 等价
# a.clear()
# del a[:]



# x = 10
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# start = 2
# end = 8
# index = a.index(6, start, end)
# index = a.index(11)

# 等价
# print(a.sort(reverse = True))
# # b = sorted(a, reverse=True)
# print(a)
# print(b)
# print(ord('A'), ord('a'))
# s = ['Acf', 'Wasd', 'zdff', 'ads']
# print(sorted(s))
# # print(s)
# # print(s.sort())
# # print(s)

a = [1, 2, 3, 'q', 'asd', {'a': 12, 'b':13}, [4, 5, 6], {7, 8, 9}]
0
# list.copy()和a[:] 对比 和copy.copy(a) 以及 copy。deepcopy(a)之间的区别

# 浅层副本
# b = a.copy()
b = a[:]
b.pop()
b[-1][len(b[-1]):] = [7]
print(a)
print(b)
# [1, 2, 3, 'q', 'asd', {'a': 12, 'b': 13}, [4, 5, 6, 7], {8, 9, 7}]
# [1, 2, 3, 'q', 'asd', {'a': 12, 'b': 13}, [4, 5, 6, 7]]

a = [1, 2, 3, 'q', 'asd', {'a': 12, 'b':13}, [4, 5, 6], {7, 8, 9}]
b = a.copy()
c = copy.copy(a)
d = copy.deepcopy(a)

# c[-2][1] = -1
# print(a)
# print(b)
# print(c)
# print(d)
# [1, 2, 3, 'q', 'asd', {'a': 12, 'b': 13}, [4, -1, 6], {8, 9, 7}]
# [1, 2, 3, 'q', 'asd', {'a': 12, 'b': 13}, [4, -1, 6], {8, 9, 7}]
# [1, 2, 3, 'q', 'asd', {'a': 12, 'b': 13}, [4, -1, 6], {8, 9, 7}]
# [1, 2, 3, 'q', 'asd', {'a': 12, 'b': 13}, [4, 5, 6], {8, 9, 7}]

b.pop()
c.pop(-2)
d.pop(-3)
print('---------------------')
print(a)
print(b)
print(c)
print(d)
# ---------------------
# [1, 2, 3, 'q', 'asd', {'a': 12, 'b': 13}, [4, 5, 6], {8, 9, 7}]
# [1, 2, 3, 'q', 'asd', {'a': 12, 'b': 13}, [4, 5, 6]]
# [1, 2, 3, 'q', 'asd', {'a': 12, 'b': 13}, {8, 9, 7}]
# [1, 2, 3, 'q', 'asd', [4, 5, 6], {8, 9, 7}]
