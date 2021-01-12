# 스택 예제

'''
stack -> list
push -> append()
pop -> pop()

Last In First Out
'''

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(8)
stack.pop()

print(stack)
print(stack[::-1])