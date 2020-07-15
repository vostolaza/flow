from matplotlib import pyplot as plt
import numpy as np
import matplotlib.cm as cm
import requests
#import dill
from bs4 import BeautifulSoup
#from datetime import datetime
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring, tostring
page = requests.get('https://traffic.api.here.com/traffic/6.2/flow.xml?app_id=OWqjCxiAY05whclUdI3p&app_code=eOcDcNMUJTTDAg6f_6Tc7Q&bbox=39.039696,-77.222108;38.775208,-76.821107&responseattributes=sh,fc')
# page = requests.get('https://traffic.api.here.com/traffic/6.2/flow.xml?app_id=OWqjCxiAY05whclUdI3p&app_code=eOcDcNMUJTTDAg6f_6Tc7Q&bbox=-12.087572,-77.030212;-12.097822,-77.018138&responseattributes=sh,fc')
soup = BeautifulSoup(page.content, "lxml")
roads = soup.find_all('fi')

a1=[]
loc_list_hv=[]
lats=[]
longs=[]
sus=[]
ffs=[]
cn=0
for road in roads:
    #for j in range(0,len(shps)):
    myxml = fromstring(str(road))
    fc=5
    for child in myxml:
        #print(child.tag, child.attrib)
        if('fc' in child.attrib):
            fc=int(child.attrib['fc'])
        if('cn' in child.attrib):
            cn=float(child.attrib['cn'])
        if('su' in child.attrib):
            su=float(child.attrib['su'])
        if('ff' in child.attrib):
            ff=float(child.attrib['ff'])
    # if((fc<=2) and (cn>=0.7)):
    if(cn>=0.7):
        shps=road.find_all("shp")
        for j in range(0,len(shps)):
            latlong=shps[j].text.replace(',',' ').split()
            #loc_list=[]
            la=[]
            lo=[]
            su1=[]
            ff1=[]

            for i in range(0,int(len(latlong)/2)):
                loc_list_hv.append([float(latlong[2*i]),float(latlong[2*i+1]),float(su),float(ff)])
                la.append(float(latlong[2*i]))
                lo.append(float(latlong[2*i+1]))
                su1.append(float(su))
                ff1.append(float(ff))
            lats.append(la)
            longs.append(lo)
            sus.append(np.mean(su1))
            ffs.append(np.mean(ff1))

fig=plt.figure()
plt.style.use('dark_background')
#plt.plot(np.linspace(0,10,10),np.linspace(0,10,10))
plt.grid(False)
for i in range(0,len(lats)):
    if(sus[i]/ffs[i]<0.25):
        plt.plot(longs[i],lats[i], c='brown',linewidth=0.5)
    elif(sus[i]/ffs[i]<0.5):
        plt.plot(longs[i],lats[i], c='red',linewidth=0.5)
    elif(sus[i]/ffs[i]<0.75):
        plt.plot(longs[i],lats[i], c='yellow',linewidth=0.5)
    else:
        plt.plot(longs[i],lats[i], c='green',linewidth=0.5)
    #print(i)
#plt.xlim(-77.055,-77.015)
#plt.ylim(38.885,38.91)
plt.axis('off')
plt.show()