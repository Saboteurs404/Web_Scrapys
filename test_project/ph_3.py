import copy

t = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5}
f = t
f.pop('1')
for i in t:
    print(i)

a1 = [1, 2, 3]
a2 = 'asfda'
a3 = {'asd':[1,2,4,5]}
a4 = [1, 2, 3, [1, 2, 3, 4] , 5]

#
# f2 = copy.deepcopy(a4)
# f2.pop()
# print("---------")
# print(f2)
# print(a1)

f3 = copy.copy(a4)
f3.pop()
f3[-1].append(55)
f3.append(18)
print(f3)
print(a4)