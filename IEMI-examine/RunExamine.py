from datetime import datetime
from checkIEMI import checkIEMI
from DBS_swapped import DBS_swapped


DBS_swapped = DBS_swapped()
t = DBS_swapped.findAllData()

listData = (list(t))
newlist =[]
for i in listData:
    check = checkIEMI(i['IEMI'])
    requit=check.Run()
    i['requit'] = requit
    i['DataTime']=datetime.now()
    newlist.append(i)


for i in newlist:
    DBS_swapped.updateOneData({'_id': i['_id']},{'$set':i})
