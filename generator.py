#!/usr/bin/env python3

# Author: Brendan Gregos
# Description: Basic site generator for vtluug-site. Reads from template.html and
# creates a page for each *.txt in the pages folder. For each page generated,
# the template is inserted and <!--*content--> is replaced with the content of
# each .txt file. The outputted filename is <name>.html for each page's <name>.txt

import os

template = open("template.html","r")
lines = template.readlines()
template.close()

for root, dirs, files in os.walk("./pages"):
    for file in files:
        if file.endswith(".txt"):
            createdFile = open(file[:-4]+".html","w")
            print("creating "+file[:-4]+".html")
            for line in lines:
                if "<!--*content-->" not in line:
                    createdFile.write(line)
                else:
                    replacmentString = ""
                    contentFile = open("./pages/"+file, "r")
                    for s in contentFile.readlines():
                        replacmentString += s
                    createdFile.write(line.replace("<!--*content-->", replacmentString))
                    contentFile.close()
            createdFile.close()
