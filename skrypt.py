import pandas as pd

def wiki_table_to_excel(wiki_table, excel_filename):
    # Splitting data into rows
    rows = wiki_table.strip().split("\n")
    
    # Parsing headers (first row of the table)
    headers = [header.strip() for header in rows[0].strip('|').split('|')]
    
    # Checking and parsing table data
    data = []
    for row in rows[1:]:
        columns = [col.strip() for col in row.strip('|').split('|')]
        # We check if the number of columns matches the headers
        if len(columns) == len(headers):
            data.append(columns)
        else:
            print(f"Error: The row has a different number of columns than the headers: {row}")
    
    # Creating DataFrame from data
    df = pd.DataFrame(data, columns=headers)
    
    # Saving to an Excel file
    df.to_excel(excel_filename, index=False)
    print(f"Saved to the file: {excel_filename}")

# Reading the text file with the table in Wiki format
with open("/Users/user/Desktop/tabelabackup.txt", "r") as file:
    wiki_table = file.read()

# Conversion to Excel
wiki_table_to_excel(wiki_table, '/Users/user/Desktop/tabela_output.xlsx')
