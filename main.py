import skillAudit as sa
import pandas as pd


lib = sa.libToList('Skill Script Template.xlsx')
cur = sa.curToList('export_agent-loginID.txt')

newList = []

for i in cur:
    for j in lib:
        if i[0][0] == j[0][2]:
            empInfo = j[0] * 1
            curInfo = i * 1
            curInfo.pop(0)
            curInfo.insert(0,empInfo)
            newList.append(curInfo)


lib.sort()
newList.sort()

for i in lib:
    i[0].append('Standard')
    i[1].sort(reverse=True)

for j in newList:
    j[0].append('Programmed')
    j[1].sort(reverse=True)
   
df1 = pd.DataFrame(lib)
df2 = pd.DataFrame(newList)



#for i in lib:
#    if i[0] not in (x[0] for x in newList):
#        print(i[0])
#for i in newList:
#    if i[0] not in (x[0] for x in lib):
#        print('Not in CMS or Users Login Credentials Dont Match User in Skill Library')


combo = lib + newList
dfList = pd.DataFrame(combo, columns = ['empInfo','skillInfo'])
 
empInfo = dfList['empInfo'].apply(pd.Series)
empInfo = empInfo.rename(columns = lambda x : 'tag_' + str(x))
 
skillInfo = dfList['skillInfo'].apply(pd.Series)
skillInfo = skillInfo.rename(columns = lambda x : 'tag2_' + str(x))
 
final = pd.concat([empInfo[:], skillInfo[:]], axis=1)
final = final.rename(columns = {'tag_0':'Department','tag_1':'Name','tag_2':'Login Id','tag_3':'Type','tag2_0':'S1','tag2_1':'S2','tag2_2':'S3','tag2_3':'S4','tag2_4':'S5','tag2_5':'S6','tag2_6':'S7','tag2_7':'S8','tag2_8':'S9','tag2_9':'S10','tag2_10':'S11','tag2_11':'S12','tag2_12':'S13','tag2_13':'S14','tag2_14':'S15','tag2_15':'S16','tag2_16':'S17','tag2_17':'S18','tag2_18':'S19','tag2_19':'S20'})
final = final.sort_values(['Department','Name'])
final = final.set_index(['Department','Name','Login Id','Type'])
final = final.astype(str)

new = final.reset_index()
new = new.drop_duplicates(subset=['Department','Name','Login Id','S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','S14','S15','S16','S17','S18','S19','S20'], keep = False)
new = new.set_index(['Department','Name','Login Id','Type'])
#print(new.applymap(lambda x: isinstance(x, str)).all())
#print(final.dtypes)

with pd.ExcelWriter('Skill Audit.xlsx') as writer:  
    final.to_excel(writer, sheet_name='Raw Data')
    new.to_excel(writer, sheet_name='Exceptions')
    
#print(len(lib))
#print(len(newList))
#print(newList[0])
#print(lib[0])
#print(newList[0][0])
#print(lib[0][0])
#print(hex(id(newList[0][0])))
#print(hex(id(lib[0][0])))
