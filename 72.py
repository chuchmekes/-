lessons=["Математика", "Физика", "Английский Язык", "Русский Язык", "Астрономия", "География"]
for i in lessons:
    print(i)
    lessons.remove(input("Введите урок, который хотите удалить из списка: ").capitalize())
print(lessons)

