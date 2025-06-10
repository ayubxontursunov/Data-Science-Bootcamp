import sys
import time
import yfinance as yf

"""
No scraping of fragile HTML

Uses Yahoo Finance's real data endpoints

Handles crumbs, tokens, cookies internally

Works for all major tickers (MSFT, AAPL, AMZN, etc.)


python3 financial.py MSalFT "Total Revenue"

"""

def get_financial_data(ticker_symbol, field_name):
    time.sleep(5)

    ticker = yf.Ticker(ticker_symbol.upper())
    financials = ticker.financials  # This returns a DataFrame

    if financials.empty:
        raise Exception("No financial data found.")

    # Normalize the field name to match available index
    matched_field = None
    for row in financials.index:
        if field_name.lower().replace(" ", "") in row.lower().replace(" ", ""):
            matched_field = row
            break

    if not matched_field:
        raise Exception(f"Field '{field_name}' not found.")

    row_data = financials.loc[matched_field]
    values = [f"{int(val):,}" for val in row_data.values if not (val != val)]  # remove NaNs

    return tuple([matched_field] + values)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./financial.py TICKER 'Field Name'")
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]

    try:
        result = get_financial_data(ticker, field)
        print(result)
    except Exception as e:
        print("Error:", e)
