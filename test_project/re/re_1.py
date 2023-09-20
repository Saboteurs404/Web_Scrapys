import re

# findall():查找所有，返回list
lst = re.findall("\d+", "今天6点，我跑了15000m")
print(lst)

# search():进行匹配，如果匹配到了都一个结果，就返回这个结果，如果匹配不到返回None
lst_2 = re.search("\d+", "今天6点,我跑了15000m")
print(lst_2)

# match():只能从字符的开头进行匹配
lst_3 = re.match("\d+", "9今天6点,我跑了15000m")
print(lst_3)
lst_4 = re.match("\d+", "今天6点,我跑了15000m")
print(lst_4)

#  finditer()：和findall差不多，只不过他返回的是迭代器

lst_5 = re.finditer("\d+", "今天6点,我跑了15000m")
for item in lst_5:
    print(item.group())

# compile():预加载正则表达式

lst_6 = re.compile("\D+").findall("今天6点，我跑了15000m")
# lst_6 = obj_s.findall("今天6点，我跑了15000m")
print(lst_6)
