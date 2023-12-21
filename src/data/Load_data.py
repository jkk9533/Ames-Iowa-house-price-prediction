import pandas as pd
from pathlib import Path

def load_data():
    """Load data from data/raw/ directory."""
    file_path = Path('..', '..', 'data', 'raw', 'complaints.csv').resolve()
    df = pd.read_csv(file_path, parse_dates=['Date received'])
    return df

def filter_data_for_2021_and_2022(df):
    """Slice data to only include years 2021 and 2022 from Date Received column."""
    df = df[df['Date received'].dt.year.isin([2021, 2022])]
    return df

df = load_data()
filtered_df = filter_data_for_2021_and_2022(df)

output_path = Path('../../data/interim/complaints_2021_2022.csv').resolve()
filtered_df.to_csv(output_path, index=False)
