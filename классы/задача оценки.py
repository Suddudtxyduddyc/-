источник = """Крюков Фёдор - 5,4,2,2,5,5,2,3,3,4,5,2,4
Карпова Маргарита - 4,4,4,5,2,2,2
Зайцева Милана - 5,3,3,5,2,4,2,2
Семенова Ева - 3,3,3,4,2,2,4,2,2,2,4,2,3,4,3,4
Беликов Мирон - 5,2,4,5,5,4,2,4,5,3,2,4,3,2,5,4
Корнева Ева - 4,5,5,3,5
Кошелева Ульяна - 2,4,3,2,3,2,3,3,5,2,5,4,3,3,5,5
Попов Платон - 4,4,3,2,2,4,3,5,3,5,2,3,2,5,3,4,3,5,4,4
Миронов Даниил - 5,3,5,3,3,2,3
Максимов Дмитрий - 3,5,2,3,2,2,3,2,2,2,5,4,2,4,3,4,5,3
Новикова Ева - 4,3,4,5,2,5,4,5,4,3,4,3,2,5
Овчинникова Виктория - 2,5,4,2,2,3,3,5,2,3
Астахова Алиса - 2,3,3,3,2,3,5,4,4
Михайлова София - 3,4,4,4,4,2
Агеева София - 4,3,5,2,3,5,4,3,5
Андреева Евгения - 4,3,5,3,5,5
Зубков Егор - 3,3,5,2,2,3,5,3,2,4,2,5,2,5
Широкова Полина - 3,3,5,2,4,2,5,3,3,5,5,5,2,2,4,5,4,2
Кузьмин Марк - 5,5,5,3,5,5,4,5,2,3
Федоров Давид - 3,5,2,3,3,3,3,4,2,3,4,5,5
Колесникова Сафия - 5,2,3,2,5,2,2,2,2,5,3,4,2,4
Терентьев Александр - 4,5,5,4,3,2,4,3,2,2,5,4,5,4
Карпов Максим - 4,4,3,4,4,4,2,5,3,5,4,4,3,2,2,3,4,2,3
Кононова Анна - 5,3,3,2,2,4,2,5,4,5,5,4
Русакова Елизавета - 4,3,3,4,2,2
Иванова Маргарита - 5,2,2,4,3,4,4,4,3,5,4,2,5
Морозова София - 2,3,3,4,4,2,5,3,5,5,2,3,5,2,4,3,3,4,4
Евдокимова София - 2,5,4,5,4,2,4,2,3,4,5,3,2"""
class Ученик:
    def __init__(self,строка) -> None:
     self.имя=""
     self.фамилия=""
     self.оценки=[]
     self.средний_бал="ещё не посчитан"
     self.узнать_фамилию_и_имя(строка)
     self.узнать_средний_бал()
    def узнать_фамилию_и_имя(self,строка):
        фамилия_и_оценки=строка.split(" - ")
        self.фамилия,self.имя=фамилия_и_оценки[0].split()
        self.сформировать_список_оценок(фамилия_и_оценки [1])
    
    def сформировать_список_оценок(self,оценки):
        все_оценки=оценки.split(",")
        for оценка in все_оценки:
            self.оценки.append(int(оценка))
    
    def узнать_средний_бал(self):
     self.средний_бал=sum(self.оценки)/len(self.оценки)
    
все_ученики=источник.splitlines()
for ученики in все_ученики:
    ученик_экз=Ученик(ученики)
    print(f"{ученик_экз.имя}{ученик_экз.фамилия}{ученик_экз.средний_бал}")