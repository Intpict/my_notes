#-*- coding:utf-8 -*-
import time
from splinter.exceptions import ElementDoesNotExist
from splinter.browser import Browser

# 初始化相关变量为全局
sale_min = buy_max = 10000
sale_min_2 = buy_max_2 = 10000
is_first = True
buy_price = sale_price = 0
sale_market_str = buy_market_str = ""
count = 0.678
total_sale_num = 0
foot_len = 0.01
max_diff_num = 7
max_error = 7

# 登录页
def login(z_b):
    z_b.visit("https://vip.zb.com/user/login")
    z_b.fill("nike", "18521410636")
    z_b.fill("password", "Zby0265188374ls")
    try:
        z_b.find_by_id("submitBtn").click()
    except ElementDoesNotExist as e:
        print("登录失败！")
        exit(1)
    else:
        time.sleep(3)
        print("账户登录成功！")
        cookies = z_b.cookies.all()
        z_b.cookies.add(cookies)
    return z_b

# 查看账户资产
def get_account(z_b):
    try:
        z_b.visit("https://vip.zb.com/u/asset")
        ans = z_b.find_by_id("totalSpotAsset")
        print(ans[0].value)
    except ElementDoesNotExist as e:
        print("cookie失效，重新登录!")
        login(z_b)

# 进入****usdt交易页面
def go_in_ubtcusdt(z_b):
    try:
        z_b.visit("https://trans.zb.com/lbtcusdt")
        time.sleep(2)
    except:
        print("页面错误，重新登录")
        login(z_b)
        go_in_ltcusdt(z_b)

# 获取当前卖出最低价和买入最高价
def get_sail_min(z_b):
    # 全局变量
    global sale_min, buy_max, sale_market_str, buy_market_str, sale_min_2, buy_max_2
    # sale逻辑
    sale_market = z_b.find_by_id("sellMarket")
    sale_market_str = sale_market[0].value
    sale_list = sale_market_str.split(' ')
    sale_min = sale_list[9]
    sale_min_2 = sale_list[7]
    # buy逻辑
    buy_market = z_b.find_by_id("buyMarket")
    buy_market_str = buy_market[0].value
    buy_list = buy_market_str.split(' ')
    buy_max = buy_list[1]
    buy_max_2 = buy_list[3]

def buy_oper(z_b):
    global buy_price, count
    z_b.fill("buyUnitPrice", str(buy_price))
    z_b.fill("buyNumber", str(count))
    z_b.find_by_id("buyBtn").click()
    
    
def sale_oper(z_b):
    global sale_price, count
    z_b.fill("sellUnitPrice", str(sale_price))
    z_b.fill("sellNumber", 10)
    z_b.find_by_id("sellBtn").click()

def batch_cancel(z_b):
    z_b.find_by_id("batchCancel").click()
    z_b.find_by_text(u"确定").click()
    time.sleep(1)

def is_no_cord(z_b):
    cord_list = z_b.find_by_text(u"暂时没有相关记录。")
    if len(cord_list) == 1:
        return False
    return True


'''
当前脚本主逻辑
'''
if __name__ == "__main__":
    # 打开浏览器
    z_b = Browser(driver_name="chrome")
    # 账号登录
    login(z_b)
    # 转到交易页面
    go_in_ubtcusdt(z_b)
    # 标志位
    in_buy = in_sale = False
    
    # 启动任务
    while True:
        time.sleep(1.5)
        try:
            # 获取当前买入和卖出最高及最低价
            get_sail_min(z_b)
            sleep(0.2)
            diff = 0.00 + float(sale_min) - float(buy_max)
            if diff < max_diff_num:
                continue

            # 第一次逻辑，直接购买
            if is_first:
                batch_cancel(z_b)
                buy_price = float(buy_max)
                buy_price = 0.01 + buy_price
                buy_oper(z_b)
                is_first = False
                in_buy = True
                continue

            time.sleep(4.5)
            no_cord_status = is_no_cord(z_b)
            # 有购买或者卖出的相关记录
            if not no_cord_status:
                buy_max_num = 0.00 + float(buy_max)
                sale_min_num = 0.00 + float(sale_min)
                # 处在购买状态并且价格不是定价最高
                if in_buy and buy_price < buy_max_num:
                    if buy_max_num - buy_price > max_error:
                        continue
                    batch_cancel(z_b)
                    buy_price = buy_max_num
                    buy_oper(z_b)
                # 处在卖出状态并且价格不是定价最低
                if in_sale and sale_price > sale_min_num:
                    if sale_price - sale_min_num > max_error:
                        continue
                    batch_cancel(z_b)
                    sale_price = sale_min_num
                    sale_oper(z_b)
            # 无相关记录，代表已经买入或者卖出
            if no_cord_status:
                # 上一条记录是购买
                if in_buy:
                    sale_price = float(sale_min)
                    sale_price = 0.00 + sale_price - foot_len
                    sale_oper(z_b)
                    in_buy = False
                    in_sale = True
                    print("已买入，价格:", str(buy_price))
                # 上一条记录为卖出
                else:
                    print("已卖出，价格:", str(sale_price))
                    total_sale_num += 0.00 + count * (sale_price - buy_price)
                    print(total_sale_num)
                    if total_sale_num < -1.0:
                        break
                    buy_price = float(buy_max)
                    buy_price = 0.01 + buy_price
                    buy_oper(z_b)
                    in_buy = True
                    in_sale = False 

        except ElementDoesNotExist as e:
            print("异常发生退出！")
            break

    # 正常退出
    exit(0)
        

