#!/usr/bin/python3

from openpyxl import Workbook
from datetime import date

book = Workbook()
sheet = book.active
today = date.today().day
month_no = date.today().month
# rows = [
#     (88, 46, 57),
#     (89, 38, 12),
#     (23, 59, 78),
#     (56, 21, 98),
#     (24, 18, 43),
#     (34, 15, 67)
# ]
day = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
day_no = 2
month = ['jan','feb','march','april','may','june','july','August','September','October','November','December']
flag=1
time = [' ','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30','20:00']
sheet.append(time)
while flag:
	arr = []
	today = today + 1
	date_day = day[day_no] + ' , ' + str(today) + ' ' + month[month_no - 1] + ' ' + '2019'
	# date_day = str(today) + '/0' + str(month_no) + '/2019' 
	arr.append(date_day)
	# for t in time:
	# 	arr.append(t)
	sheet.append(arr)

	if(day_no == 6):
		day_no = 0
	else:
		day_no+=1

	if((month_no==9 or month_no==11 ) and today == 30) or today == 31 :
		today = 0
		month_no+=1
		sheet.append([])

	if (month_no == 13):
		flag=0

book.save('Tech_Discussion_Timeline.xlsx')