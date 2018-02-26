#-*- coding:utf-8 -*-
import time
from splinter.exceptions import ElementDoesNotExist
from splinter.browser import Browser

# 初始化相关变量为全局
sale_min = buy_max = 10000
sale_min_2 = buy_max_2 = 10000
is_first = True
buy_price = sale_price = 10000
sale_market_str = buy_market_str = ""
count = 100
# 控制买入价格阈值，低于此值会自动购买
buy_price_threshold = 49.5

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

# 进入***usdt交易页面
def go_in_usdt(z_b):
    try:
        z_b.visit("https://trans.zb.com/qtumusdt")
        time.sleep(2)
    except:
        print("页面错误，重新登录")
        login(z_b)
        go_in_ltcusdt(z_b)

# 获取当前卖出最低价和买入最高价
def get_current_price(z_b):
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
    print("已生成购买订单，购买价格为:", str(buy_price))

def sale_oper(z_b):
    global sale_price, count
    z_b.fill("sellUnitPrice", str(sale_price))
    z_b.fill("sellNumber", str(count))
    z_b.find_by_id("sellBtn").click()

def batch_cancel(z_b):
    global buy_price
    z_b.find_by_id("batchCancel").click()
    z_b.find_by_text(u"确定").click()
    time.sleep(1)
    print("已撤销购买订单，购买价格为:", str(buy_price))

'''
判断当前账号是否已存在买入和卖出单号
'''
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
    go_in_usdt(z_b)
     # 启动任务
    while True:
        time.sleep(1.5)
        try:
            # 获取当前买入和卖出最高及最低价
            get_current_price(z_b)
            buy_max_num = 0.00 + float(buy_max)
            print("当前买入价格: ", str(buy_max_num))

            # 延时并获取当前购买状态
            time.sleep(4)
            no_cord_status = is_no_cord(z_b)

            # 主流程
            # 符合购买条件
            if buy_max_num < float(buy_price_threshold):
                # 如果存在购买记录
                if not no_cord_status:
                    # 如果当前订单购买价格小于buy_max
                    if buy_price < buy_max_num:
                        batch_cancel(z_b)
                        buy_price = buy_max_num
                        buy_oper(z_b)
                else:
                    buy_price = 0.01 + buy_max_num
                    buy_oper(z_b)
            else:
                # 如果不符合要求，且有购买订单，则撤销该订单
                if not no_cord_status:
                    batch_cancel(z_b)


        except ElementDoesNotExist as e:
            print("异常发生退出！")
            break

    # 正常退出
    exit(0)