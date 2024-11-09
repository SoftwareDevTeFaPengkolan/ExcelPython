import tkinter as tk
from tkinter import simpledialog as sd

# Append data to the end of sheet - after last existing row

from openpyxl import load_workbook

root=tk.Tk()
word1=sd.askstring('word', 'kelas ?')
if not word1:
    exit()
word2=sd.askstring('word', 'asal sekolah ?')


#Specify the Workbook

wb_add = load_workbook("hello_world.xlsx")

sheet = wb_add["Sheet"]

#convert returned last row to string

ins_row = str(len(sheet['B']) + 1 )

#New row's data

sheet["A"+ins_row] = word1

sheet["B"+ins_row] = word2


#Save data in the Workbook

wb_add.save('hello_world.xlsx')

root.mainloop()