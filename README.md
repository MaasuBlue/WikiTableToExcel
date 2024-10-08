# Wiki Table to Excel Converter

This Python script converts a table in Wiki format from a text file into an Excel file. It reads the table, parses it into rows and columns, checks if the number of columns matches the headers, and exports the data to an Excel file.

## Features

- Reads a Wiki-style table from a plain text file.
- Parses the table into headers and rows.
- Validates if the number of columns in each row matches the headers.
- Exports the table as an Excel file.

## Requirements

- Python 3.x
- `pandas` library
- `openpyxl` library (for writing Excel files)

## Installation

First, make sure you have Python 3 installed. Then, install the required Python libraries:

```bash
pip install pandas openpyxl
```
## Usage

1. Ensure your input text file contains a table in Wiki format, like this:

    ```text
    | Nazwa   | SN      | Profil   | Hasło            | Data       | User                |
    | NR45 | 123456 | Xyz | 21323ffp | 12/01/2021 | Piotr Nowak |
    | NM56  | 123456 | pxyz| 897dhdn | 26/01/2021 | Jan Jankowski      |
    ```

2. Save your Wiki table in a `.txt` file, for example, `tabelabackup.txt`.

3. Run the script with the path to your `.txt` file and the desired output file:

    ```bash
    python3 script.py
    ```

4. The resulting Excel file will be saved to the specified location, for example, `tabela_output.xlsx`.

## Script Example

```python
import pandas as pd

def wiki_table_to_excel(wiki_table, excel_filename):
    # Split the input into rows
    rows = wiki_table.strip().split("\n")
    
    # Parse headers (first row of the table)
    headers = [header.strip() for header in rows[0].strip('|').split('|')]
    
    # Parse the table rows
    data = []
    for row in rows[1:]:
        columns = [col.strip() for col in row.strip('|').split('|')]
        if len(columns) == len(headers):
            data.append(columns)
        else:
            print(f"Error: Row has different column count: {row}")
    
    # Create a DataFrame and save as Excel
    df = pd.DataFrame(data, columns=headers)
    df.to_excel(excel_filename, index=False)
    print(f"Saved to file: {excel_filename}")

# Example usage
with open("tabelabackup.txt", "r") as file:
    wiki_table = file.read()

wiki_table_to_excel(wiki_table, 'tabela_output.xlsx')
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

