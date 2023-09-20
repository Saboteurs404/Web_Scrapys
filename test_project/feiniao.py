import copy


# class Solution:
def max_string(A):
    A = list(A)
    A_list = copy.deepcopy(A)
    A_list.sort()
    # 获取最大字母
    s_max = A_list[0]
    # 该字母在原序列中对应的位置
    s_index = A.index(s_max)
    print(s_index)
    # 切片
    s_temp = A[s_index+1:]
    print(s_temp)
    # 最终结果
    res = []
    res.append(s_max)

    while s_temp:
        temp = copy.deepcopy(s_temp)
        s_temp.sort()
        print(temp)
        # 字串中最大字母
        s_max = s_temp[0]
        # print(s_max)
        # 字串中对应的位置
        s_index = temp.index(s_max)
        # print(s_index)
        # 切片+
        if len(temp) == 1:
            res.append(temp[0])
        else:
            s_temp = temp[s_index + 1:]
            print(s_temp)
             # 最终结果
            res.append(s_max)
    print(res)
    return res

st = 'asfasfqhZZqweqweqw'
max_string(st)
