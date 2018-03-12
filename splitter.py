# This reads in brownfixed.csv and splits it up into a set of files so that
# they can be opened more easily.

import re

AEStext = open('brownfixed.csv').readlines()
header = AEStext[0].splitlines()[0]

#Add the extra coding columns!  Put whatever headers you want.
header = "Line.Number" + header + ",VerbCheck,Imperative,Repetition,Comments\n"



filename_matcher = re.compile('Brown/Brown/[A-Za-z]+/[a-z0-9]+.cha')
filename_grabber = re.compile('[a-z]+[0-9]+')

last_sess_name = ''
session_counter = 0
sess_start = ''
sess_end = ''
index_start = 0
index_end = 0
for i in range(1,len(AEStext)):
    fields = AEStext[i].split(',')
    session = fields[6]

    #Get the session label.  If it's a dud line, skip to the next line
    try:
        sess_name = re.match(filename_matcher, session).group(0)
    except AttributeError:
        sess_name = last_sess_name

    #Did we find a new session label?
    if sess_name == last_sess_name:
        continue #Nope
    
    else: #Yep
        session_counter += 1

        #If it's a new label, take care of recording labels and emitting shortfiles.  Note this only actually happens on the first round through...
        if session_counter == 1:
            
            #Record starting locations
            sess_start = re.search(filename_grabber, sess_name).group(0)
            index_start = i


            
        elif session_counter == 4: #we ate 3 files, this is the first line of the fourth one

            #Record ending locations
            sess_end = re.search(filename_grabber, last_sess_name).group(0)
            index_end = i-1

            #Make next shortfile
            next_shortfilename = 'Brown_' + sess_start + '_' + sess_end +'.csv'
            
            print next_shortfilename
            print index_start
            print index_end

            #lines to print out

            shortfile_lines = AEStext[index_start:index_end+1]
            shortfile_lines.insert(0, header)

            f = open(next_shortfilename, 'w')
            f.write(''.join(shortfile_lines))
            f.close()

            #Reindex everything to continue on!
            session_counter = 1
            sess_start = re.search(filename_grabber, sess_name).group(0)
            index_start = i

            
        #and keep going
        last_sess_name = sess_name


#Error!  Print out the last filename in case we didn't end on an even number!

sess_end = re.search(filename_grabber, sess_name).group(0)
index_end = i
next_shortfilename = 'Brown_' + sess_start + '_' + sess_end +'.csv'
print next_shortfilename
print index_start
print index_end


#lines to print out
shortfile_lines = AEStext[index_start:index_end+1]
shortfile_lines.insert(0, header)

f = open(next_shortfilename, 'w')
f.write(''.join(shortfile_lines))
f.close()

    
