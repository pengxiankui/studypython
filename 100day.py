# 斐波拉契数

# a = 0
# b = 1
# for i in range(100):
#         c = b
#         b = a+b
#         a = c
#         print(a)
#
# a = 0
# b = 1
# for _ in range(20):
#     (a, b) = (b, a + b)
#     print(a, end=' ')

#水仙花数

# for i in range(100, 1000):
#         a = i//100
#         b = (i - a*100)//10
#         c = i - a*100 - b*10
#         if (a**3 + b**3 + c**3) == i:
#                 print(i)

# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)
#取模运算符 %
#整除运算符 //

# 完美数
for num in range (10000):
    numa = num
    for i in range(numa):
        if 