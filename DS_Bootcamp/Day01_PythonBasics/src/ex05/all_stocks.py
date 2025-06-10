import sys

def search():
    # Dictionaries for companies and their ticker symbols
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

    # Check if the correct number of arguments is provided (exactly one argument is allowed)
    if len(sys.argv) != 2:
        return  # Do nothing if there's not exactly one argument

    # Extract the expression from the argument and split by commas
    expressions = sys.argv[1].strip()

    # If the string contains two commas in a row (empty expression), do nothing
    parts = [part.strip() for part in expressions.split(',')]

    # If there are any empty parts after the split, it means there were two commas in a row
    if '' in parts:
        return
        # Normalize the input to handle whitespace and case insensitivity
    expressions = [expr.strip().lower() for expr in expressions.split(',')]

    # Iterate over each expression and check if it's a valid company name or ticker symbol
    for expr in expressions:
        found = False
        # Check if it's a company name
        for company, ticker in COMPANIES.items():
            if expr == company.lower():
                print(f"{company} stock price is {STOCKS[ticker]}")
                found = True
                break
            # Check if it's a ticker symbol
            elif expr == ticker.lower():
                print(f"{ticker} is a ticker symbol for {company}")
                found = True
                break
        if not found:
            print(f"{expr} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    search()
