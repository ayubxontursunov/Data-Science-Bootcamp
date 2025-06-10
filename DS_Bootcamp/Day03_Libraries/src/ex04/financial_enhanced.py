import sys
import yfinance as yf
import time


def get_financial_data(ticker_symbol, field_name):
    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol.upper())

    # Get the financial data (this is where Yahoo Finance is accessed)
    financials = ticker.financials

    if financials.empty:
        raise Exception("No financial data found.")

    # Normalize the field name to match the available index
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
        print("Usage: ./financial_enhanced.py TICKER 'Field Name'")
        sys.exit(1)

    ticker = sys.argv[1]
    field = sys.argv[2]

    try:
        result = get_financial_data(ticker, field)
        print(result)
    except Exception as e:
        print("Error fetching data:", e)
