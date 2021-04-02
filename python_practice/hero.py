# 创建父类
class Hero:
    hp= 0
    power = 0
    name = ''
    # def __init__(self, hp, power, name):
    #     self.hp = hp
    #     self.power = power
    #     self.name = name

    # 战斗方法（和别人对打，传入对手的信息）
    def fight(self, enemy, enemy_hp, enemy_power):
        """

        :param enemy:   创建变量-敌人
        :param enemy_hp: 敌人的血量
        :param enemy_power:  敌人的力量
        :return:
        """
        # 我的血量
        final_hp = self.hp - enemy_power
        # 敌人的血量
        enemy_final_hp = enemy_hp - self.power
        # 进行较量，一决雌雄
        if final_hp > enemy_final_hp:
            print(f"{self.name}赢了, {enemy}输了。")
        elif final_hp < enemy_final_hp:
            print(f"{enemy}赢了，{self.name}输了。")
        else:
            print(f"{self.name}和{enemy}打平局了！")

    def speak_lines(self):
        if self.name == "Timo":
            print("提莫队长正在待命")
        elif self.name == "police":
            print("见识一下法律的子弹")
        else:
            print("无台词显示")
