import pandas as pd
import os

def load_data(file_name):
    # Adjust path to look into the data folder
    path = os.path.join(os.path.dirname(__file__), 'data', file_name)
    return pd.read_csv(path)

def get_total_sales():
    df = load_data('sales_data.csv')
    # Adding .item() converts the NumPy value to a standard Python int
    return df['sales'].sum().item()

if __name__ == "__main__":
    print(f"Total Sales: {get_total_sales()}")