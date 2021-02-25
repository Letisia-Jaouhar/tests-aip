school = {"1А" : 17, "1Б" : 26, "2А" : 24, "2Б" : 25, "3А" : 18, "3Б" : 30}
chldr = 0

print(school)
print("Выберите действие (вводите число нужного действия): ")
print("1. Изменение кол-ва учеников в классу ")
print("2. Добавление нового класса (+ кол-во учеников)")
print("3. Удаление класса")
print("4. Подсчет общего кол-ва учащихся в школе")

choice = int(input())
if choice == 1:
   ed_class = input("Какой класс изменить?")
   a_chldr = input("Сколько человек?")
   if ed_class not in school:
       print("Такого класса нет")
   else:
       school[ed_class] = a_chldr
       print("Обновленно")
       print(new_class, a_chldr)
      
elif choice == 2:
    ed_class = input("Какой класс добавить")
    a_chldr = input("Сколько человек?")
    school[ed_class] = a_chldr
    print("Создан новый класс")
    print(school)
    
elif choice == 3:
    del_class = input("Какой класс удалить?")
    school.pop(del_class)
    print(school)
    
elif choice == 4:
    chldr = sum(school.values())
    print(chldr)
