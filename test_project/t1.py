'''
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

示例 1：
输入：s = "([)]"
输出：false

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

提示：
1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

输入案例：
[{}](
[()]}
[{]}

'''

s = '''
qwqeqwqwe  12312 
123213  123kj21
qweoiqwnksadiu12as
'''

print(s)
def solution(s):
    n = len(s)
    temp = {')': '(', '}': '{', ']': '['}
    stack = []
    if n % 2 != 0:
        return False

    for i in range(n):
        if s[i] in temp and len(stack) != 0:
            t = stack.pop()
            if t != temp[s[i]]:
                return False
        elif s[i] in temp and len(stack) == 0:
            return False
        else:
            stack.append(s[i])
    if len(stack) == 0:
        return True
    else:
        return False


# s = "([)]"
# s = "()[]{}"
s = "(]"
print(solution(s))
