#REZA ABIRI

import translate_mdl
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("495x240+450+260")
root.title("Translator")

Translator = translate_mdl.Translator()


title_top = Label(root, text='Welcome to Translate', font='aria 15 bold')
title_top.pack()

input_text = ttk.Entry(root,width=40, font='aria 13 bold', justify='center')
input_text.pack(side=TOP, ipady=5)

Show_txt = Label(root, text = 'Translated text', font='aria 12 bold', fg='blue')
Show_txt.pack(side=TOP, ipady=20)


var = IntVar()
persian_to_english = ttk.Radiobutton(root, text='Persian to English', variable=var, value=1)
persian_to_english.place(x=250, y=180)
english_to_persian = ttk.Radiobutton(root, text='English to Persian', variable=var, value=2)
english_to_persian.place(x=130, y=180)

var.set(2)


def show():

    target = int(var.get())
    if target == 1:
        txt = Translator.translate(str(input_text.get()), 'fa', 'en')
    else:
        txt = Translator.translate(str(input_text.get()), 'en', 'fa')

    Show_txt.config(text=txt)

translate = ttk.Button(root, text = 'Translate', command=show, width=40)
translate.pack()

root.mainloop()


