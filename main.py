import skillAudit as sa
import pandas as pd
import xlsxwriter


# =============================================================================
# Initial lists of lists
# =============================================================================

lib = sa.libToList('Skill Script Template.xlsx') #excell template w/ optimal skill data.
#Index[0] = [Department, Name, Login Id], Index[1] = [[Skill1,Pri1],[Skill2,Pri2], etc]

cur = sa.curToList('export_agent-loginID.txt') #txt file w/ programmed skill data.
#Index[0] = [Login Id, Name], Index[1] = [[Skill1,Pri1],[Skill2,Pri2], etc]


# =============================================================================
# Creates new list with only current data that matches library data based on Login Id
# Also updates index[0] to match index[0] of lib for dataframe grouping purposes.
# =============================================================================

newList = []

for i in cur:
    for j in lib:
        if i[0][0] == j[0][3]:
            empInfo = j[0] * 1
            curInfo = i * 1
            curInfo.pop(0)
            curInfo.insert(0,empInfo)
            newList.append(curInfo)

#Sort both lists
lib.sort()
newList.sort()

#adds value to index[0] that depicts the list type
for i in lib:
    i[0].append('Standard')
    i[1].sort(reverse=True)

for j in newList:
    j[0].append('Programmed')
    j[1].sort(reverse=True)

    
#combine two lists
combo = lib + newList


# =============================================================================
# Turn lists into dataframes
# =============================================================================

dfList = pd.DataFrame(combo, columns = ['empInfo','skillInfo']) 
#create dataframe w/ two colums, one for each list in list

#change each list into new columns 
empInfo = dfList['empInfo'].apply(pd.Series)
empInfo = empInfo.rename(columns = lambda x : 'tag_' + str(x)) 
skillInfo = dfList['skillInfo'].apply(pd.Series)
skillInfo = skillInfo.rename(columns = lambda x : 'tag2_' + str(x))

#Dataframe of all matched data between lists, based on Login Id
allMatches = pd.concat([empInfo[:], skillInfo[:]], axis=1)
allMatches = allMatches.rename(columns = {'tag_0':'Department','tag_1':'Template','tag_2':'Name','tag_3':'Login Id','tag_4':'Type','tag2_0':'S1','tag2_1':'S2','tag2_2':'S3','tag2_3':'S4','tag2_4':'S5','tag2_5':'S6','tag2_6':'S7','tag2_7':'S8','tag2_8':'S9','tag2_9':'S10','tag2_10':'S11','tag2_11':'S12','tag2_12':'S13','tag2_13':'S14','tag2_14':'S15','tag2_15':'S16','tag2_16':'S17','tag2_17':'S18','tag2_18':'S19','tag2_19':'S20'})
allMatches = allMatches.sort_values(['Department','Template','Name'])
allMatches = allMatches.set_index(['Department','Template','Name','Login Id','Type'])
allMatches = allMatches.astype(str)

#Replacing data to enhance column readability
allMatches = allMatches.replace('[\'\', \'\']','')
allMatches= allMatches.replace('\'\'','\'R1\'', regex=True)
allMatches= allMatches.replace('\[\'','', regex=True)
allMatches= allMatches.replace('\', \'',', ', regex=True)
allMatches= allMatches.replace('\'\]','', regex=True)

#Dataframe of skill based exceptions. Will return row if any Skill or Priority is not correct
skillExceptions = allMatches.reset_index()
skillExceptions = skillExceptions.drop_duplicates(subset=['Department','Template','Name','Login Id','S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','S14','S15','S16','S17','S18','S19','S20'], keep = False)
skillExceptions = skillExceptions.set_index(['Department','Template','Name','Login Id','Type'])

exceptionCount = skillExceptions.reset_index()
exceptionCount = exceptionCount[['Department','Template','Name','Login Id']].copy()
exceptionCount = exceptionCount.drop_duplicates(subset=['Department','Template','Name','Login Id'], keep='first')

statSummaryText = open('stats.txt', 'a')
statSummaryText.write(exceptionCount.to_string())
statSummaryText.close()
print(exceptionCount)
# =============================================================================
# Write all dataframes to Excel File for final review and correction.
# =============================================================================
with pd.ExcelWriter('Skill Audit.xlsx') as writer:  
    allMatches.to_excel(writer, sheet_name='Master List')
    skillExceptions.to_excel(writer, sheet_name='Skill Exceptions')




