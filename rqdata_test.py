import rqdatac

rqdatac.init(username = '15810715022',password = '123456')
def main():
    instrument_list = rqdatac.all_instruments(type = 'stock', market = 'cn')
    print(instrument_list)
if __name__ == "__main__":
    main()