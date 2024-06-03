# Список позволяет хранить неограниченное количество других значений и переменных вне зависимости от их типа.
# Список является итерируемым объектом - он состоит из элементов. Они подчиняются правилам индекса
# Список создаётся в квадратных скобках. Элементы разделены запятой
города=[]
города=["Коломна","Москва","Рязань"]
#добавление
города.append("Питер")
города==["Коломна","Москва","Рязань""питер"]
#добавление 1 элемента по индексу,
города.insert(1,"Воскресенкс")
#замена элемента
города[4]="Санкт-петербург"
города==["Коломна","Москва","Рязань""питер"]
города.pop()=="Санкт петебург"
#удалить последний элемент
#функция pop УМЕЕТ принимать номер индекса по которому мы хотим удалить элемент
города.pop(1)=="воскресенкс"
#удалить по названию
города.remove("Москва")
["1", "2", "3"].remove("4")
# если через append добавить новый список, он добавится как целиковый элемент
города.append(["Краснодар", "Ростов-на-Дону", "Адлер"])
города == ["Коломна", "Рязань", ["Краснодар", "Ростов-на-Дону", "Адлер"]]
города.pop() == ["Краснодар", "Ростов-на-Дону", "Адлер"] # удалили последний элемент, весь список

# если нужно добавить все элементы нового списка в существующий, то нужно использовать функцию extend
города.extend(["Краснодар", "Ростов-на-Дону", "Адлер"])
города == ["Коломна", "Рязань", "Краснодар", "Ростов-на-Дону", "Адлер"]
города.sort()
#отсортировать от а до я или от 0 до 9
# обратить список в обратный порядок
города.reverse()
города == ['Адлер', 'Ростов-на-Дону', 'Краснодар', 'Рязань', 'Коломна']

# отсортировать от А до Я или от 1 до 9
города.sort()
города == ['Адлер', 'Коломна', 'Краснодар', 'Ростов-на-Дону', 'Рязань']

# отсортировать от Я до А или от 9 до 1
города.sort(reverse=True)
города == ['Рязань', 'Ростов-на-Дону', 'Краснодар', 'Коломна', 'Адлер']
