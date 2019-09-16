import random
masterlist = """Job Class,Percentage
Management,6.1
Business and Financial operations,5
Computer and Mathematical,2.7
Architecture and Engineering,1.7
"Life, Physical and Social Science",0.9
Community and Social Service,1.6
Legal,0.8
"Education, training and library",6.1
"Arts, design, entertainment, sports and media",1.7
Healthcare practioners and technical,5.5
Healthcare support,2.8
Protective service,2.3
Food preparation and serving,8.3
Building and grounds cleaning and maintenance,3.7
Personal care and service,4
Sales,10.2
Office and administrative support,15.1
"Farming, fishing and forestry",0.6
Construction and extraction,4.3
"Installation, maintenance and repair",3.8
Production,6.1
Transportation and material moving,6.5
Total,99.8"""

dict = {}

def makeDictionary():
    listOfLines = []
    i = 0
    prevLine = 0
    while i < len(masterlist):
        if masterlist[i] == '\n':
            listOfLines.append(masterlist[prevLine:i])
            prevLine = i + 1
        i += 1
    listOfLines.append(masterlist[prevLine:len(masterlist)])
    i = 1
    while i < len(listOfLines):
        j = 0
        key = ""
        if listOfLines[i][0] == '\"':
            j += 1
            while listOfLines[i][j] != '\"':
                j += 1
            key = listOfLines[i][1:j]
            j +=1
        else:
            while listOfLines[i][j] != ',':
                j += 1
            key = listOfLines[i][0:j]
        dict.update({key:listOfLines[i][j+1:len(listOfLines[i])]})
        i += 1

makeDictionary()

def returnRandomJob():
    numb = 100 * random.random()
    index = 0.0
    for keys in dict:
        if numb < index + float(dict[keys]):
            return (keys)
        else:
            index += float(dict[keys])

#print (returnRandomJob())
