import tushare as ts

#ts.set_token("ca9a880eb55cf5479fe8b021615f26d1a59c6f187e9d008a817c4ae0")
def history_quote():
    api =  ts.pro_api("ca9a880eb55cf5479fe8b021615f26d1a59c6f187e9d008a817c4ae0")
    klines = api.daily(ts_code='000001.SZ', start_date='2019-01-01')
    print(klines)

def main():
    history_quote()

if __name__ == '__main__':
    main()