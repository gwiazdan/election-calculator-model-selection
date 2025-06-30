import os
import json
import pandas as pd

def list_json_files(folder_path):
    """
    Zwraca listę nazw plików JSON w podanym folderze.
    """
    return [f for f in os.listdir(folder_path) if f.endswith('.json')]

def load_json_to_dataframe(folder_path, filename):
    """
    Wczytuje plik JSON jako pandas DataFrame.
    """
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return pd.DataFrame(data)

# Przykład użycia:
# files = list_json_files('../data')
# df = load_json_to_dataframe('../data', files[0])