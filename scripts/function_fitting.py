import data_loading as dl
import time
class function_fitter:
    
    def __init__(self, i=0):
        dfs, keys = dl.load_all_df()
        if i < 0 or i >= len(dfs):
            raise IndexError("Index out of range for the list of dataframes.") 
        self.df = dfs[i]
        self.keys = keys
        self.total = self.df['totalVotes'].sum()
        self.ref_x = dl.calculate_ref_results(self.df, self.keys)
        
    def calculate_mse(self, func, x=0.61):
        if not callable(func):
            raise TypeError("The provided argument must be a callable function.")

        mse, rmse = func(df=self.df, ref_x=self.ref_x, keys=self.keys, total=self.total, x=x)
        
        time_sum = 0
        for i in range(10):
            start_time = time.time()
            func(df=self.df, ref_x=self.ref_x, keys=self.keys, total=self.total, x=x)
            end_time = time.time()
            time_sum += (end_time - start_time)
        
        return mse, rmse, time_sum / 10
                    
        
         