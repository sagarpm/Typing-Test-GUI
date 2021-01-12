def remove_char(sentence):
	new_sentence=''
	for i in range(len(sentence)):
		if(sentence[i]=='.'):
			if(i==len(sentence)-1):
				continue
			else:
				new_sentence+=' '
		elif(sentence[i]==','):
			new_sentence+=''
		else:
			new_sentence+=sentence[i]
	return new_sentence

def word_count(sentence):
	sentence=remove_char(sentence)
	count=0
	words_d=[]
	word=''
	for i in range(len(sentence)):
		if(sentence[i]!=' ' and sentence[i]!='.' and sentence[i]!=','):
			word+=sentence[i]
		elif((sentence[i]==' ' or sentence[i]=='.' or sentence[i]==',') and word!=''):
			words_d.append(word)
			word=''
			count+=1
	return count+1 #+1 because the last word will end and we will not know because the . is removed.