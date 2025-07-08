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
    
    def get_keys(self):
        return self.keys
        
    def calculate_mse(self, func, results):
        error = 0
        start_time = time.time()
        for i in range(len(results)):
            error += (self.__single_calculation(func, results[i]))**2
        end_time = time.time()
        avg_time = (end_time - start_time) / len(results)
        mse = error
        rmse = mse / ((len(results)) ** 2 * self.total ** 2)
             
        return mse, rmse, avg_time
    
    def __single_calculation(self, func, x):
        if not callable(func):
            raise TypeError("The provided argument must be a callable function.")

        error = func(df=self.df, ref_x=self.ref_x, keys=self.keys, total=self.total, x=x)

        return error
        
         