def calculate(a,b):
    return a*a + 2*a*b + b*b

print((lambda a,b: a*a + 2*a*b + b*b) (2,3))
print(calculate(2,3))