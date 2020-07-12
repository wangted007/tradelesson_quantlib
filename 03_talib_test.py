import talib
import tushare as ts
import pandas as pd
from matplotlib import pyplot as plt
#文档地址
#https://mrjbq7.github.io/ta-lib/
#github 文档中文翻译地址
#https://github.com/HuaRongSAO/talib-document
#函数列表
#http://www.tadoc.org/


ts.set_token("ca9a880eb55cf5479fe8b021615f26d1a59c6f187e9d008a817c4ae0")

#准备K线数据
api = ts.pro_api()
data_table = api.daily(ts_code='000001.SZ', start_date='2020-01-01')
data_table = data_table.sort_values('trade_date',ascending=True)
data_table.index = pd.to_datetime(data_table.trade_date)


def talib_describe():
    print(talib.get_functions())
    # print(talib.get_function_groups())
    ta_fun = talib.get_function_groups()
    print(ta_fun)
    print(ta_fun.keys())


def Overlap_test():
    data_table["MA5"] = talib.MA(data_table.close, timeperiod=5)
    print(data_table["MA5"])
    data_table["EMA"] = talib.EMA(data_table.close)
    print(data_table["EMA"])
    #考夫曼的自适应移动平均线
    data_table["KAMA"] = talib.KAMA(data_table.close, timeperiod=30)
    print(data_table["KAMA"])
    #布林通道
    data_table["BBANDS_upper"], data_table["BBANDS_middle"], data_table["BBANDS_lower"] = talib.BBANDS(
        data_table.close, matype= talib.MA_Type.T3)


    # plt.figure(1)
    # plt.plot(data_table.index,data_table.close,label = 'close')
    # plt.plot(data_table.index,data_table["MA5"],label = 'MA5')
    # plt.plot(data_table.index,data_table["MA5"],label = 'MA5')
    # plt.legend(loc='upper middle')
    # plt.show()


#波动率
def Volatility_test():
    #真实波动幅度
    data_table["TRANGE"] = talib.TRANGE(data_table.high, data_table.low, data_table.close)
    #真实波动幅度均值
    data_table["ATR"] = talib.ATR(data_table.high, data_table.low, data_table.close, timeperiod=14)
    print(data_table["ATR"])

def Momentum_test():
    #顺势指标
    data_table["CCI"] = talib.CCI(data_table.high, data_table.low, data_table.close, timeperiod=14)
    #平滑异同移动平均线
    data_table["MACD"],data_table["SIGNAL"],data_table["HIST"] = talib.MACD(data_table.close, fastperiod=12, slowperiod=26, signalperiod=9)
    #相对强弱指数
    data_table["RSI"] = talib.RSI(data_table.close, timeperiod=14)

#统计指标与其他
def Other_test():
    data_table["AVGPRICE"] = talib.AVGPRICE(data_table.open,data_table.high,data_table.low,data_table.close)
    print("AVGPRICE", data_table["AVGPRICE"])
    data_table["MEDPRICE"] = talib.MEDPRICE(data_table.high,data_table.low)
    print("MEDPRICE", data_table["MEDPRICE"])
    data_table["BETA"] = talib.BETA(data_table.high, data_table.low, timeperiod=4)
    print("BETA", data_table["BETA"])
    data_table["VAR"] = talib.VAR(data_table.close, timeperiod=5, nbdev=1)
    print("VAR", data_table["VAR"])


def main():
    #talib_describe()
    #Overlap_test()
    #Volatility_test()
    Momentum_test()
    Other_test()

if __name__ == '__main__':
    main()