import pandas as pd
import os

def load_data(file_name):
    """
    Loads a CSV file from the project's internal data directory.

    This function constructs an absolute path to a file located within 
    a '/data' folder relative to the script's location, ensuring 
    cross-platform compatibility.

    Args:
        file_name (str): The name of the CSV file to load (e.g., 'users.csv').

    Returns:
        pd.DataFrame: A pandas DataFrame containing the loaded data.

    Raises:
        FileNotFoundError: If the file does not exist in the expected directory.
    """
    # Adjust path to look into the data folder
    path = os.path.join(os.path.dirname(__file__), 'data', file_name)
    return pd.read_csv(path)

def get_total_sales():
    df = load_data('sales_data.csv')
    # Adding .item() converts the NumPy value to a standard Python int
    return df['sales'].sum().item()

if __name__ == "__main__":
    print(f"Total Sales: {get_total_sales()}")













    