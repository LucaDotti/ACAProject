import os as Os

def parseGeneralResult(line):
    endValueIndex = line.find("#") - 1
    line = line[0:endValueIndex]
    startValueIndex = line.rfind(" ")
    line = line[startValueIndex+1:]
    print line
    
stream = Os.popen("/home/lab/simplescalar/pisa/simplesim/sim-profile -iprof bin/rawcaudio < data/small.pcm &> output.txt")
f = open("output.txt", "r")

content = f.read()

resultsIndex = content.find("sim: ** simulation statistics **")
content = content[resultsIndex:]
lines = content.split("\n")

results = []
parseGeneralResult(lines[1])
#for line in lines:
#  if line.startswith("sim_num_insn"):
#    results.append()


f.close()