import random
class Human:

    def __init__(self, name, home=None, car=None):
        self.name = name
        self.money = 200
        self.enjoyment = 100
        self.home = home
        self.car = car

    def get_home(self, home):
        self.home = home

    def get_car(self, car):
        if car != None:
            print(f"Продали авто марки {car.marka}")
        self.car = car
        print(f"придбана автівка, марка{car.marka}")

    def work(self):
        print("ідем працювати")
        money = random.randint(5, 20)
        print(f"Сьогодні заробили {money}")
        self.money += money
        self.enjoyment -= 5
    def chill(self):
        pass
    def shoping(self):
        pass

    def clean_house (self):
        pass
    def life(self):
        pass
    def is_alive(self):
        pass


class Car:

    def __init__(self, marka):
        self.marka = marka
        self.passengers = []


    def add_passengers(self, human):
        self.passengers.append(human)
    def passengers_info(self):
            print(f"Авто {self.marka}, ", end='')
            if self.passengers != []:
                print(f"зараз в салоны:")
                for p in self.passengers:
                    print(p.name)
                else:
                    print("немає пасажирів")

class Home:
    def __init__(self):
        self.food = 0
        self.cleanlinies_level = 50