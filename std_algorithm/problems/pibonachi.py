def pibo(pno):
    a = 0
    b = 1
    
    for n in range(pno):
        print("n: " + str(n) + " - "+ str(a))
        temp = a
        a = b
        b = temp + b

n = 10
pibo(n)
