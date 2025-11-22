from heroes.hero import Hero

class Mage(Hero):
    def attack(self, target):
        damage = self.damage.calculate()
        target.hp -= damage
        print(f"{self.name} varázslattal támad és {damage} sebzést okoz {target.name}-nak")

        