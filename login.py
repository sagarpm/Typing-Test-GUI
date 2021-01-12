from tkinter import *

def login_click():
	global username_entry, password_entry, error_message
	#all that was needed to get it work was declaring global for entry widgets(works without bind also).
	username='a'
	password='a'
	username_text=username_entry.get()
	password_text=password_entry.get()
	print("u "+username_text)
	print("p "+password_text)
	if(username_text!=username or password_text!=password):
		error_message.configure(text='Username or Password is wrong!!!')
		error_message.place(x=100,y=105)
	#else:
	#	error_message.configure(text='Valid User')
	#	error_message.place(x=150,y=105)

root=Tk()
#Setting the size of the window visible initially.
root.geometry("400x400")
root.configure(bg='#65fc8d')

#in case the user enters wrong password or username.
error_message=Label(root,text='',bg='#65fc8d')

#username label and entry.
user_text=Label(root,text="Username:",padx=10,bg='#65fc8d')
username_entry=Entry(root,borderwidth=5,width=30)

#password label and entry.
password_text=Label(root,text="Password: ",padx=10,bg='#65fc8d')
password_entry=Entry(root,borderwidth=5,show='*',width=30)

#login button.
submit=Button(root,text='LogIn',command=login_click)

#user signup message and button.
signup_message=Label(root,text="*Not a member? click SignUp!",bg='#65fc8d')
signup=Button(root,text='SignUp')

#placement of the widgets on the screen.
user_text.place(x=100,y=150,anchor=CENTER)
username_entry.place(x=240,y=150,anchor=CENTER)
#username_entry.bind("<Return>", lambda event: login_click())#only binding here but still getting the value for password as well.
password_text.place(x=100,y=190,anchor=CENTER)
password_entry.place(x=240,y=190,anchor=CENTER)
submit.place(x=280,y=220)
signup_message.place(x=100,y=250)
signup.place(x=160,y=275)

#loop that keeps the main window alive.
root.mainloop()