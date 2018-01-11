import xlwt

wbk = xlwt.Workbook()
sheet=wbk.add_sheet("she1")
sheet.write(0,1,"test adsdf ")
wbk.save('test.xlsx')