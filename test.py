# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:07:02 2020

@author: Tanner - Home
"""

import skillAudit as sa
import pandas as pd
import xlsxwriter
import operator


# =============================================================================
# Initial lists of lists
# =============================================================================

lib = sa.libToList('Skill Script Template.xlsx') #excell template w/ optimal skill data.
#Index[0] = [Department, Name, Login Id], Index[1] = [[Skill1,Pri1],[Skill2,Pri2], etc]

cur = sa.curToList('export_agent-loginID.txt') #txt file w/ programmed skill data.
#Index[0] = [Login Id, Name], Index[1] = [[Skill1,Pri1],[Skill2,Pri2], etc]

newList = []

for i in lib:
    tempList = []
    tempList.append(i[0])
    
    
    test_list = i[1]
    for i in test_list:
        tempList = i
        intConversion = [int(i) for i in tempList]
        tempList.append(intConversion)


        

            
    
    sorted_list = sorted(intList,key=operator.itemgetter(0))
    tempList.append(sorted_list)
    newList.append(tempList)
    

print(newList[28])
print(type(newList[1][0][0]))
print(cur[56])