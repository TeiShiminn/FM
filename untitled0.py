#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 08:55:35 2025

@author: chengzimin
"""

# %%
import pandas as pd
import matplotlib.pyplot as plt
import os
os.getcwd()  # working path "..../FM"
# %%

# load Data
# SPX 
SPX_DailyReturn = pd.read_csv("./Data/SPX_Daily.csv")
SPX_DailyReturn.rename(columns={'sprtrn':'SPX'}, inplace=True)
SPX_DailyReturn['SPX'] = SPX_DailyReturn['SPX']*100
SPX_DailyReturn['DATE'] = pd.to_datetime(SPX_DailyReturn['DATE']).dt.date
# VIX
VIX_DailyReturn = pd.read_csv('./Data/VIX_Daily.csv')
VIX_DailyReturn.rename(columns={'Date':'DATE', 'vix':'VIX'}, inplace=True)
VIX_DailyReturn['DATE'] = pd.to_datetime(VIX_DailyReturn['DATE']).dt.date
VIX_DailyReturn.sort_values(by = 'DATE')
# merge data
SPX_DailyData = pd.merge(SPX_DailyReturn, VIX_DailyReturn, on='DATE', how='left')
SPX_DailyData
# Top worst
Top10Worst = SPX_DailyData.nsmallest(10, 'SPX').reset_index(drop=True)
Top10Worst.insert(0, 'Rank', range(1,11))
Top10Worst[['SPX', 'VIX']] = Top10Worst[['SPX', 'VIX']].round(2).fillna("")

# %%
# plot
plt.figure(figsize=(5, 5))
plt.plot(SPX_DailyReturn['DATE'], SPX_DailyReturn['SPX'], linestyle='None', \
         color='blue', marker='o', markersize=1)
plt.ylim(-25, 15)
plt.scatter(Top10Worst['DATE'], Top10Worst['SPX'], facecolors='none', edgecolors='red', marker='o', s=50, linewidths=0.5)
plt.title('Daily SPX Returns (%)')
plt.show()

# %%