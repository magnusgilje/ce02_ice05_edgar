'''
Author : Albert Tran
Created: 2020-08-08

Examples showing extract the word count table from a list of 10-k filings.
'''

# %%
# ------------------------------------------------------------------------------
# File I/O
# ------------------------------------------------------------------------------
folder_clean10k = r'C:\temp\junk\10k_reports_clean'
file_out        = r'C:\temp\junk\sentiment_factors.csv'


# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import edgar.edgar_sentiment_wordcount as edgar_sentiment


# %%
# ------------------------------------------------------------------------------
# 10-k File Download (Full Download pf S&P100)
# ------------------------------------------------------------------------------
edgar_sentiment.write_document_sentiments(folder_clean10k, file_out)

