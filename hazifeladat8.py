import json

class Vehicle:
    def __init__(self, tipus, gyarto, ev):
        self.type = type
        self.gyarto = gyarto
        self.ev = ev

    def to_dictionary(self):
        return {
            "type": self.tipus,
            "manufacturer": self.gyarto,
            "year": self.ev
        }

class Car(Vehicle):
    def __init__(self, gyarto, ev, ajtok_szama):
        super().__init__("Személyautó", gyarto, ev)
        self.ajtok_szama = ajtok_szama

    def to_dictionary(self):
        alap = super().to_dictionary()
        alap["ajtok_szama"] = self.ajtok_szama
        return alap


class Truck(Vehicle):
    def __init__(self, gyarto, ev, teherbiras):
        super().__init__("Teherautó", gyarto, ev)
        self.teherbiras = teherbiras

    def to_dictionary(self):
        alap = super().to_dictionary()
        alap["teherbiras"] = self.teherbiras
        return alap

class CarPark:
    def __init__(self, fajlnev):
        self.fajlnev = fajlnev
        self.jarmuvek = self._betoltes()

    def _betoltes(self):
        try:
            with open(self.fajlnev, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def _mentes(self):
        with open(self.fajlnev, "w", encoding="utf-8") as f:
            json.dump(self.jarmuvek, f, indent=4, ensure_ascii=False)

    def hozzaad(self, jarmu):
        self.jarmuvek.append(jarmu.to_dictionary())
        self._mentes()

    def torol(self, index):
        if 0 <= index < len(self.jarmuvek):
            self.jarmuvek.pop(index)
            self._mentes()

    def lista(self):
        return self.jarmuvek