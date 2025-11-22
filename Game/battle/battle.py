

class Battle:
    def __init__(self, hero1, hero2):
        self.hero1 = hero1
        self.hero2 = hero2

    def harc(self):
        print(f"Küzdelem:{self.hero1.name} - {self.hero2.name}")

    turn = 0
    while self.hero1.hp > 0 and self.hero2.hp > 0:
        if turn % 2 == 0:
            self.hero1.attack(self.hero2)
        else:
            self.hero2.attack(self.hero1)
        turn += 1

    gyoztes = self.hero1 if self.hero1.hp > 0 else self.hero2
    print(f"A győztes: {gyoztes}")
