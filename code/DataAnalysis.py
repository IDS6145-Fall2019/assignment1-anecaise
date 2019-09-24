#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Data include average daily ridership for all WMATA metro stops in May"""

# import
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Set path & read file
datadir = "../Data/ridership.xlsx"
data = pd.read_excel(datadir).drop(columns={"Unnamed: 0"})
data = data.drop([47, 48, 49, 94, 95, 96], axis=0)
data_summary = data.describe()


# Save descrpitive stats
data_summary.to_csv("../Data/descriptive_stats.csv")


# Vis raw data
hist = plt.figure(1)
plt.hist(data['2018***'], bins = 9, histtype = 'bar', color = 'grey',
         edgecolor = 'black', )
plt.title("Daily Ridership - All WMATA Stations, May")
plt.xlabel("Daily Ridership")
plt.ylabel("Number of Stations")


plt.savefig(fname = "../images/Raw_data_hist.png",dpi = 100, edgecolor='b')
plt.show()

# plt.close()

# Vis summary data
bar = plt.figure(2)
plt.bar(data_summary.columns, height = data_summary.iloc[1,:], 
        yerr = data_summary.iloc[2,:], color = 'grey',edgecolor='black')

plt.title(" WMATA Ridership Data Year over Year (2015-18)")
plt.xlabel("Operation Year")
plt.ylabel("Average Riders")
plt.savefig("../Images/SummaryStats_visualized.png", dpi=100)
plt.show()


# Visual Raw Data Set (NYC Transit)
data2 =  pd.read_csv("../Data/nyc_transit.csv")
data2 = data2[data2['Entrance Type'] != 'Ramp']
data2 = data2[data2['Entrance Type'] != 'Walkway']

freq = sns.countplot(y = 'Entrance Type', hue = 'Division', data = data2,
                     palette = 'Greys_d')
plt.title('NYC Subway Entrance Type')
plt.xlabel('Number of Stations')
plt.ylabel('Entrance Type')
plt.tight_layout()
plt.savefig("../Images/NYC_entrance_types.png", dpi = 100)
plt.show()
