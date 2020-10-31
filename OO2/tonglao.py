class TongLao():
    hp = ""
    power = ""

    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self, name):
        if name == 'WYZ':
            print("师弟！！！！")
        elif name == "李秋水":
            print("师弟是我的！")
        elif name == "丁春秋":
            print("叛徒！我杀了你")

    def fight_zms(self, enemyHp, enemyPower):
        self.hp /= 2
        self.power *= 10

        self.hp -= enemyPower
        enemyHp -= self.power

        if self.hp > 0 and self.hp > enemyHp:
            print("童姥获胜")
        elif enemyHp > 0 and self.hp < enemyHp:
            print("敌方获胜")
        else:
            print("双方打和")
