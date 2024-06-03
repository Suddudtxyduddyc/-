#111+"222"
#TypeError: can only concatenate str (not "int") to str
#нельзя склеивать текст и число
#1/0
#ZeroDivisionError: division by zero
#делить на ноль нельзя
int(45343/4)
ValueError: invalid literal for int() with base 10:  # type: ignore
'34.'
["1", "2", "3"].remove("4")
# ValueError: list.remove(x): x not in list
# из списка нельзя удалить такой объект, которого там нет
["1", "2", "3"].index("4")
# ValueError: 'Питер' is not in list
# искомый элемент отсутствует в списке
def привет():
    print()
привет("аргумент")
# TypeError: привет() takes 0 positional arguments but 1 was given
# функция не умеет принимать аргументы, но ей они были переданы при вызове

def привет(имя):
    print()
привет()
# привет() missing 1 required positional argument: 'имя'
# функция хочет получить на вход 1 обязательный аргумент 'имя', но при вызове он не был передан