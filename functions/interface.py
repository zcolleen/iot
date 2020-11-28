import tkinter
import PyQt5 as qt


def on_click():
	print("hello from pyqt")


def hello(event):
	print(event)
	button.configure(state="disabled")
	button.update()
	#event.configure(state="disabled")
	#print("hello world")


root = tkinter.Tk()
root.title("intarface")
root.geometry("720x360")
button = tkinter.Button(root, text="click", bg="blue", fg="yellow", state="active",
						activeforeground="yellow")
button.bind("<Button-1>", hello)
button.pack()
root.mainloop()
