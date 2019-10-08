"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoingCallers = set()
inComingTeles = set()
texters = set()
for rec in calls:
    outgoingCallers.add(rec[0])
    inComingTeles.add(rec[1])

for rec in texts:
    texters.add(rec[0])
    texters.add(rec[1])

removeThese = inComingTeles.union(texters)
outgoingCallers.difference_update(removeThese)

teleMarketers = list(outgoingCallers)
teleMarketers.sort()
print("These numbers could be telemarketers: ")
for tele in teleMarketers:
  print(tele)