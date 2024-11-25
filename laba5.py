class Kinoteatr:
    def __init__(self, nameFilms, yerFilm=2015, cena=150):
        self.nameFilms = nameFilms  
        self.yerFilm = yerFilm  
        self.cena = cena  

    def filmTiket(self):
        print(f"Фильм: {self.nameFilms} / Год: {self.yerFilm} / Цена: {self.cena} рублей")


#второй класс насследник
class Session(Kinoteatr):
    def __init__(self, nameFilms, yerFilm=2015, cena=150, date="7-03-2001", start_time="19:00"):
       
        super().__init__(nameFilms, yerFilm, cena)
        self.date = date  
        self.start_time = start_time  

    def session_info(self):
        print(f"Сеанс фильма {self.nameFilms} состоится {self.date} в {self.start_time}.")

        self.filmTiket()  


kino = Session("Шрек часть первая", 2001, 200, "7-03-2001", "20:00")
kino.session_info()
kino.filmTiket()
