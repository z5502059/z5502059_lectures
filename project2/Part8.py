import config as cfg
import test2 as zid


import pandas as pd
import os

# ----------------------------------------------------------------------------
# Part 8: Answer the following questions
# ----------------------------------------------------------------------------
# NOTES:
#
# - You can create a separate module (you can call it main.py if you want)
#   and then use the functions defined above to answer the questions below.
#   YOU DO NOT NEED TO SUBMIT THIS OTHER MODULE YOU CREATE. THE ONLY MODULE
#   YOU NEED TO SUBMIT IS THIS ONE, zid_project2.py.
#
# - Do not create any other functions inside this module.
#
# - For this part of the project, only the answers provided below will be
#   marked. You are free to create any function you want (IN A SEPARATE
#   MODULE).
#
# - All your answers should be strings. If they represent a number, include 4
#   decimal places.
#
# - Here is an example of how to answer the questions below. Consider the
#   following question:
#
#   Q0: Which ticker included in config.TICMAP starts with the letter "C"?
#   Q0_answer = '?'
#
#   You should replace the '?' with the correct answer:
#   Q0_answer = 'CSCO'
#

# Q1: Which stock in your sample has the highest average daily return for the
#     year 2020 (ignoring missing values)? The sample should include all tickers
#     included in the dictionary config.TICMAP. Your answer should include the
#     ticker for this stock.
Q1_ANSWER = '?'

# Solution
tickers = cfg.TICKERS
df_dailypr = zid.mk_prc_df(tickers, prc_col='adj_close')
df_dailyrt = zid.mk_ret_df(df_dailypr)
average_dailyrt = {}
for column in df_dailyrt:
    avg = zid.get_avg(df_dailyrt, column, 2020)
    average_dailyrt[column] = avg
answer1 = max(average_dailyrt,key=average_dailyrt.get)
#print('tickers')
#print(tickers)
#print('df_dailypr')
#print(df_dailypr)
#print('mk_ret_df')
#print(df_dailypr)
#print('average_dailyrt')
#print(average_dailyrt)

print('Q1')
print(answer1)

# Q2: What is the annualised return for the EW portfolio of all your stocks in
# the config.TICMAP dictionary from the beginning of 2010 to the end of 2020?
Q2_ANSWER = '?'

# Solution
tickersl = [i.lower() for i in tickers]
ser_ewdailyrt = zid.get_ew_rets(df_dailyrt, tickersl)
#print('ser_ewdailyrt')
#print(ser_ewdailyrt)

answer2 = zid.get_ann_ret(ser_ewdailyrt, '2010-01-01', '2020-12-31')
print('Q2')
print(answer2)

# Q3: What is the annualised daily return for the period from 2010 to 2020 for
# the stock with the highest average return in 2020 (the one you identified in
# the first question above)?
Q3_ANSWER = '?'

# Solution
ser_tsla = df_dailyrt.loc[: , 'tsla']
answer3 = zid.get_ann_ret(ser_tsla, '2010-01-01', '2020-12-31')
print('Q3')
print(answer3)

# Q4: What is the annualised daily ABNORMAL return for the period from 2010 to 2020 for
# the stock with the highest average return in 2020 (the one you identified in
# the first question Q1 above)? Abnormal returns are calculated by subtracting
# the market return ("mkt") from the individual stock return.
Q4_ANSWER = '?'

# Solution
df_dailyabrt = zid.mk_aret_df(df_dailyrt)
ser_tslaab = df_dailyabrt.loc[:,'tsla']
answer4 = zid.get_ann_ret(ser_tslaab,'2010-01-01', '2020-12-31')
print('Q4')
print(answer4)

