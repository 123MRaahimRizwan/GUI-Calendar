"""
Project : GUI Calendar
@author : M.Raahim Rizwan
Date Created : 28/09/2021 
"""

# Importing libraries
from tkinter import *
from tkinter import ttk
import calendar

# Basic tkinter setup
window = Tk()
window.title("GUI Calendar")
window.geometry("240x230")
window.wm_iconbitmap("icon.ico")

def show_calendar():
	"""
	Showing calendar
	"""
	month = int(month_spin.get())
	year = int(year_spin.get())
	cal = calendar.month(year, month)
	text_area.delete('1.0', END)
	text_area.insert(INSERT, cal)

# Creating month and year label
year_label = Label(window, text="Year", font="lucida 9 bold").place(x=115, y=0)
month_label = Label(window, text="Month", font="lucida 9 bold").place(x=15, y=0)

# Creating month and year Spinbox
month_spin = ttk.Spinbox(window, values=[i for i in range(13)], width=4)
month_spin.place(x=60, y=0)

year_spin = ttk.Spinbox(window,from_=1899,to=2100, width=4)
year_spin.place(x=150, y=0)

# Creating button
button = ttk.Button(window, text="Show Calendar", command=show_calendar).place(x=75, y=35)

# Creating textarea for showing calendar
text_area = Text(window, width=24, height=8)
text_area.place(x=20, y=66)

window.mainloop()