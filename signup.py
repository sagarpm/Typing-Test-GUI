from tkinter import *

def signup_click():
	global error_message,name,username,password,re_password
	name_val=name.get()
	username_val=username.get()
	password_val=password.get()
	re_password_val=re_password.get()

	if(name_val=='' or username_val=='' or password_val=='' or re_password_val==''):
		error_message.configure(text="Please fill all the details to sign in.")

	#print(name_val)
	#print(username_val)
	#print(password_val)
	#print(re_password_val)

root=Tk()

root.geometry("400x400")
root.configure(bg='#65fc8d')

error_message=Label(root,text='',bg='#65fc8d')

name_label=Label(root,text="Name: ",bg='#65fc8d')
name=Entry(root,borderwidth=5,width=30)

username_label=Label(root,text="Username: ",bg='#65fc8d')
username=Entry(root,borderwidth=5,width=30)

password_label=Label(root,text="Password: ",bg='#65fc8d')
password=Entry(root,show='*',borderwidth=5,width=30)

re_password_label=Label(root,text="Re-Type Password: ",bg='#65fc8d')
re_password=Entry(root,show='*',borderwidth=5,width=30)

submit=Button(root,text='SignUp',command=signup_click)
login_label=Label(root,text="Already have an account? Press LogIn!!!",bg='#65fc8d')
login_button=Button(root,text="LogIn")

error_message.place(x=120,y=75)

name_label.place(x=93,y=100)
name.place(x=150,y=100)

username_label.place(x=72,y=130)
username.place(x=150,y=130)

password_label.place(x=75,y=160)
password.place(x=150,y=160)

re_password_label.place(x=30,y=190)
re_password.place(x=150,y=190)

submit.place(x=275,y=230)
login_label.place(x=55,y=265)
login_button.place(x=275,y=263)
root.mainloop()