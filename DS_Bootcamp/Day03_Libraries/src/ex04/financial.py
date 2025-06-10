# financial.py
import sys
import time
import yfinance as yf
"""
python3 -m cProfile -o profiling-sleep.prof financial.py MSFT "Total Revenue"
python3 -m cProfile -o profiling-tottime.prof financial.py MSFT "Total Revenue"


"""
def get_financial_data(ticker_symbol, field_name):
    # time.sleep(5)  # This will be removed later
    ticker = yf.Ticker(ticker_symbol.upper())
    financials = ticker.financials

    if financials.empty:
        raise Exception("No financial data found.")

    matched_field = None
    for row in financials.index:
        if field_name.lower().replace(" ", "") in row.lower().replace(" ", ""):
            matched_field = row
            break

    if not matched_field:
        raise Exception(f"Field '{field_name}' not found.")

    row_data = financials.loc[matched_field]
    values = [f"{int(val):,}" for val in row_data.values if not (val != val)]
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
