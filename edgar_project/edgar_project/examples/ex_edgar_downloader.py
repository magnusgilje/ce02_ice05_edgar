'''
Author : Albert Tran
Created: 2020-08-08
'''
import sys
sys.path.insert(0,"..")
import edgar_downloader
import ref_data as edgar_refdata

# from tqdm import tqdm




# %%
# ------------------------------------------------------------------------------
# File I/O
# ------------------------------------------------------------------------------
# This is the folder where the reports will be downloaded
data_dir = r"C:\temp\junk\10k_reports_raw"


# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------



# %%
# ------------------------------------------------------------------------------
# 10-k File Download (Full Download pf S&P100)
# ------------------------------------------------------------------------------
# Specify the company whose 10-k reports we are interested in.
df_sp100 = edgar_refdata.get_sp100()
# tickers  = df_sp100['Symbol']
tickers  = ['MSFT'] # Smaller subset

# Download the data for each ticker
# Note that this takes around 50 minutes to run.
for i, ticker in enumerate(tickers):
    print(f'{int((i/len(tickers))*100)}% complete. Current ticker: {ticker}.')
    edgar_downloader.download_files_10k(ticker, data_dir)
    print('--------------------------------')

print('done')
