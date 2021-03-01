x = 11
a = x
for aa in range(10):
    for i in range(2,5+1):
        print(x, i)
        x=x-(x/i+1/i)
    if x == 11:
        print(a)
        break
    a = a+1
    x =a