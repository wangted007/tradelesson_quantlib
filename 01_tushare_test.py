import tushare as ts
import pandas as pd
import datetime as dt
#文档地址https://www.waditu.com

ts.set_token("ca9a880eb55cf5479fe8b021615f26d1a59c6f187e9d008a817c4ae0")

def stock_quote():
    api = ts.pro_api()
    # #股票基本信息
    # stocks = api.stock_basic(exchange = 'SZSE',list_status = "L", fields = "ts_code,symbol,name,area,industry,list_date",)
    # print(stocks)
    #
    # #新股
    # new_stocks = api.new_share(start_date = '20200101')
    # print(new_stocks)
    #
    # #通用行情获取方法
    # klines = ts.pro_bar(ts_code = '000001.SZ',freq = '1min',adj = 'qfq',start_date = '20200101',end_date = '20200115')
    # print(klines)
    #
    # # 日行情
    # klines = api.daily(ts_code='000001.SZ', start_date='2020-01-01')
    # print(klines)
    #
    # #财务数据
    # finance_index = api.fina_indicator(ts_code='000001.SZ')
    # print(finance_index)


    #指数数据获取
    #获取指数样本
    #index_basic = api.index_basic(market = 'SW')
    #print(index_basic)

    index_kline = api.index_daily(ts_code='399300.SZ',fields = 'trade_date,close')
    print(index_kline)
def change_bond():
    #可转债数据获取
    api = ts.pro_api()
    # 获取可转债基础信息列表
    basic_info = api.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,maturity_date,delist_date,issue_size,conv_price")
    print(basic_info)
    #筛选掉已经到期的债券
    basic_info = basic_info[basic_info['maturity_date'] > '2020-07-01']
    basic_filename = "data/bond_basic_" + dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".xlsx"
    basic_info.to_excel(basic_filename)

    #可转债行情
    quote_info = api.cb_daily(trade_date = '20200710')
    print(quote_info)
    quote_filename = "data/bond_quote_" + dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".xlsx"
    quote_info.to_excel(quote_filename)

    bond_merge_info = pd.merge(basic_info,quote_info,on = 'ts_code')
    print(bond_merge_info)
    bond_mergeinfo_filename = "data/all_info" + dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".xlsx"
    bond_merge_info.to_excel(bond_mergeinfo_filename)

def main():
    stock_quote()
    #change_bond()

if __name__ == '__main__':
    main()