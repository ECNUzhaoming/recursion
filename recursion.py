def calculate(a):
    if a>0:
        return  a+calculate(a-1);
    else:
        return 0;


print(calculate(50));

