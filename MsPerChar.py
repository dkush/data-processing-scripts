# By Region-Cond Character
# Dave Kush
# Created: 12/12/12
#
# This script takes a .del file used for eye-tracking regioning and returns a .csv file containing the number of characters. by-item/by-region. 
# Useful for merging with larger datafile for computing ms/char RTs when regions differ in length across conditions.
#
# To be included in later one-stop eyetracking processing file


###########################
delpath = "" # location del file 
outpath = "" # name of output file
expname = "" # name of experiment

########################## The guts. 
delfile = open(delpath,'r')
outfile = open(outpath,'w')
outfile.write("exp,cond,item,reg,charlen\n")

def makeLine(expname, regs, currReg):
  preamble = regs[0].split()
	return "%s,%s,%s,%d,%d\n" % (expname, preamble[0], preamble[1], x,len(regs[x]))
	
del_lines = delfile.readlines()

for lin in del_lines:
	regs = lin.split("/")
	for x in range(2,len(regs)-1):
		outfile.write(makeLine(expname,regs,x))

outfile.close()
delfile.close()
