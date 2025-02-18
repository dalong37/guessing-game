import random

#生成1到10之间的随机数
number = random.randint(1,10)
#初始化猜测次数
count = 0
#最多猜测次数
max = 5

while count < max:
  try:
    #提示用户输入猜测的数字
    guess = int(input("请猜测一个1到10之间的数字："))
    count = count + 1
    
    #检查用户的猜测是否在有效范围内
    if 1 <= guess <= 10:
      #检查猜测是否正确
      if guess == number:
        print("恭喜你，猜对了！你总共用了{count}次猜测。游戏结束。")
        break
      else:
        remain = max - count
        if remain > 0:
          print("猜错了，你还剩{remain}次机会。再试一次。")
        else:
          print("很遗憾，你已经用完了{max}次机会，正确答案是{number}。游戏结束。")
    else:
      print("你输入的数字不在1到10的范围内，请重新输入。")
      #无效输入时，本次猜测不消耗次数，所以减一
      count = count - 1
  except ValueError:
    print("输入无效，请输入一个有效的整数。")
    #无效输入时，本次猜测不消耗次数，所以减一
    count = count - 1
