# THIS IS THE RANDOMIZER
from random import randrange

nofitems = int(input("Enter the number of items: "))
ntodiv = float(input("Enter the float to divide: "))
ranger = input("Enter the range: ")

rangerlist = ranger.split(" ")
final = []

for a in range(nofitems):
    r = float(randrange(int(rangerlist[0]),int(rangerlist[1])))/ntodiv
    final.append(r)

finalstr = ""
for b in range(len(final)):
    if b != len(final)-1:
        finalstr = finalstr + str(final[b]) + "\n"

print(finalstr)

filel = open("input01.txt","w")
filel.write(finalstr)
filel.close()
