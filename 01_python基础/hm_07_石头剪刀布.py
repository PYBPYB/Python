# 倒入 随机 工具包
import random

# 从控制台输出您要出的拳 - 石头（1）/剪刀（2）/布（3）
player = int(input("请输出您要出的拳 - 石头（1）/剪刀（2）/布（3）:"))

# 电脑随机出拳 - 先假定电脑只会出石头，完成整体代码功能
computer = random.randint(1,3)

print("玩家: %d  电脑: %d" % (player, computer))
# 比较胜负
if ((player == 1 and computer == 2)
        or(player == 2 and computer == 3)
        or(player == 3 and computer == 1)):

    print("恭喜，玩家胜利了！")
# elif (player==1 and computer==1)or(player==2 and computer==2)or(player==3 and computer==3):
elif player == computer:
    print("平局！")
else:
    print("电脑赢了!")
