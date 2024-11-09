# Append data to the end of sheet - after last existing row

from openpyxl import load_workbook

#Specify the Workbook

wb_add = load_workbook("hello_world.xlsx")

sheet = wb_add["Sheet"]

#convert returned last row to string

ins_row = str(len(sheet['B']) + 1 )

#New row's data

sheet["A"+ins_row] = "Kelas 11 TKJ"

sheet["B"+ins_row] = "SMKN 2 Cikarang Barat"


#Save data in the Workbook

wb_add.save('hello_world.xlsx')