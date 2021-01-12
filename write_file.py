from utilities import remove_char
from utilities import word_count

def file_enter(paragraph,count):
	file=open("paragraph.txt","a")
	file.write(paragraph)
	#file.write("\n")
	file.write(str(count))
	file.write("\n")
	file.close()

print("Enter the paragraph :")
paragraph=input()
paragraph=remove_char(paragraph)
words=word_count(paragraph)
file_enter(paragraph,words)