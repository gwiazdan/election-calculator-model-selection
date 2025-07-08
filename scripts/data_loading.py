import os
import json
import pandas as pd

folder_path = "scripts/data/"

def list_json_files():
    return [f for f in os.listdir(folder_path) if f.endswith('.json')]

def load_json_to_dataframe(filename):
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    keys = df['votes'].iloc[0].keys()
    votes_df = df['votes'].apply(pd.Series)
    df_expanded = pd.concat([df.drop(columns=['votes']), votes_df], axis=1)
    keys = list(keys)
    keys.append('others')
    keys.remove('mn')
    df_expanded['others'] = df_expanded['totalVotes'] - df_expanded[list(keys[:-1])].sum(axis=1)
    return df_expanded, keys 

def load_all_df():
    dfs = []
    json_files = list_json_files()
    keys = {}
    for file in json_files:
        df, file_keys = load_json_to_dataframe(file)
        if not keys: keys = file_keys
        dfs.append(df.fillna(0))
    return dfs, keys
            
def calculate_ref_results(df, keys):
    dict = {}
    total = df['totalVotes'].sum()
    for key in keys:
        votes = df[key].sum()
        dict[key] = votes / total if total > 0 else 0
    return dict
