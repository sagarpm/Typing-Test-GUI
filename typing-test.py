from tkinter import *
import time

root = Tk()
root.title("Speed Test")
t0 = t1= None
started = False
def start():
    global t0, started, e, duration_label, accuracy_label, wpm_label
    if started:
        return

    started = True
    e.config(state='normal')
    e.delete(0, END)
    duration_label.config(text = " ")
    accuracy_label.config(text = " ")
    wpm_label.config(text= " ")

    t0 = time.time()

def end():
    global t1, duration_label, e, started
    if not started:
        return

    started = False
    t1 = time.time()
    e.config(state='disabled')
    input_string = e.get()
    accuracy_label.config(text = "Accuracy: xyz %")
    wpm_label.config(text="Speed: xyz WPM")
    duration_label.config(text = "Duration: " + str(round(t1-t0,2)) + " seconds")


# Create input text-box and the start and end button
para = Label(root, width=70, wraplengt=400, text="some para for now, actually this \none is huge yk like very very "
                                                 "big. Don't you dare open this. Well let's just keep going and see "
                                                 "what happens yk. I mean the main thing is that I want to test the "
                                                 "length of the para nad all so this will come in handy.",
             font="Arial 9")
e = Entry(root, width=70, bd=5, text="Press start then start typing here...", state='disabled')
start_button = Button(root, text="Start", padx=20, pady=10, bg="#a4c789",command=start)
end_button = Button(root, text="End", padx=20, pady=10, bg ="#d16262", command=end)

# Put the start and end button on the screen
para.grid(row=0, columnspan=3)
e.grid(row=1, column=0, columnspan=3)
e.bind("<Return>", lambda event: end())
start_button.grid(row=2, column=0, columnspan=1)
end_button.grid(row=2, column=2, columnspan = 1)

# Create three labels for the result
accuracy_label = Label(root, text=" ", font = "Verdana 10 bold")
wpm_label = Label(root, text=" ", font = "Verdana 10 bold")
duration_label = Label(root, text=" ", font = "Verdana 10 bold")

# Put the result labels on the screen (currrently empty)
accuracy_label.grid(row=3, column=0)
wpm_label.grid(row=3, column=1)
duration_label.grid(row=3, column=2)

root.mainloop()
