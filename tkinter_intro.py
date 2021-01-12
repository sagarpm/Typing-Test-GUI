from tkinter import *
import random

def file_read():  
  count=0
  para=""
  file=open("paragraph.txt", "r")
  para_dict={}
  i=0

  for line in file:
    para=line[0:-3]
    count=line[-3:-1]
    para_dict[i]=[para,count]
    i+=1
  file.close()
  #print(para_dict)
  return para_dict

word_stat=file_read()
#print(word_stat)
r=random.randint(0,5)

#create root widget
root = Tk()

text_label=Label(root, text=word_stat[r][0])
text_label.grid(row=0,columnspan=3)
text_label.config(wrap=600)

text_area=Entry(root,width=50,borderwidth=5)
text_area.grid(row=1, column=0, pady=10,columnspan=3)

start_button=Button(root,text="Start",bg="green",width=20, height=3)
start_button.grid(row=2,column=0,pady=10,columnspan=1)

end_button=Button(root,text="End",bg="red",width=20, height=3)
end_button.grid(row=2,column=2,pady=10,columnspan=1)

root.mainloop()