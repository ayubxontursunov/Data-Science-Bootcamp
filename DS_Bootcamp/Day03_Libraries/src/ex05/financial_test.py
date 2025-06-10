import pytest
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.insert(0, parent_dir)
"""pytest ex05/financial_test.py
"""

# Now import get_financial_data from ex03.financial
from ex03.financial import get_financial_data

# Test case 1: Check that the function returns correct data for a valid ticker and field
def test_valid_total_revenue():
    # Using AAPL (Apple) and the "Total Revenue" field - adjust as needed if the data changes.
    result = get_financial_data("AAPL", "Total Revenue")
    assert isinstance(result, tuple)  # Result must be a tuple
    assert len(result) > 1            # Must include more than just the field name

# Test case 2: Check that the function returns a tuple
def test_return_type():
    result = get_financial_data("AAPL", "Total Revenue")
    assert isinstance(result, tuple)  # Ensuring the return type is a tuple

# Test case 3: Check that an exception is raised for an invalid ticker
def test_invalid_ticker():
    # The message must exactly match what is raised in get_financial_data.
    with pytest.raises(Exception, match="No financial data found."):
        get_financial_data("INVALIDTICKER", "Total Revenue")

# Test case 4: Check that an exception is raised for an invalid field
def test_invalid_field():
    # Matching the exception message for an invalid field.
    with pytest.raises(Exception, match="Field 'Nonexistent Field' not found."):
        get_financial_data("AAPL", "Nonexistent Field")
