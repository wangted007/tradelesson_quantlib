import talib
import tushare as ts
import pandas as pd

#文档地址
#https://mrjbq7.github.io/ta-lib/
#github 文档中文翻译地址
#https://github.com/HuaRongSAO/talib-document

ts.set_token("ca9a880eb55cf5479fe8b021615f26d1a59c6f187e9d008a817c4ae0")

#准备K线数据
api = ts.pro_api()
klines = api.daily(ts_code='000001.SZ', start_date='2020-01-01')
klines = klines.sort_values('trade_date',ascending=True)
klines.index = pd.to_datetime(klines.trade_date)

def talib_describe():
    # print(talib.get_functions())
    # print(talib.get_function_groups())
    ta_fun = talib.get_function_groups()
    print(ta_fun)
    print(ta_fun.keys())


def Overlap_test():
    ma5 = talib.MA(klines.close, timeperiod=5)
    print(ma5)
    sma = talib.SMA(klines.close)
    print(sma)
    kama = talib.KAMA(klines.close, timeperiod=30)
    print(kama)



def Volatility_test():
    atr = talib.ATR(klines.high, klines.low, klines.close, timeperiod=14)
    print(atr)
    #归一化波动幅度均值
    nart = talib.NATR(klines.high, klines.low, klines.close, timeperiod=14)
    print(atr)

def Momentum_test():
    cci = talib.CCI(klines.high, klines.low, klines.close, timeperiod=14)

    macd, macdsignal, macdhist = talib.MACD(klines.close, fastperiod=12, slowperiod=26, signalperiod=9)

    rsi = talib.RSI(klines.close, timeperiod=14)

def Other_test():
    avg = talib.AVGPRICE(klines.close)
    print(avg)
    med = talib.MEDPIRCE(klines.close)
    print(med)
    beta = talib.BETA(klines.high, klines.low, timeperiod=4)

    var = talib.VAR(klines.close, timeperiod=5, nbdev=1)


def main():
    #talib_describe()
    #Overlap_test()
    Volatility_test()

if __name__ == '__main__':
    main()