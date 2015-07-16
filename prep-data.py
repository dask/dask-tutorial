import pandas as pd
from accounts import *
import os

if not os.path.exists('data'):
    os.mkdir('data')

def accounts_csvs(num_files, n, k):
    ids, names, wealth_mag, wealth_trend, freq = account_params(k)
    for i in range(num_files):
        df = account_entries(n, ids, names, wealth_mag, wealth_trend, freq)
        df.to_csv(os.path.join('data', 'accounts.%d.csv' % i), index=False)
