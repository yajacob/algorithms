str1 = "test 123"
list_str1 = list(str1)

stack = []
for _ in range(len(list_str1)):
    stack.append(list_str1.pop())

rev_str1 = "".join(stack)

print(rev_str1)
    