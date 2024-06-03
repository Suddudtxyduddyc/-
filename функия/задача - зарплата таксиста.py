# Напишите программу, рассчитывающую стоимость поездки на такси в зависимости от расстояния.
# Базовый тариф составляет 150 р, в него включено 5 км, а цена за километр сверх минимума – 30 р.

# Результатом работы программы должна быть зарплата таксиста за месяц, при условии, что:
# - таксист получает 70% от стоимости каждого заказа
    # каждый заказ может быть в пределах от 2 до 20 км
    # - каждый день таксист начинает смену в разное время суток
    # - загруженность города в разное время суток отличается:
    #       с 7 до 9 - 40 км/ч
    #       с 9 до 17 - 60 км/ч
    #       с 17 до 18 - 30 км/ч
    #       с 18 до 20 - 50 км/ч
    #       с 20 до 7 утра - 60 км/ч
# - каждый пассажир садится в машину от 1 до 10 минут
# - между заказами у таксиста бывает простой от 0 до 15 минут
    # - один раз в день таксисту необходим обеденный перерыв
    #       он длится 1 час и начинается спустя примерно 4 часа после начала смены
    #       (после окончания заказа, который был взят менее чем за 4 часа работы)
    # - рабочая смена таксиста состоит из двух заходов по 4 часа (до обеда и после)
    # - необходимо учесть, что если заказ начат в 8:45, а проехать надо 50 км,
    #       то первые 15 минут таксист будет ехать со скоростью 40 км/ч, а позже 60 км/ч
# - предполагается, что в месяц таксист выходил на работу 20 раз
# - зарплата водителя расчитывается "на руки" - после вычета 13%
# - результат должен выводиться на экран в формате "81 484 р."
import datetime
def проверить_скорость(час):
    if час in range(7,9):
     return 40
    if час in range(17,18):
     return 30
    if час in range(18,20):
     return 50
    return 60

def сколько_км_проехал_за_минуту(час):
    скорость=проверить_скорость(час)
    return скорость/60

зарплата = 0
базовый_тариф = 150
км_включено_в_тариф = 5
цена_за_км_сверх_тарифа = 30
for день in range(20):
    начало_смены = datetime.datetime(2024, 5, 27, 8, 45, 0)
    сейчас=начало_смены
    for смена in range(2):
        while (сейчас-начало_смены).seconds<4*60*60:
            заказ = 50
            стоимость_заказа = базовый_тариф + (заказ - км_включено_в_тариф) * цена_за_км_сверх_тарифа
            дополнительная_стоимость=(заказ-км_включено_в_тариф)*цена_за_км_сверх_тарифа
            if дополнительная_стоимость<0:
                стоимость_заказа=базовый_тариф
            else:
                стоимость_заказа=базовый_тариф+дополнительная_стоимость
            зарплата+=стоимость_заказа*0.7
            ожидание=datetime.timedelta(minutes=10)
            сейчас+=ожидание
            проехал=0
            while заказ>проехал:
                проехал+=сколько_км_проехал_за_минуту(сейчас.hour)
                сейчас+=datetime.timedelta(minutes=1)
            простой=datetime.timedelta(minutes=15)
            сейчас+=простой
        сейчас+=datetime.timedelta(hours=1)
        начало_смены=сейчас
print(зарплата)     