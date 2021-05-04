def checkTopicFile(topics):
    filledFiles = []
    for topic in topics:
        with open("DATA/Topics/{}.csv".format(topic)) as Obj:
            Obj.readline()
            if(Obj.readline()):
                filledFiles.append(topic)
    return filledFiles

def stringFormation(val):
    L = len(val)
    number = ""
    for i in range(4-L):
        number += "0"
    number += val
    return number

def topicDataExtraction(topic):
    strings = ["|  #  | Title           |   Run Time       | Difficulty    | Acceptance rate | LeetCode Link |\n",
        "|-----|---------------- |  --------------- | ------------- | ------------- | ------------- |\n"]
    with open("DATA/Topics/{}.csv".format(topic)) as Obj:
        Obj.readline()
        for line in Obj:
            tempLine = line[:-1].split(",")
            tempStr = "|   {}   |   ".format(tempLine[0])
            
            number = stringFormation(tempLine[0])
            difficulty = tempLine[3]
            fileName = "_".join(tempLine[1].lower().split(" "))
            fileName = "{}_{}.py".format(number, fileName)
            
            tempStr += "[{}]({}/{})   |".format(tempLine[1], difficulty, fileName)
            tempStr += "   |   ".join(tempLine[2:5]) + "   |   "
            tempStr += "[Redirect]({})   |\n".format(tempLine[5])
            strings.append(tempStr)
    return strings



Obj = open("DATA/Index.txt", "r")

topicNames = []
for i in range(43):
    topicNames.append(Obj.readline()[:-1])
    
Obj.readline()
mainIndex = Obj.readlines()
Obj.close()


Obj = open("README.md", "w")
Obj.writelines(mainIndex)

topicNames = checkTopicFile(topicNames)

for topic in topicNames:
    Obj.write("# {}\n".format(topic))

    strings = topicDataExtraction(topic)
    for line in strings:
        Obj.write(line)
    
    Obj.write("\n\n\n")
    
Obj.close()


