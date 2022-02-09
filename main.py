from tkinter import *
# from tkinter import all^^


def button_clicked():
    print("I got clicked!")
    new_text = user_input.get()
    my_label.config(text=new_text)


# create window:
window = Tk()
window.title("Hello TK!")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# create and modify labels:
my_label = Label(text="I am a label.", font=("Times New Roman", 30, "italic"))
# 2 diff ways to do same thing:
my_label.config(text="New Text.")
my_label["text"] = "New Text."
my_label.grid(column=0, row=0)
my_label.config(padx=5, pady=5)


# buttons:
button = Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1)
button2 = Button(text="New button!")
button2.grid(column=2, row=0)


# entry:
user_input = Entry(width=10)
print(user_input.get())
user_input.grid(column=3, row=2)


window.mainloop()
