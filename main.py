from elopy import *
import xlrd



i = Implementation()

i.addPlayer("Ming Fong")
i.addPlayer("Ainsley Lai")

print(i.getRatingList())

i.recordMatch("Ming Fong", "Ainsley Lai", winner="Ming Fong")

print(i.getRatingList())

#read from a spreadsheet or SQL table
file = ("Log.xlsx")
wb = xlrd.open_workbook(file)
sheet = wb.sheet_by_index(0)
#calculate elo while reading
a = 1
player_list = i.getRatingList()
while (sheet.cell_value(a, 0) != None):
    for x in player_list:
        if(sheet.cell_value(a, 0) == x):
            break
        else:
            break

#return list of players and elo

#display on a webpage
