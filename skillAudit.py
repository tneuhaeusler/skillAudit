# =============================================================================
# Class File for skillAudit
# =============================================================================
import pandas as pd
import numpy as np

class skillAudit:
    
    skillDictionary = []
    skillCurrent = []
    errorList = []
    
    def __init__(self, sDict, sCurrent):
        self.skillDictionary = sDict
        self.skillCurrent = sCurrent
        if self.skillCurrent != self.skillDictionary:
            self.errorList.append('Not Equal')
        else:
            self.errorList.append('Equal')

##helper function that change Excel Skill Library to List
def libToList(fileName):
    fileName = fileName
    df = pd.read_excel(fileName)
    #df.drop(df.index[0])
    df = df.replace(np.nan, '', regex=True)    
    empList = df.values.tolist()

    newList = []
    finalList = []
    for item in empList:
        tlist = []
        for i in item:
            if type(i) == float:
                i = int(i)          
            if i == 'R1' or i == 'R2':
                i = ''
            tlist.append(str(i))
        newList.append(tlist)  
    for i in newList:
        templist = []
        templist.append(list(i[1:4]))
        templist.append(list(i[9:]))
        finalList.append(templist)
    for i in finalList:
        it = 0
        skills = i[1]
        i[1] = list()
        while it<len(skills):
            i[1].append(skills[it:it+2])
            it+=2
        
    return(finalList)
    
##helper function that changes CMS login file dump to List
def curToList(fileName):
    fileName = fileName
    df = pd.read_csv(fileName, sep=',')
    df = df.replace(np.nan, '', regex=True)  
    empList = df.values.tolist()
    newList = []
    finalList = []
    for item in empList:
        tlist = []
        for i in item:
            if type(i) == float:
                i = int(i)          
            tlist.append(str(i))
        newList.append(tlist)
    for i in newList:
        templist = []
        templist.append(list(i[0:2]))
        templist.append(list(i[2:42]))
        finalList.append(templist)
    for i in finalList:
        it = 0
        skills = i[1]
        i[1] = list()
        while it<len(skills):
            i[1].append(skills[it:it+2])
            it+=2
            
    return(finalList)
