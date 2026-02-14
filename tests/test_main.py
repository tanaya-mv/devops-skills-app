import pytest
from src.main import get_total_sales, load_data
import numpy as np 


def test_sales_calculation():
    total = get_total_sales()
    assert total > 0
    # Update this line to include np.integer and np.floating
    assert isinstance(total, (int, float, np.integer, np.floating))

def test_stock_data_columns():
    # Verify the stock data has the expected quantity column
    df = load_data('stock_data.csv')
    assert 'quantity_in_stock' in df.columns
    assert not df.empty