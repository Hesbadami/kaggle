import pandas as pd
import numpy as np

def gen_data(weeks):
    dates = pd.date_range(
        start="2000-03-04",
        periods = weeks*7,
        freq = "D"
    )
    Y = dates.dayofweek + np.random.randint(-1, 2, weeks*7)
    data = pd.DataFrame({"y": Y, "ds": dates})
    return data