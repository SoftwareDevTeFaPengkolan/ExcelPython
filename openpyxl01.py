from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "kelas 12 tkj"
sheet["B1"] = "SMKN 2 Cikarang Barat"

workbook.save(filename="hello_world.xlsx")