num=[123, 234, 345, 456]
for i in num:
    print(i)
num2 = int(input("Введите трехзначное число: "))
num.index(int(num2), [0, 3])

