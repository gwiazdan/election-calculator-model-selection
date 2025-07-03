import data_loading as dl

def linear_function(ref_x, keys, df, total, x=0.61):
    
    mse = 0
    for key in keys:
        sum = 0
        for row in df.itertuples():
            party_result = getattr(row, key)
            result = party_result * x / ref_x[key] if ref_x[key] != 0 else 0
            sum += round(result)
        mse += (sum - x * total) ** 2
    return mse / len(keys), mse / (total ** 2)