import tushare as ts
#文档地址https://www.waditu.com

ts.set_token("ca9a880eb55cf5479fe8b021615f26d1a59c6f187e9d008a817c4ae0")

def history_quote():
    api = ts.pro_api()
    #股票基本信息
    # stocks = api.stock_basic(exchange = 'SZSE',list_status = "L", fields = "ts_code,symbol,name,area,industry,list_date",)
    # print(stocks)

    # new_stocks = api.new_share(start_date = '20200101')
    # print(new_stocks)
    #通用行情获取方法
    # klines = ts.pro_bar(ts_code = '000001.SZ',freq = '1min',adj = 'qfq',start_date = '20200101',end_date = '20200115')
    # print(klines)

    # 日行情
    # klines = api.daily(ts_code='000001.SZ', start_date='2020-01-01')
    # print(klines)

    #财务数据
    finance_index = api.fina_indicator(ts_code='600000.SH')
    print(finance_index)


    #指数数据获取
    # index_basic = api.index_basic(market = 'SW')
    # print(index_basic)

    #可转债数据获取
    # 获取可转债基础信息列表
    bond_change_list = api.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date")
    print(bond_change_list)

def main():
    history_quote()

if __name__ == '__main__':
    main()