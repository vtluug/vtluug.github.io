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

consts = {"currentSem": "Fall 2025",
          "currentSemShort": "Fall '25",
          "currentSchoolYear": "2025-26"}
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
                        i = 0
                        news = ""
                        while i < len(s):
                            if i < len(s)-2 and s[i:i+3] == "\\${":
                                news += "${"
                                i += 3
                            if s[i] == "$" and i < len(s)-1 and s[i+1] == "{":
                                key = ""
                                i += 2
                                while i < len(s) and s[i] != "}":
                                    key += s[i]
                                    i += 1
                                if i >= len(s) and s[i] != "}":
                                    raise IndexError("Expected '}' before end of line")
                                if key not in consts:
                                    raise KeyError("Invalid key '%s'" % key)
                                news += consts[key]
                            else:
                                news += s[i]
                            i += 1
                        replacmentString += news
                    createdFile.write(line.replace("<!--*content-->", replacmentString))
                    contentFile.close()
            createdFile.close()
