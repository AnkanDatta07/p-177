# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:38:03 2024

@author: Ankan Datta
"""

from tkinter import *
root = Tk()
root.title("Encapsulation")
root.geometry("600x400")

#----Unupdated variables-----#

label_name = Label(root, text = "Name: ", font = ("bold", 15))
label_name.place(relx=0.35, rely = 0.2, anchor = CENTER)

label_name_input = Entry(root)
label_name_input.place(relx=0.5, rely = 0.2, anchor = CENTER)

label_pw = Label(root, text = "Password: ", font = ("bold", 15))
label_pw.place(relx=0.32, rely = 0.3, anchor = CENTER)

label_pw_input = Entry(root)
label_pw_input.place(relx=0.5, rely = 0.3, anchor = CENTER)

label_captcha = Label(root, text = "Captcha: ", font = ("bold", 15))
label_captcha.place(relx=0.33, rely = 0.4, anchor = CENTER)

label_cap_input = Entry(root)
label_cap_input.place(relx=0.5, rely = 0.4, anchor = CENTER)

#------Updated Variables -------#

label_n = Label(root, font = ("bold", 12))
label_n.place(relx= 0.5, rely = 0.6, anchor = CENTER)

label_p = Label(root, font = ("bold", 12))
label_p.place(relx= 0.5, rely = 0.7, anchor = CENTER)

label_c = Label(root, font = ("bold", 12))
label_c.place(relx= 0.5, rely = 0.8, anchor = CENTER)



class userDB():
    def __init__(self):
        self.__username = "Ankan Datta"
        self.__password = "lambo_super137998"
        self.captcha = label_cap_input.get()
        
    def showuser(self):
        label_n['text'] = "Name: " + self.__username
        label_p['text'] = "PassWord: " + self.__password
        label_c['text'] = "Captcha: " + self.captcha
        
user = userDB()

def addUser():
    global user
    user.username = label_name_input.get()
    user.password = label_pw_input.get()
    user.captcha = label_cap_input.get()
    
btn_add = Button(root, text = "Update Login Detals", command = addUser)
btn_add.place(relx = 0.25, rely = 0.5, anchor = CENTER)

btn_show = Button(root, text = "Show profile", command = user.showuser)
btn_show.place(relx = 0.65, rely = 0.5, anchor = CENTER)

root.mainloop()