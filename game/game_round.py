import random


def fight(enemy_hp, enemy_power):
    # 初始化我方血量和攻击力
    my_hp = 1000
    my_power = 200

    # 模拟攻击，然后扣血的步骤，循环进行，直到游戏结束
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        # 判断游戏结束的条件：我方血量低于或等于0，或敌方血量低于或等于0，跳出循环
        if my_hp <= 0:
            printHp(my_hp, enemy_hp)
            print("I lost")
            break

        elif enemy_hp <= 0:
            printHp(my_hp, enemy_hp)
            print("I win")
            break

# 封装一下
def printHp(my_hp, enemy_hp):
    print(f"my remaining hp is {my_hp}")
    print(f"enemy remaining hp is {enemy_hp}")


# 相当于程序入口，其他文件调用时候，name为文件的名字，本文件调用时，name为main
if __name__ == "__main__":
    # 敌人的血量和力量随机生成，幅度和我方血量和力量比较接近
    enemy_hp = random.randint(990, 1010)
    enemy_power = random.randint(190, 210)
    # 调用函数
    fight(enemy_hp, enemy_power)
