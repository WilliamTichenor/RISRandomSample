import sys
import os
import random
import rispy


fpath = sys.argv[1]
with open(fpath, 'r', encoding="utf-8-sig") as dataFile:
    data = rispy.load(dataFile)
    outputContent = []
    totalNum = len(data)
    samples = int(sys.argv[2])
    if (samples>totalNum):
        samples = totalNum
    print("Num Samples: "+str(samples))
    print("Total Entries: "+str(totalNum))
    for i in range(samples):
        randIndex = random.randrange(0,totalNum-i)
        outputContent.append(data[randIndex])
        data.pop(randIndex)
    print(str(len(outputContent))+" Entries")
    os.makedirs("output", exist_ok = True)
    outpath = 'output/output.ris'
    with open(outpath, 'w', encoding="utf-8-sig") as dataFile:
        rispy.dump(outputContent, dataFile)