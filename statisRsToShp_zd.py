from rasterstats import zonal_stats

import csv
import sys
data = []
type=""


stats = zonal_stats(sys.argv[1],sys.argv[2],stats="min max mean count sum ",nodata=0,categorical=True,category_map={"a":1},geojson_out=True)
     
for t in stats:
 
    name = t.get('properties').get(sys.argv[3])
    a = t.get('properties').get(1.0)
  
    count = t.get('properties').get('count')
    a1=a if a!=None else 0.0

    count1=count if count!=None else 0.0
    if count1!=0:
        percentA=a1/count1
 
    else:
        percentA=0
       
    print(name, percentA)

 
    type="整地"	
   
    data.append([name, percentA,type])

with open(sys.argv[4],"w") as csvfile: 
    writer = csv.writer(csvfile,dialect='excel')
    writer.writerow('D12345T')
    m = len(data)
    for i in range(m):
         writer.writerow(data[i])
csvfile.close()	
