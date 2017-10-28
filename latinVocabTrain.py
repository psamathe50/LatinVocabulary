# cd <your directory path to get to this file>
import csv
import re
pattern=re.compile('^[1-4]{1}$')
#reads the csv file and separates within each line the elements by :
wbookReader=csv.reader(open('LatinVocab.txt'), delimiter=':')
myDict={}
#makes a dictionary between the latin word and the corresponding English translation
for line in wbookReader:
    if len(line)>1:
     myDict[line[0]]=line[1]
words=list(myDict)
L=len(words)
import numpy as np
frq=np.zeros(L)
succ=np.zeros(L)
score=(succ+1)/(frq+L) # We start with 1/L when there is no information

prob=score/sum(score)
#badlist is the list that keeps updating based on words that are answered incorrectly
badList=[]
#lowlist collects words consistently answered incorrect
lowList=[]
#merges badlist and lowlist together for the final list of words to work on
report=[]
while True :
	inds=np.random.choice(L, 4, replace=False,p=prob)
	indl=inds.tolist()
	if(len(badList)>0):
		#chooses to return to bad words when random number generated less than .2
		if np.random.uniform()<.2:
			c1=badList.pop(0)
			indl[0]=c1
    	  
    
    
	ord=np.random.permutation(4)
	w=words[indl[0]]
	c=indl[0]
	print(w)
	frq[c]+=1
	j=0
	for i in ord:
		j=j+1
		print(repr(j)+' '+myDict[words[indl[i]]])
	print("Choose 1-4 or q to quit or hit return to continue")

	ans = input()
  	#when the user decides to quit the program 
	if ans == "q" :
		print(w+' '+myDict[w])
		score=(succ+1)/(frq+L) 
		for i in range(L): 
			if (score[i]<1/L): 
				lowList.append(i)
		if(len(badList)>0):
			for j in badList: 
				report.append(words[j])
		if(len(lowList)>0):
			for k in lowList: 
				report.append(words[k])
		print(report)
		break
	 
	if (bool(pattern.match(ans)) is False or (ord[int(ans)-1]!=0)):
		print('Sorry, you are incorrect. This is the correct answer: ')
		print(w+' '+myDict[w])
		if (c in badList) is False:
			badList.append(c)
	else:
		if (bool(pattern.match(ans)) & (ord[int(ans)-1]==0)):
			print('Correct!')  
			succ[c]+=1   

