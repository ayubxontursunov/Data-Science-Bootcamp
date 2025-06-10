import sys
def search():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    istrue = True
    if len(sys.argv) == 2:
        value1 = sys.argv[1].upper()
        for key,value in COMPANIES.items():
            if value1 == value:
                print(f"{key} {STOCKS[value1]}")
                istrue = False

        if istrue:
            print("Unknown ticker")


if __name__ == '__main__':
    search()