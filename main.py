import csv
import datetime


class Pizza:
    def __init__(self, description, cost, soslar):
        self.description = description
        self.cost = cost
        self.soslar = []

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 20, [])


class Margarita(Pizza):
    def __init__(self):
        super().__init__("Margarita", 20, [])


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza", 30, [])


class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 15, [])


class Decorator():
    def __init__(self, desc, cost):
        self.desc = desc
        self.cost = cost

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.desc


class Zeytin(Decorator):
    def __init__(self):
        super().__init__("Zeytinli", 4)


class Mantarlar(Decorator):
    def __init__(self):
        super().__init__("Mantarlı", 5)


class KeciPeyniri(Decorator):
    def __init__(self):
        super().__init__("Keçi Peynirli", 9)


class Et(Decorator):
    def __init__(self):
        super().__init__("Etli", 13)


class Sogan(Decorator):
    def __init__(self):
        super().__init__("Soğanlı", 5)


class Misir(Decorator):
    def __init__(self):
        super().__init__("Mısırlı", 4)


def kredi_karti(ucret):
    ad = input("Ad: ")
    tc = input("TC: ")
    while len(tc) != 11:
        tc = input("TC: ")
    kart_no = input("Kart No: ")
    while len(kart_no) != 16:
        kart_no = input("Kart No: ")
    sifre = input("Şifre: ")
    while len(sifre) != 4:
        sifre = input("Şifre: ")
    with open("Orders_Database.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ad, tc, kart_no, sifre, ucret, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])


def main():
    global sos
    f = open('Menu.txt', 'r')
    menu = f.read()
    print(menu)
    f.close()
    cost = 0
    description = ""
    pizza = None
    while pizza is None:
        pizza_num = input("Pizza tabani seciniz: ")
        while len(pizza_num) < 1 or len(pizza_num) > 4:
            pizza_num = input("Pizza tabani seciniz: ")
        if pizza_num == "1":
            pizza = KlasikPizza()
            cost += int(pizza.get_cost())
        elif pizza_num == "2":
            pizza = Margarita()
            cost += int(pizza.get_cost())
        elif pizza_num == "3":
            pizza = TurkPizza()
            cost += int(pizza.get_cost())
        elif pizza_num == "4":
            pizza = SadePizza()
            cost += int(pizza.get_cost())
        else:
            print("Gecerli bir pizza tabani seciniz: ")

    daha_sos = True
    while daha_sos:
        sos_num = input("Sos seciniz: ")
        while int(sos_num) < 11 or int(sos_num) > 16:
            sos_num = input("Sos seciniz: ")
        if sos_num == "11":
            sos = Zeytin()
        elif sos_num == "12":
            sos = Mantarlar()
        elif sos_num == "13":
            sos = KeciPeyniri()
        elif sos_num == "14":
            sos = Et()
        elif sos_num == "15":
            sos = Sogan()
        elif sos_num == "16":
            sos = Misir()
        if (sos_num == "11" or sos_num == "12" or sos_num == "13" or
                sos_num == "14" or sos_num == "15" or sos_num == "16"):
            pizza.soslar.append(sos)
            cost += int(sos.get_cost())
            description += sos.get_description() + " "
        yesno = input("Sos eklemek ister misiniz?(y/n)")
        if (yesno == "y"):
            daha_sos = True
            description += ", "
        else:
            daha_sos = False

    description += pizza.get_description() + " hazırlandı."
    print(description)
    print("Ücret: " + str(cost))
    with open("Orders_Database.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["AD", "TC", "KART NO", "SIFRE", "UCRET", "TARIH"])
    kredi_karti(cost)


if __name__ == "__main__":
    main()
