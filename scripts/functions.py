import data_loading as dl
import random
import math
import numpy as np

def linear_function(ref_x, keys, df, total, x=0.61):
    mse = 0
    for key in keys:
        sum = 0
        for row in df.itertuples():
            party_result = getattr(row, key)
            result = party_result * x / ref_x[key] 
            sum += round(result)
        mse += (sum - x * total) ** 2
    return mse / len(keys), mse / (total ** 2)

def improved_linear_function(ref_x, keys, df, total, x=0.61):
    mse = 0
    mse_dict = {}
    for row in df.itertuples():
        total_votes = row.totalVotes
        total_sum = 0
        for key in keys:
            party_results = getattr(row, key)
            result = party_results * x / ref_x[key]
            mse_dict[key] = mse_dict.get(key, 0) + round(result)
            total_sum += round(result)
        if total_sum == 0: print(row)
        coeff = total_votes / total_sum
        
        floored_dict = {}
        residuals = []

        for key in keys:
            scaled = mse_dict[key] * coeff
            floored = math.floor(scaled)
            floored_dict[key] = floored
            residual = scaled - floored
            residuals.append((key, residual))
        residuals.sort(key=lambda x: x[1], reverse=True)
        remainder = math.floor(sum([v * coeff for v in mse_dict.values()]) - sum(floored_dict.values()))
        
        while remainder > 0:
            key, _ = residuals.pop(0)
            floored_dict[key] += 1
            remainder -= 1        
    for key in keys:
        mse += (mse_dict[key] - x * total) ** 2
    return mse / len(keys), mse / (total ** 2)