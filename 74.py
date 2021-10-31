colors= ("Красный", "Оранжевый", "Желтый", "Зеленый", "Голубой", "Синий", "Фиолетовый", "Коричневый", "Черный", "Серый")
for i in colors:
    print(i)
firstnum=int(input("Введите число от 0 до 4: "))
secondnum=int(input("Введите число от 5 до 9: "))
print(colors[firstnum:secondnum])
