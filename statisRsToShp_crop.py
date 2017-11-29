from rasterstats import zonal_stats

import csv
import sys
data = []
type=""


stats = zonal_stats(sys.argv[1],sys.argv[2],stats="min max mean count sum ",nodata=0,categorical=True,category_map={"a":1,"b":2,"c":3,"d":4,"e":5},geojson_out=True)
     
for t in stats:
 
    name = t.get('properties').get(sys.argv[3])
    a = t.get('properties').get(1.0)
    b = t.get('properties').get(2.0)
    c = t.get('properties').get(3.0) 
    d = t.get('properties').get(4.0) 
    e = t.get('properties').get(5.0) 
    count = t.get('properties').get('count')
    a1=a if a!=None else 0.0
    b1=b if b!=None else 0.0
    c1=c if c!=None else 0.0
    d1=d if d!=None else 0.0
    e1=e if e!=None else 0.0
    count1=count if count!=None else 0.0
    if count1!=0:
        percentA=a1/count1
        percentB=b1/count1
        percentC=c1/count1
        percentD=d1/count1
        percentE=e1/count1
    else:
        percentA= percentB= percentC=percentD=percentE=0
       
    print(name, percentA, percentB,percentC, percentD,percentE)

    if a1==max(a1,b1,c1,d1,e1):
        type="苜蓿"	
    elif b1==max(a1,b1,c1,d1,e1):
        type="玉米"
    elif c1==max(a1,b1,c1,d1,e1):
        type="葵花" 
    elif d1==max(a1,b1,c1,d1,e1):
        type="荒地" 
    elif e1==max(a1,b1,c1,d1,e1):
        type="林地" 
    data.append([name, percentA, percentB, percentC, percentD,percentE,type])

with open(sys.argv[4],"w") as csvfile: 
    writer = csv.writer(csvfile,dialect='excel')
    writer.writerow('D12345T')
    m = len(data)
    for i in range(m):
         writer.writerow(data[i])
csvfile.close()	
