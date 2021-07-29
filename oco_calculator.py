# Author: Reganto
# Blog: reganto.net
# Calculate OCO parameters for trade in binance

def buy_price():
    """ get buy price """
    price_of_buy_order = float(input('Buy Price:'))
    return price_of_buy_order


def take_benefit():
    """ get take_benefit """
    percentage_of_benefit = float(input('Take Benefit(%):'))
    return percentage_of_benefit

def stop_loss():
    """ get stop loss """
    percent_of_loss = float(input('Stop Loss(%):'))
    return percent_of_loss

def calculate_price(buy_prc, take_bnft):
    """ calculate oco price """
    return (buy_prc * (take_bnft / 100)) + buy_prc

def calculate_stop(buy_prc, stop_ls):
    """ calculate oco stop(sell trigger) """
    t = tuple()
    c_stop = (buy_prc * (stop_ls / 100))
    stop = buy_prc - (buy_prc * (stop_ls / 100))
    t += (stop, c_stop)
    return t

def calculate_limit(buy_prc, c_stop):
    """ calculate oco limit """
    return buy_prc - ((0.5 / 100) * c_stop + c_stop)

def make_app():
    buy_prc = buy_price()
    take_bnft = take_benefit()
    stop_ls = stop_loss()

    price = calculate_price(buy_prc, take_bnft)
    stop, c_stop = calculate_stop(buy_prc, stop_ls)
    limit = calculate_limit(buy_prc, c_stop)

    print("Price:{}, Stop:{}, Limit:{}".format(price, stop, limit))

if __name__ == "__main__":
    make_app()

