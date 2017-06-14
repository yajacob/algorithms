import operator
a = [1, 2, 1, 0, 5, 2, 4, 2, 3, 0, 1, 3, 2, 4]

dic = {}
for no in a:
    if no in dic.keys(): 
        dic[no] += 1
    else:
        dic[no] = 1

print(dic)
sorted_dict = sorted(dic.items(), key=operator.itemgetter(1), reverse=True) 
for key, value in sorted_dict:
    print("%s" % key, end=" ")

