import tkinter as tk
from tkinter import ttk
import pandas as pd
import random

fileexel=pd.read_csv("./vocabulary.csv")
kanji=fileexel["kanji"]
hiragana=fileexel["hiragana/katakana"]
persian=fileexel["persian"]
english=fileexel["english"]

window=tk.Tk()

window.config(bg="lightblue")

window.geometry("500x500+500+100")
window.maxsize(500,500)
window.minsize(500,500)

window.title("japanese word")

window.option_add("*font",["arial",25])



def change_word():
    random_row=fileexel.sample()
    random_kanji=random_row["kanji"].to_string(index=False,header=False)
    random_hiragana=random_row["hiragana/katakana"].to_string(index=False,header=False)
    random_persian=random_row["persian"].to_string(index=False,header=False)
    random_english=random_row["english"].to_string(index=False,header=False)
    
    srandom_kanji=random_kanji
    srandom_hiragana= random_hiragana
    srandom_persian=random_persian
    srandom_english=random_english
    
    
    
    next_btn.config(text="next")
    
    word_label.config(text=random_kanji)
    hiragana.config(text=random_hiragana)
    persian.config(text=random_persian)
    english.config(text=random_english)
    
    
titrlabel=tk.Label(window,text="با این برنامه زبان ژاپنی خودت رو تقویت کن")
titrlabel.place(x=30,y=10,width=400,height=50)
titrlabel.config(font="arial,20")

canvas=tk.Canvas(window,bg="yellow")
canvas.place(x=50,y=70,width=400,height=300)

kanji_label=tk.Label(canvas,text="漢字")
kanji_label.place(x=5,y=15)
kanji_label.config(font="arial,10")
word_label=tk.Label(canvas,text="دکمه شروع را بزنید")
word_label.place(x=100,y=10,width=300,height=50)

hiragana_label=tk.Label(canvas,text="هیراگانا")
hiragana_label.place(x=5,y=80)
hiragana_label.config(font="arial,10")
hiragana=tk.Label(canvas,text="هیراگانا")
hiragana.place(x=100,y=70,width=300,height=50)

persian_label=tk.Label(canvas,text="فارسی")
persian_label.place(x=5,y=140)
persian_label.config(font="arial,10")
persian=tk.Label(canvas,text="ترجمه فارسی")


english_label=tk.Label(canvas,text="انگلیسی")
english_label.place(x=5,y=210)
english_label.config(font="arial,10")
english=tk.Label(canvas,text="ترجمه انگلیسی")



persian.place(x=100,y=130,width=300,height=50)
english.place(x=100,y=200,width=300,height=50)


word_label.config(background="orange",height=4,width=20,fg="black")
hiragana.config(background="orange",bd=4)
persian.config(background="orange",font="None,15",bd=4)
english.config(background="orange",bd=4)


next_btn=tk.Button(window,text="شروع",command=change_word)
next_btn.pack(side="bottom",padx=5,pady=5)
next_btn.config(background="orange",bd=2,width=10)


window.mainloop()
