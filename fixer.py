#This just reads in the (new!) broken AES corpus, tries to fix the lines
#and then reads it back out into a new file.  That's all folks!

AEStext = open('Brown_ToCode4.csv').read()

import re

#The big problem seems to be a case where a line is quoted (so excel shows
#it fine") and contains a tabbed return.  Happens on long lines for whatever
#reason.  

matcher = re.compile('''(?:\n|\r|\r\n?)\t''', re.MULTILINE)


#making sure it finds what we want...
n = re.findall(matcher, AEStext)
m = re.search(matcher, AEStext)

#Just get rid of those tab sequences!

AEStext = re.sub(matcher,'', AEStext)

#Quotation marks continue to cause problems!! Look for those terrible
#lines that start with @, either alone on their lines or petering out in a ".

####Alone on a line
matcher2 = re.compile('''(?:\n|\r|\r\n?)@[^,]+(?:\n|\r|\r\n?)''', re.MULTILINE)

#making sure it finds what we want...
n = re.findall(matcher2, AEStext)

#And get rid of this!  Leave behind just the return that started the sequence...

AEStext = re.sub(matcher2,'\n',AEStext)

####Now we try to catch the quoted parts...

matcher3 = re.compile('''\"[^\"]+(?:\n|\r|\r\n?)@[^\"]+\"''', re.MULTILINE)

#making sure it finds what we want...
n = re.findall(matcher3, AEStext)

#And get rid of them!  Here we carefully preserve the stuff that was on the first
#line before the badness...

def myrepl3(matchobj):
    brokesection = matchobj.group(0)
    tokeep = brokesection.splitlines()[0] #grabs the first line!
    tokeep = tokeep.lstrip('"') #but take off that quotation mark!
    return tokeep #these breaks seem to happen in the middle of lines...


AEStext = re.sub(matcher3,myrepl3,AEStext)


##########################
#and check that it's all fixed!

AESlines = AEStext.splitlines()
len(AESlines)
broken = 0
fixed = 0
for i in range(1,len(AESlines)):
    numfind = re.match('[0-9]+', AESlines[i]) #Every line should start witha  number!
    stringnum = numfind.group(0)
    if stringnum == str(i):
        fixed = i
        continue
    else:
        broken = i
        break


##########################
#Wohoo!  Read it out!

open('Brownfixed.csv','w').write(AEStext)

#Open up again and check for misaligned columns!

import csv
csvcheck = csv.reader(open('Brownfixed82.csv', 'rb'), delimiter=',', quotechar='"')

broken = 0
fixed = 0
brokenlist = []
for row in csvcheck:
    if row[0] == 'Line.Number':
        print 'got here'
        continue
    if row[12] == 'TRUE':
        fixed = row[0]
        continue
    elif row[12] == 'FALSE':
        fixed = row[0]
        continue
    else:
        broken = row[0]
        print broken
        brokenlist.append(broken)
        continue

