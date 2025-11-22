from heroes.hero import Hero

class Archer(Hero):
    def attack(self, target):
        damage = self.damage.calculate()
        target.hp -= damage
        print(f"{self.name} íjjal lő és {damage} sebzést okoz {target.name}-nak!")