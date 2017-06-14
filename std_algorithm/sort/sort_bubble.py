def bubblesort(alist):
    for i in range(len(alist)):
        for j in range(len(alist) - 1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist

test_list = [3,2,5,1]
print(test_list)
print(bubblesort(test_list))
