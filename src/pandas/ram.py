#!/usr/bin/env python

"""
This demos shows the types of columsn in a pandas table...
"""

import pandas
import random
import sys
import os, psutil

if False:
    tbl = pandas.read_csv("data.csv")
    print(tbl.dtypes)
    print("==========================================")
    for (columnName, columnData) in tbl.iteritems():
        print(f"{columnName} {tbl[columnName].dtype}")
    print(tbl.memory_usage())
    print(sys.getsizeof(tbl))
# 890*12
m=[]
for i in range(890):
    new_row=[]
    for j in range(12):
        new_row.append(random.random())
    m.append(new_row)
process = psutil.Process(os.getpid())
print(process.memory_info().rss)  # in bytes 
