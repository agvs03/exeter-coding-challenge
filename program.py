import csv

import time
import os, psutil
from humanfriendly import format_timespan
from collections import OrderedDict
start= time.time()
dicfile = open("french_dictionary.csv","r")
#Retrieve all english and french words from csv and stroring it in dict{}
mydic={}
for i in dicfile:
    currenti=i.rstrip("\n").split(',')
    mydic[currenti[0]]=currenti[1]
frequency = {}
sourcefile = open( 't8.shakespeare.txt', 'r+' )
tempfile=open( 't8.shakespeare.translated.txt', 'w' )

#Fetch each i from sourcefile.
for i in sourcefile:
    #Fetch each word from i.
    for word in i.split(' '):
      #Check whether the word is in mydict{} and not equal to new i.
      if word!='\n' and word in mydic.keys():
          #Write corresponding french word in tempfile using dictionary keys.
          tempfile.write(mydic[word]+" ")
          #check whether the word is in frequency{} and iterate it.
          if word in frequency:
            frequency[word]+=1
          #If not set the key value as "1".
          else:
            frequency[word]=1
      #If word not in mydict{}, write the word. 
      else:
        tempfile.write(word+" ")

tempfile.close()

#Sort the frequency{} in ascending order.
occurence = OrderedDict(sorted(frequency.items()))

csvwriter=open("frequency.csv","w")
freq=csv.writer(csvwriter)
freq.writerow(['English word','French word','Frequency'])

#write the frequency of each translated word in csv
for key in list(occurence.keys()):
    freq.writerow([key,mydic[key],occurence[key]])
csvwriter.close()
end=time.time()


#calculate time taken and memory used
str1="Time to process: "+format_timespan(end-start)
str2="Memory used: "+str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)+" MB"

with open("performance.txt","w") as per:
    per.write(str1+"\n"+str2)




