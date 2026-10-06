import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data" / "processed"

def load_real_estate_data() -> pd.DataFrame:
    """
    Load the cleaned real estate dataset.
    """
    file_path = DATA_DIR / "thailand_homes_dashboard.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found at {file_path}")
    
    df = pd.read_csv(file_path)
    
    # Optional: Fill NaNs in text columns to prevent errors in filters
    df['Province'] = df['Province'].fillna('Unknown')
    df['District'] = df['District'].fillna('Unknown')
    df['Subdistrict'] = df['Subdistrict'].fillna('Unknown')
    
    return df
