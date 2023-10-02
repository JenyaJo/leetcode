class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack1 = 0
        stack2 = 0
        stack3 = 0
        for i in s:
            if i == '(':
                stack1 += 1
                stack.append(i)
            elif i == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack1 -= 1
                    stack.pop()
                else:
                    return False
            elif i == '[':
                stack2 += 1
                stack.append(i)
            elif i == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack2 -= 1
                    stack.pop()
                else:
                    return False
            elif i == '{':
                stack3 += 1
                stack.append(i)
            elif i == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    stack3 -= 1
                    stack.pop()
                else:
                    return False
            if stack1 < 0 or stack2 < 0 or stack3 < 0:
                return False

        if stack1 == stack2 == stack3 == 0:
            return True
        else:
            return False