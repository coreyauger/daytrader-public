import os
from os.path import isfile, join
import re 

def loadHtmlMap():
    htmlDict = {}
    htmlFiles = [f for f in os.listdir("./") if ".html" in f]
    for f in htmlFiles:
        with open(f) as x:
            htmlDict[f] = "".join(x.readlines())
    return htmlDict

htmlFileMap = loadHtmlMap()
for (k,v) in htmlFileMap.items():
    regex = re.compile("(.+?(?=<!-- \$))<!-- \$(\w+\.html){ -->(.+?(?=<!-- } -->))",re.DOTALL)
    matches = re.findall(regex,v)
    update = ""
    if len(matches) > 0:
        for g in matches:
            con = htmlFileMap[g[1]]
            update += g[0]+"<!-- $"+g[1]+"{ -->" + con
        update += " <!-- } -->"
        print(update)
        with open(k, "w") as html_file:
            html_file.write(update)
    