import openpyxl
from openpyxl.chart import BarChart, Reference, Series
wb=openpyxl.load_workbook(r"C:\Users\carj\Desktop\example.xlsx")
py=wb['Veggies']
for i in range(1,11):
    py["A"+str(i)]=i
values = Reference(py, min_col=1, min_row=1, max_col=1, max_row=10)
chart=BarChart()
chart.add_data(values)
py.add_chart(chart, "D1")
wb.save(r"C:\Users\carj\Desktop\example.xlsx")
    