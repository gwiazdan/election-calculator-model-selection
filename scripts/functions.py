from scipy.interpolate import PchipInterpolator
def linear_function(ref_x, keys, df, total, x, **kwargs):
    err = 0
    for key in keys:
        sum = 0
        for row in df.itertuples():
            party_result = getattr(row, key)
            result = party_result * x[key] / ref_x[key] 
            sum += round(result)
        err += abs(sum - x[key] * total)
    return err

def improved_linear_function(ref_x, keys, df, total, x, **kwargs):
    final_party_sums = {key: 0 for key in keys}
    for row in df.itertuples():
        initial_results_float = {}
        initial_sum = 0
        for key in keys:
            party_votes = getattr(row, key)
            result = (party_votes * x[key] / ref_x[key]) if ref_x[key] != 0 else 0
            initial_results_float[key] = result
            initial_sum += result
            
        actual_total_votes = row.totalVotes
        if initial_sum == 0:
            continue 
        coeff = actual_total_votes / initial_sum
        
        rescaled_votes = {key: val * coeff for key, val in initial_results_float.items()}
        final_votes_int = {key: int(v) for key, v in rescaled_votes.items()}
        remainders = {key: v - final_votes_int[key] for key, v in rescaled_votes.items()}
        current_sum = sum(final_votes_int.values())
        votes_to_distribute = actual_total_votes - current_sum
        sorted_parties = sorted(remainders, key=remainders.get, reverse=True)
        for i in range(votes_to_distribute):
            party_to_get_vote = sorted_parties[i]
            final_votes_int[party_to_get_vote] += 1

        for key in keys:
            final_party_sums[key] += final_votes_int[key]
    err = 0
    for key in keys:
        expected_votes = x[key] * total
        error = final_party_sums[key] - expected_votes
        err += abs(error)
    return err

def linear_splines(ref_x, keys, df, total, x, **kwargs):
    final_party_sums = {key: 0 for key in keys}
    for row in df.itertuples():
        initial_results_float = {}
        initial_sum = 0
        for key in keys:
            party_votes = getattr(row, key)
            percentage = party_votes / row.totalVotes
            if x[key] >= ref_x[key]:
                perc_result = percentage + (1-percentage)/(1-ref_x[key]) * (x[key]-ref_x[key])
            else: 
                perc_result = percentage / ref_x[key] * x[key]
            result = perc_result * row.totalVotes
            initial_results_float[key] = result
            initial_sum += result
            
        actual_total_votes = row.totalVotes
        if initial_sum == 0:
            continue 
        coeff = actual_total_votes / initial_sum
        
        rescaled_votes = {key: val * coeff for key, val in initial_results_float.items()}
        final_votes_int = {key: int(v) for key, v in rescaled_votes.items()}
        remainders = {key: v - final_votes_int[key] for key, v in rescaled_votes.items()}
        current_sum = sum(final_votes_int.values())
        votes_to_distribute = actual_total_votes - current_sum
        sorted_parties = sorted(remainders, key=remainders.get, reverse=True)
        for i in range(votes_to_distribute):
            party_to_get_vote = sorted_parties[i]
            final_votes_int[party_to_get_vote] += 1

        for key in keys:
            final_party_sums[key] += final_votes_int[key]
    err = 0
    for key in keys:
        expected_votes = x[key] * total
        error = final_party_sums[key] - expected_votes
        err += abs(error)
    return err

def pchip_interpolation(ref_x, keys, df, total, x, **kwargs):
    final_party_sums = {key: 0 for key in keys}
    for row in df.itertuples():
        initial_results_float = {}
        initial_sum = 0
        for key in keys:
            party_votes = getattr(row, key)
            percentage = party_votes / row.totalVotes
            f = PchipInterpolator([0.0, ref_x[key], 1.0], [0.0, percentage, 1.0])
            perc_result = f(x[key])
            result = perc_result * row.totalVotes
            initial_results_float[key] = result
            initial_sum += result
            
        actual_total_votes = row.totalVotes
        if initial_sum == 0:
            continue 
        coeff = actual_total_votes / initial_sum
        
        rescaled_votes = {key: val * coeff for key, val in initial_results_float.items()}
        final_votes_int = {key: int(v) for key, v in rescaled_votes.items()}
        remainders = {key: v - final_votes_int[key] for key, v in rescaled_votes.items()}
        current_sum = sum(final_votes_int.values())
        votes_to_distribute = actual_total_votes - current_sum
        sorted_parties = sorted(remainders, key=remainders.get, reverse=True)
        for i in range(votes_to_distribute):
            party_to_get_vote = sorted_parties[i]
            final_votes_int[party_to_get_vote] += 1
        for key in keys:
            final_party_sums[key] += final_votes_int[key]
    err = 0
    for key in keys:
        expected_votes = x[key] * total
        error = final_party_sums[key] - expected_votes
        err += abs(error)
    return err