#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
import sys, getopt
import pandas as pd
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element,ElementTree
from xml.dom import minidom

def write_xml(datas, outputf):
    root = ET.Element("calibration")
    reflecth = ET.Element("handreflectorHeight")
    meters = ET.Element("meters")
    meters.text = str(datas["handreflectorHeight"][0])
    meters.tail ="\n"
    reflecth.append(meters)
    root.append(reflecth)   #添加子节点

    raderheight = ET.Element("installraderheight")
    mters = ET.Element("meters")
    mters.text = str(datas["installraderheight"][0])
    mters.tail ="\n"
    raderheight.append(mters)
    root.append(raderheight)

    #extend(subments) #添加多个子节点

    origpoll = ET.Element("originpoll")
    lng = ET.Element("lng")
    lng.text = str(datas["originpoll"][0])
    lng.tail ="\n"
    origpoll.append(lng)
    root.append(origpoll)

    lat =ET.Element("lat")
    lat.text = str(datas["originpoll"][1])
    lat.tail = "\n"
    origpoll.append(lat)

    radarmeasure= ET.Element("radarmeasure")
    size = 0 
    for i in datas["radarmeasureX"]:
        if pd.isna(i)==False:
            size+=1

    for elem in range(size):
        hors = "hors{}".format(elem)
        hors = ET.Element("horizontalDis")
        hors.text = str(datas["radarmeasureX"][elem])
        hors.tail ="\n"
        vert = "verts{}".format(elem)
        vert = ET.Element("verticalDis")
        vert.text = str(datas["radarmeasureY"][elem])
        vert.tail = "\n"
        radarmeasure.extend([hors, vert])
    root.append(radarmeasure)

    pickpoint = ET.Element("pickpoint")
    for i in range(size):
        index = ET.Element("index")
        index.text = str(i+1)
        index.tail = "\n"
        pickpoint.append(index)
    root.append(pickpoint)

    pixelcoord = ET.Element("pixelcoord")
    for i in range(size):
        xcoord = ET.Element("xcoord")
        xcoord.text =str(datas["pixelcoordX"][i])
        xcoord.tail = "\n"
        ycoord = ET.Element("ycoord")
        ycoord.text = str(datas["pixelcoordY"][i])
        ycoord.tail = "\n"
        pixelcoord.extend([xcoord,ycoord])
    
    root.append(pixelcoord)

    gps = ET.Element("gps")
    for i in range(size):
        lon = ET.Element("lon")
        lon.text = str(datas['lon'][i])
        lon.tail = "\n"
        gps.append(lon)

    for i in range(size):
        lan = ET.Element("lan")
        lan.text = str(datas['lan'][i])
        lan.tail = "\n"
        gps.append(lan)
    root.append(gps)

    distort =ET.Element("distort")
    for i in range(5):
        values = "value{}".format(i)
        value = ET.Element(values)
        value.text = str(datas["distort"][i])
        value.tail = "\n"
        distort.append(value)
    root.append(distort)

    gpsheight = ET.Element("gpsheight")
    gp0 = ET.Element("gp0")
    gp0.text = str(datas["origgpsheight"][0])
    gp0.tail = "\n"
    gpsheight.append(gp0)
    for i in range(size):
        gp = ET.Element("gp")
        gp.text = str(datas["gpsheight"][i])
        gp.tail = "\n"
        gpsheight.append(gp)

    root.append(gpsheight)

    camerainstrinic = ET.Element("camerainstrinic")
    fx = ET.Element("fx")
    fx.text = str(datas['camerainstrinic'][0])
    fx.tail = "\n"
    camerainstrinic.append(fx)
    fy = ET.Element("fy")
    fy.text = str(datas['camerainstrinic'][1])
    fy.tail = "\n"
    camerainstrinic.append(fy)
    cx = ET.Element("cx")
    cx.text = str(datas['camerainstrinic'][2])
    cx.tail = "\n"
    camerainstrinic.append(cx)

    cy = ET.Element("cy")
    cy.text = str(datas['camerainstrinic'][3])
    cy.tail = "\n"
    camerainstrinic.append(cy)
    root.append(camerainstrinic)


    tree = ET.ElementTree(root)
    tree.write(outputf, encoding="utf-8", xml_declaration=True)  #保存时无缩进，添加缩进需要借用dom

    #借用dom，添加缩进
    rawtext = ET.tostring(root)
    dom = minidom.parseString(rawtext)
    with open(outputf, "w") as f:
        dom.writexml(f, indent="\t", newl="", encoding="utf-8")



def main(argv):
    
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print (' -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(' -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        if outputfile == None:
            outputfile = "input.xml"
            pass
    print("input:",inputfile)
    print("output:",outputfile)
    df = pd.read_excel(inputfile)
    write_xml(df,outputfile)
 
if __name__ == "__main__":
    main(sys.argv[1:])
   


# In[ ]:




