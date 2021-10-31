num=[123, 234, 345, 456]
for i in num:
    print(i)
try:
    print(num.index(input("Введите число: ")))
except ValueError:
    print("This is not in the list")
