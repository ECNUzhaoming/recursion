def zhiyinshu(n):
    for x in range(2,int(n/2+1)):
        if n%x==0:
            l.append(x)
            return zhiyinshu(n/x)
        l.append(int(n))
        print(l)
l=[]
zhiyinshu(90)