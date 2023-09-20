# 列表推导式

# 正方形
'''
    使用for循环创建（或覆盖）一个名为x 的变量，
    该变量再循环完成后仍然存在。
'''
squares = []
for x in range(10):
    # 等价于squares.append(x**2)
    # 等价于 squares.extend([x**2])
    squares[len(squares):] = [x**2]
print(squares)


# 我们可以使用以下方法计算没有任何副作用的正方形列表

squares_new = list(map(lambda x: x**2, range(10) ))
print(squares_new)

# 或者等效的：
squares_new_1 = [x**2 for x in range(10)]
print(squares_new_1)

list_new = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(list_new)

print('----------------')
# 嵌套列表推导式
# matrix矩阵
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

result = []
temp = []
# list_matrix = [[row[i] for row in matrix] for i in range(4)]
# print(list_matrix)

for i in range(4):
    for row in matrix:
        temp.append(row[i])
    result.extend([temp])
    print(result)
    # temp = []
print(result)


for i in range(10):
    if i>10:
        break
else:
    print(i)


print(list(zip(*matrix)))