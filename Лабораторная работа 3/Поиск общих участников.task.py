# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, razdel = ','): # функция принимающая две строки, в которых перечислены участники и аргумент, отвечающий за разделитель по умолчанию равен запятой
    first_list = first_group.split(razdel) # разбиваем строку первой группы в список, используя указанный разделитель
    second_list = second_group.split(razdel) # разбиваем строку второй группы в список, используя указанный разделитель
    set1 = set(first_list) # преобразуем первый список в множество
    set2 = set(second_list) # преобразуем второй список в множество
    x = set1.intersection(set2) # находим пересечение множеств общих участников, которые есть в обеих группах
    y = list(x) # преобразуем полученное множество обратно в список
    y.sort() # сортируем список в алфавитном порядке
    return y # возвращаем список
participants_first_group = "Иванов|Петров|Сидоров" # участники первой группы
participants_second_group = "Петров|Сидоров|Смирнов" # участники второй группы
result = find_common_participants(participants_first_group, participants_second_group, razdel='|') # вызываем функцию
print(result) # печатаем результат функции

# TODO Провеьте работу функции с разделителем отличным от запятой
