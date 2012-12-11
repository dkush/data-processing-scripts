# Dave Kush
#
# Linger to CSV
#
# Takes directory of .dat and .itm files output by Linger and outputs a .csv file

import os
import re



#### modify path names here
path = ""
outputpath = ""

## array positions of question, accuracy scores in raw csvs
## don't modify unless you've already edited the files and changed the position
QuestionPosit = 4
RightAnswerPosit = 6

########################
# the guts are below
# don't modify unless you want to change behavior
#

direct = os.listdir(path)
lines = [] #for storing csv lines


for resfile in direct:
    if resfile[0] != ".":
        if resfile.split(".")[1] != "itm":
            #get .dat file
            f = open(path+resfile,'r')
            #get corresponding .itm file for trial order
            orderfile = open(path+(resfile.split(".")[0])+".itm",'r')
            orderLines = orderfile.readlines()
            itemOrder = 0
            itemNumber = orderLines[itemOrder].split(":")[1]
            for line in f:
                if line.split()[1]!="practice":
                    fItemNo = line.split()[2]
                    #switch itemNumber if new trial encountered in .dat file
                    if fItemNo != itemNumber:
                        itemOrder += 1
                        itemNumber = orderLines[itemOrder].split(":")[1]
                    g = line.split(" ")
                    if g[5][-1] == ",":              # gets rid of double commas 
                        g[5] = g[5][0:-1]            #
                    outputLine = ''
                    for item in g[0:-2]:
                        outputLine = outputLine+str(item)+","
                    outputLine = outputLine + str(g[-2])+","+str(g[-1])
                    outputLine = "s%s,%s" % (outputLine.rstrip(), str(itemOrder))
                    lines.append(outputLine)
            f.close()
            orderfile.close()
            

g = open(outputpath,'w')
accval = 0
#List that'll contain all the new lines once they've had the accuracy val appended to them
accLines = []

#reverse to iterate through the list backwards
lines.reverse()
for line in lines:
    currLine = line.split(",")
    if currLine[QuestionPosit] == "?":               # find the lines that correspond to responses
        accval = currLine[RightAnswerPosit]          # get accuracy for current question
    else:
        accLines.append(line.rstrip()+","+str(accval)+"\n") # for all lines per item, append accuracy on question


# reverse order to obtain original order
accLines.reverse()

#output new file with header :: 'Subject#, ExperimentName,Item#,Condition,wordOrder,word,region,RT,orderOfTrial,Accuracy'
g.write("subj,exp,item,cond,itemOrder,word,reg,RT,testOrder,acc\n")
for line in accLines:
    g.write(line)
    
g.close()