# for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
#     print(item)
# print('\n')
#
# for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice', 'test'], strict=False):
#     print(item)
# print('\n')
#
# for item in zip([1, 2, 3, 4], ['sugar', 'spice', 'everything nice']):
#     print(item)
#
# print(zip([1, 2, 3, 4], ['sugar', 'spice', 'everything nice']))

# x = [1, 2, 3]
# y = [4, 5, 6]
# zip_1 = list(zip(x, y))
# print(zip_1)

# # *用于解压缩列表
# x2, y2 = zip(*zip(x, y))
# print(x2)
# print(y2)
# print(zip([1, 2 , 3], ['1', '2', '3']))

a = [-1, 1, 66, 25, 333, 333, 1234, 5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)


