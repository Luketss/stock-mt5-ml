from datetime import datetime
import MetaTrader5 as mt5
import pytz
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters

from error import OrderNotFulfilledError, LoginError
from setup import user, password, investidor


class Metatrader:
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        quit()

    def __init__(self, stock_code):
        self.symbol = stock_code

    def send_order(self):
        pass

    def get_account_info(self):
        authorized = mt5.login(user, password=password)
        if authorized:
            account_info = mt5.account_info()
            if account_info != None:
                print(account_info)
                print("Show account_info()._asdict():")
                account_info_dict = mt5.account_info()._asdict()
                for prop in account_info_dict:
                    print("  {}={}".format(prop, account_info_dict[prop]))
        else:
            raise LoginError(user, mt5.last_error())


# prepare the buy request structure
# symbol = "EURUSD"
# symbol_info = mt5.symbol_info(symbol)
# if symbol_info is None:
#     print(symbol, "not found, can not call order_check()")
#     mt5.shutdown()
#     quit()

# if the symbol is unavailable in MarketWatch, add it
# if not symbol_info.visible:
#     print(symbol, "is not visible, trying to switch on")
#     if not mt5.symbol_select(symbol, True):
#         print("symbol_select({}}) failed, exit", symbol)
#         mt5.shutdown()
#         quit()

# lot = 0.1
# point = mt5.symbol_info(symbol).point
# price = mt5.symbol_info_tick(symbol).ask
# deviation = 20
# request = {
#     "action": mt5.TRADE_ACTION_DEAL,
#     "symbol": symbol,
#     "volume": lot,
#     "type": mt5.ORDER_TYPE_BUY,
#     "price": price,
#     "sl": price - 100 * point,
#     "tp": price + 100 * point,
#     "deviation": deviation,
#     "magic": 234000,
#     "comment": "python script open",
#     "type_time": mt5.ORDER_TIME_GTC,
#     "type_filling": mt5.ORDER_FILLING_RETURN,
# }

# # send a trading request
# result = mt5.order_send(request)
# # check the execution result
# print(
#     "1. order_send(): by {} {} lots at {} with deviation={} points".format(
#         symbol, lot, price, deviation
#     )
# )
# if result.retcode != mt5.TRADE_RETCODE_DONE:
#     print("2. order_send failed, retcode={}".format(result.retcode))
#     # request the result as a dictionary and display it element by element
#     result_dict = result._asdict()
#     for field in result_dict.keys():
#         print("   {}={}".format(field, result_dict[field]))
#         # if this is a trading request structure, display it element by element as well
#         if field == "request":
#             traderequest_dict = result_dict[field]._asdict()
#             for tradereq_filed in traderequest_dict:
#                 print(
#                     "       traderequest: {}={}".format(
#                         tradereq_filed, traderequest_dict[tradereq_filed]
#                     )
#                 )
#     print("shutdown() and quit")
#     mt5.shutdown()
#     raise OrderNotFulfilledError("TRADE_ACTION_DEAL", symbol, price, "ORDER_TYPE_BUY")

if __name__ == "__main__":
    mt = Metatrader(stock_code="EURUSD")
    mt.get_account_info()
