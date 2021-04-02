from python_practice.timo import Timo
from python_practice.police import police


# 创建英雄工厂
class HeroFactory:
    def create_hero(self, name):
        if name == 'Timo':
            return Timo()
        elif name == "Police":
            return police()
        else:
            raise Exception('此英雄不再英雄工厂中')


if __name__ == '__main__':
    hero_factory = HeroFactory()
    timo = hero_factory.create_hero("Timo")
    police_name = hero_factory.create_hero("Police")
    # timo.speak_lines()
    police_name.speak_lines()
    timo.fight(police_name.name, police_name.hp, police_name.power)

