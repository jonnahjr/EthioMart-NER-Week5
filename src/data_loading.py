import pandas as pd
  
def load_dataset(file_path):
    """
    Load dataset from a CSV file.
    Args:
    - file_path: str, path to the CSV file.
 
    Returns: 
    - df: DataFrame, loaded dataset.
    """
    return pd.read_csv(file_path)
