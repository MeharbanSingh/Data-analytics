# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 01:39:38 2017

@author: Meharban waraich
"""

import re
file_in = open('DaLogIT.txt', 'r')
file_out = open('sensordata.csv', 'w')
for line_in in file_in:
    line_in = file_in.readline()
    print(line_in)
    line_in =  re.sub('\*',' ',line_in)
    line_out = re.sub('\s{5,}', ',', line_in.strip()) + '\n' # \s+
    print(line_out)
    file_out.write(line_out)
file_out.close()    
file_in.close()

#%%

file = open('sensordata.csv','r')
header = file.readline()
row= file.readline()
print(row)
file.close()

#%%
