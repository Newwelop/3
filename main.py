import random
class Human:

    def __init__(self, name, home=None, car=None):
        self.name = name
        self.money = 200
        self.enjoyment = 100
        self.home = home
        self.car = car

    def get_home(self, home):
        if home != None:
            print("Продали будинок")

        self.home = home
        print("Прибдали новий будинок")

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
        self.cleanlinies_level -= 20

    def shopping(self):
        if self.car != None:
            print(f"я не можу туди поїхати")
        else:
            print(f"я сьогодні був у магазині у мне залишок {self.money}")

            self.food += 1
            self.food = self.food

            self.money -=7

        pass

    def clean_house (self):
        if self.home != None:
            print(f"ти не можешь прибратися")
        else:
            print("пішли прибиратися")
            self.cleanlinies_level += 1
            self.enjoyment -= 3
            self.cleanlinies_level = self.cleanlinies_level



    def life(self):
        pass
    def is_alive(self):
        pass


class Car:

    def __init__(self, marka):
        self.marka = marka
        self.passengers = []




class Home:
    def __init__(self):
        self.food = 0
        self.cleanlinies_level = 50

