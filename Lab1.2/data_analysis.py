from openpyxl import load_workbook
from matplotlib import pyplot

def getvalue(x):
    return x.value

wb = load_workbook("data_analysis_lab.xlsx")
sheet = wb['Data']
list_x=list(map(getvalue, sheet['A'][1:]))
list_y1=list(map(getvalue, sheet['B'][1:]))
list_y2=list(map(getvalue, sheet['C'][1:]))
pyplot.plot(list_x, list_y1, label="Метка")
pyplot.plot(list_x, list_y2, label="Метка")
pyplot.show()