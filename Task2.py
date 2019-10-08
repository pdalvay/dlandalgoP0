"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

maxTeleSecs = 0
maxTele = None
teleSecs = dict()
for rec in calls:
    teleSecs.setdefault(rec[0],0)
    teleSecs.setdefault(rec[1],0)    
    teleSecs[rec[0]]+=int(rec[3])
    if maxTeleSecs < teleSecs[rec[0]]:
        maxTeleSecs = teleSecs[rec[0]]
        maxTele = rec[0]
    teleSecs[rec[1]]+=int(rec[3])
    if maxTeleSecs < teleSecs[rec[1]]:
        maxTeleSecs = teleSecs[rec[1]]
        maxTele = rec[1]        

print(maxTele , "spent the longest time", maxTeleSecs ,"seconds, on the phone during September 2016.")