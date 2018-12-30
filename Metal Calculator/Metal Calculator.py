#! /usr/bin/python
# TODO: Pull metal Prices from Kitco -DONE
# TODO: send prices to calculations
# TODO: allow user to set formula
# TODO: allow user to edit formula
# TODO: create a folder to save Prices
# TODO: everyday generates a txt file for that days prices based on the formula
#       provided by the user
from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import font
import tkinter as Tk, re

import datetime, time
#Front end
class MetalWindow(Tk.Tk):
    def __init__(self):
        Tk.Tk.__init__(self)
        self.title('Metal Calculator')
        self.winGeometry()
        calc = Calculations()
        calc.__init__()
        self.winGeometry()
        self.priceDisplay(calc)

    def winGeometry(self):
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = ws-200
        y = hs-600
        self.geometry('%dx%d+%d+%d'%(250,250,x,y))
    def priceDisplay(self,cal):
        winFont = font.Font(family='Times New Roman',size=13)
        displayText = Text(self, width=45, height=20)
        displayText.configure(font=winFont)
        displayText.insert(END,"Today's prices are:\n ")
        displayText.insert(END,"Gold: %d Plat: %d \n"% (float(cal.gold), float(cal.plat)))
        displayText.insert(END,"18w: %.2f\n"% (float(cal.m18w)))
        displayText.insert(END,"14w: %.2f\n"% (float(cal.m14w)))
        displayText.insert(END,"18y: %.2f\n"% (float(cal.m18y)))
        displayText.insert(END,"14y: %.2f\n"% (float(cal.m14y)))
        displayText.pack()
#Back end
class Calculations():
    def __init__(self):
        page = requests.get("http://www.kitco.com/market/")
        soup = BeautifulSoup(page.content,'html.parser')
        self.gold = soup.find(id="AU-high").get_text()
        self.plat = soup.find(id="PT-high").get_text()
        self.silver = 3
        self.metal18k = 26.66
        self.metal14k = 34.18
        self.m18w = (float(self.gold)+3+320)/self.metal18k
        self.m14w = (float(self.gold)+3+320)/self.metal14k
        self.m18y = (float(self.gold)+3+215)/self.metal18k
        self.m14y = (float(self.gold)+3+215)/self.metal14k
    def whiteCal(self,metal):
        return str((self.gold+3+320)/metal)
    def yellowCal(self,metal):
        return str((self.gold+3+215)/metal)

if __name__ == '__main__':
    main = MetalWindow()
    main.mainloop()
