def Gen(n):
    for i in range(n):
        yield i
    # a,b=0,1
    # a=0
    # b=1
    # while a<n:
    #     # print("value A : ",a)
    #     # print("value B : ",b)
    #     yield a
    #     a, b = b, a + b
    #     # a=b
    #     # b=a+b

Gen_1=Gen(10)

# Type 1st
print(Gen_1.__next__())
print(Gen_1.__next__())
print(Gen_1.__next__())
print(Gen_1.__next__())
print(Gen_1.__next__())
print(Gen_1.__next__())

# Type 2nd
print(next(Gen_1))
print(next(Gen_1))
print(next(Gen_1))
