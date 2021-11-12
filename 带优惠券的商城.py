shop = [
    ["牙膏",21.5],
    ["lenovo",4500],
    ["Mac pro",12000],
    ["Iphone 18 max Pro",56000],
    ["海尔洗衣机",2500],
    ["辣条",3],
    ["洗衣粉",25],
    ["利群",160],
    ["红塔山",130]
]

import random
A = random.randint(1,3)

if A == 1:
    print('辣条3折优惠卷')
    shop[5][1] = 3 * 0.3
else:
    print('机械革命9折优惠券')
    shop[1][1] = 4500 * 0.9
mycart = []# 空的购物车

# 初始化余额
salary = input("请输入您的余额：")
sal = salary = int(salary)

#买东西
while True:
    for key,value in enumerate(shop):
        print(key,value)
    chose = input("请输入您要的商品编号：")

    if chose.isdigit():
        chose = int(chose)
    # 判断是否存在
        if chose >= len(shop):
            print("温馨提示：这个商品不存在。")
        else:
            if salary >= shop[chose][1]:
                mycart.append(shop[chose])
                salary = salary - shop[chose][1]
                print("恭喜您，添加成功！您的余额还剩:￥", salary)
            else:
                print("没钱，别瞎买！")


    elif chose == 'Q' or chose == 'q':
        print("----------------欢迎下次光临小侯的小商店--------------")
        print("以下是您的购物清单，请拿好：")
        print("--------------------------------------------------")
        for key, value in enumerate(mycart):
                print(key, value)
        print("-------------------------------------------------")
        print("您本次还剩余额为：￥", salary, "，本次消费：￥", (sal - salary))
        break
    else:
        print("？？？,商品不存在，重新选")
for index,value in mycart:
    print(index,value)