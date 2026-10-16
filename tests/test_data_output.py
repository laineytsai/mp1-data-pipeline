import pandas as pd
from src import save_data

def test_save_data_creates_csv(sample_df, tmp_path):
    output_path = tmp_path / "clean.csv"

    output = save_data(sample_df, output_path)

    assert output == output_path
    df = pd.read_csv(output)
    assert len(df) == len(sample_df)
    assert df.columns.tolist() == sample_df.columns.tolist()