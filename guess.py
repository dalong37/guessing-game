import random

#生成1到10之间的随机数
number = random.randint(1,10)

while True:
  try:
    #提示用户输入猜测的数字
    guess = int(input("请猜测一个1到10之间的数字："))
    
    #检查用户的猜测是否在有效范围内
    if 1 <= guess <= 10:
      #检查猜测是否正确
      if guess == number:
        print("恭喜你，猜对了！游戏结束。")
        break
      else:
        print("猜错了，再试一次。")
    else:
      print("你输入的数字不在1到10的范围内，请重新输入。")
  except ValueError:
    print("输入无效，请输入一个有效的整数。")
