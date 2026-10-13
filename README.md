# MP1 Data Pipeline
This project is a command-line pipeline that takes an input file and loads, validates, cleans, and saves the data using settings
from a YAML configuration file. The main file, `pipeline.py`, loads the input data based on its file type, validates it, applies the
cleaning steps specified in the configuration file, and saves the cleaned data as a CSV. It also handles errors and prints a cleaning
report at the end. In the `src/` folder that contains reusable code, `data_loaders.py` reads CSV, JSON, and YAML files, `data_validator.py`
checks for required columns and removes rows with invalid numeric values, and `data_processor.py` removes duplicate rows, rows or columns
with missing values, and outliers. `data_output.py` saves the cleaned data as a CSV and creates an output folder if it doesn't exist, and
`utils.py` sets up logging and checks that input files exist. Since nothing is hard-coded, the settings in `config/config.yaml` can be 
changed to clean different datasets without editing any code.


## Example Command
```
python3 pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```

## Example Output
```
20:31:53 DEBUG    __main__ — Arguments parsed: input = fixtures/sample_data.csv, config = config/config.yaml, output = output/clean.csv
20:31:53 INFO     src.utils — Input file validated: fixtures/sample_data.csv
20:31:53 INFO     src.utils — Input file validated: config/config.yaml
20:31:53 INFO     src.data_loaders — Loaded CSV file: fixtures/sample_data.csv (100 rows)
20:31:53 INFO     src.data_loaders — Loaded YAML file: config/config.yaml
20:31:53 WARNING  src.data_validator — Invalid numeric value in rating at row 94: not_available
20:31:53 WARNING  src.data_validator — Invalid numeric value in rating at row 95: error
20:31:53 WARNING  src.data_validator — Removed 2 rows with invalid numeric values in rating
20:31:53 DEBUG    src.data_validator — Validation: 100 -> 98 rows
20:31:53 INFO     __main__ — Validation complete: 100 -> 98 rows
20:31:53 DEBUG    src.data_processor — remove_duplicates: 98 -> 96 rows
20:31:53 DEBUG    src.data_processor — handle_missing: 96 -> 94 rows
20:31:53 DEBUG    src.data_processor — method: iqr, threshold: 1.5, rows removed: 2
20:31:53 INFO     __main__ — Processing complete: 98 -> 92 rows
20:31:53 DEBUG    src.data_output — Saved 92 rows to output/clean.csv
20:31:53 INFO     __main__ — Saved cleaned data to output/clean.csv
Cleaning report: 
{'rows_before': 98, 'rows_after': 92, 'rows_removed': 6, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}
```