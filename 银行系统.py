import random


# 银行的数据库
bank = {}
# 银行名称
bank_name = "中国工商银行昌平支行"

# 首页面
def welcome():
    print("--------------------------------------")
    print("-      中国工商银行账户管理系统V1.0       -")
    print("--------------------------------------")
    print("-  1.开户                             -")
    print("-  2.存钱                             -")
    print("-  3.取钱                             -")
    print("-  4.转账                             -")
    print("-  5.查询                             -")
    print("-  6.Bye!                            -")
    print("--------------------------------------")

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door,money):
    if len(bank) > 100:
        return 3

    if username in bank:
        return 2

    # 正常开户
    bank[username] = {
        "account":account,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":bank_name
    }
    return 1

# 开户的输入数据
def addUser():
    username = input("请输入姓名：")

    password = input("请输入密码：")

    country = input("请输入国籍：")

    province = input("请输入省份：")

    street = input("请输入街道：")

    door  = input("请输入您家门牌号：")

    money = int(input("请输入初始化您的银行卡余额："))

    account = random.randint(10000000,99999999)

    status = bank_addUser(account,username,password,country,province,street,door,money)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%s
            密码：%s
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (username,account,password,country,province,street,door,money,bank_name))
        print(bank)

# 存钱
def bank_cun():
    username = input('请输入账户用户名')
    addmoney = int(input('请输入存款金额'))
    addcun = cun_money(username,addmoney)
    if addcun  == 1:
        print("嘻嘻，存款成功")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            余额：%s
            存入金额：%s
            ---------------------------------------
        '''
        print(info % (username,bank[username]["money"],addmoney))
        print(bank)

def cun_money(username,addmoney):
    if username in bank:
        bank[username]["money"] =  bank[username]["money"] + addmoney
        return 1
    else:
        return 2

# 取钱
def bank_qumoney():
    username = input("请输入用户名:")
    password = input('请输入密码：')
    addmoney = int(input("请输入取款金额:"))
    add = add_money(username, addmoney,password)
    if add == 3:
        print("对不起，钱不够")
    elif add == 2:
        print("密码不对")
    elif add == 1:
        print('账户不存在')
    elif add == 0:
        print("取钱成功")
        print("下面是您的账户信息:")
        info = '''
            --------------账户信息--------------
            用户名：%s
            取出金额: %s 元
            账户余额: %s 元
            ----------------------------------
            '''
        print(info % (username, addmoney, bank[username]['money']))

def add_money(username,addmoney,password):
    if username in bank :
        bank[username]['password'] = password
        bank[username]['money'] =  bank[username]['money'] - addmoney
        if bank[username]['money'] >= 0:
            return 1
        else :
            return 3

# 转账




# 查询
def bank_cha(account,password,username):
    if account in bank and password in bank:
        bank[username]['account'] = account
        bank[username]['password'] = password
        return 1

def bank_chaxun():
    username = input('请输入用户名：')
    account = input('请输入账号：')
    password = input('请输入密码：')
    addcha = bank_cha(
        account,
        password,
        username,
        )
    if addcha == 1:
        print("恭喜你，查询成功喽。")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%s
            密码：%s
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (
        account,
        password,
        username,
        bank[username]['country'],
        bank[username]['province'],
        bank[username]['street'],
        bank[username]['door'],
        bank[username]['money'],
        bank[username]['bank_name']
        ))
        print(bank)
# 结束
    if chose == 6:
        print("byebye，欢迎下次使用！")

while True:
    welcome()
    chose = input("请输入业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        bank_cun()
    elif chose == "3":
        bank_qumoney()
    elif chose == "4":
        pass
    elif chose == "5":
        bank_chaxun()
    elif chose == "6":
        print('---------------------')
        print('bye bye,欢迎下次使用哦￥')
        print('---------------------')
        break



































































