class Dog:
    def __init__(self, nev, fajta):
        self.nev = nev
        self.fajta = fajta

    def ugat(self):
        print(f"{self.nev} {self.fajta} ugat: Vau vau!")

def dog_lista():
    nev = input("Mi a kutya neve?:")
    fajta = input("mi a kutya fajtája?:")

    kutya = Dog(nev, fajta)
    kutya.ugat()

def main():
    dog_lista()
if __name__ == "__main__":
    main()


class Book:
    def __init__(self, cim, szerzo, oldalszam):
        self.cim = cim
        self.szerzo = szerzo
        self.oldalszam = oldalszam


    def kiir(self):
        print(f"Cím: {self.cim}")
        print(f"Szerzo: {self.szerzo}")
        print(f"Oldalszam: {self.oldalszam}")

def main():
    konyv1 = Book("Vak asszony visszanéz", "Vaksi Ferenc", 200)
    konyv2 = Book("Utazás","Kiss Endre",260)

    konyv1.kiir()
    konyv2.kiir()

if __name__ == "__main__":
    main()



class Vehicle:
    def __init__(self, marka):
        self.marka = marka

class Car(Vehicle):
    def __init__(self, marka, modell):
        super().__init__(marka)
        self.model = modell

    def indul(self):
        print("Az autó elindult.")

def main():
    auto = Car("Mercedes-Benz","S class")
    auto.indul()

if __name__ == "__main__":
    main()


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Vau")

class Cat(Animal):
    def speak(self):
        print("Miau")

def main():
    kutya = Dog()
    macska = Cat()

    kutya.speak()
    macska.speak()

if __name__ == "__main__":
    main()


def make_animal_speak(animal):
    animal.speak()

def main():
    kutya = Dog()
    macska = Cat()

    make_animal_speak(kutya)
    make_animal_speak(macska)

if __name__ == "__main__":
    main()


class User:
    def __init__(self, nev, email):
        self.nev = nev
        self.email = email

class UserPrinter:
    def print_user(self, user):
        print("Felhasználó adatai:")
        print(f"Név:{user.nev}")
        print(f"Email: {user.email}")
        print("")

def main():
    user1 = User("Feri", "feri@gmail.com")
    user2 = User("Juli", "jucus@gmail.com")

    printer = UserPrinter()
    printer.print_user(user1)
    printer.print_user(user2)

if __name__ == "__main__":
    main()

