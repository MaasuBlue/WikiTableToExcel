import pandas as pd

def wiki_table_to_excel(wiki_table, excel_filename):
    # Rozdzielenie danych na wiersze
    rows = wiki_table.strip().split("\n")
    
    # Parsowanie nagłówków (pierwszy wiersz z tabeli)
    headers = [header.strip() for header in rows[0].strip('|').split('|')]
    
    # Sprawdzenie i parsowanie danych w tabeli
    data = []
    for row in rows[1:]:
        columns = [col.strip() for col in row.strip('|').split('|')]
        # Sprawdzamy, czy liczba kolumn zgadza się z nagłówkami
        if len(columns) == len(headers):
            data.append(columns)
        else:
            print(f"Błąd: Wiersz ma inną liczbę kolumn niż nagłówki: {row}")
    
    # Tworzenie DataFrame z danych
    df = pd.DataFrame(data, columns=headers)
    
    # Zapis do pliku Excel
    df.to_excel(excel_filename, index=False)
    print(f"Zapisano do pliku: {excel_filename}")

# Wczytanie pliku tekstowego z tabelą w formacie wiki
with open("/Users/user/Desktop/tabelabackup.txt", "r") as file:
    wiki_table = file.read()

# Konwersja do Excela
wiki_table_to_excel(wiki_table, '/Users/user/Desktop/tabela_output.xlsx')