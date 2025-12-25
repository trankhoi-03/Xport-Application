from win32com.client import Dispatch

def export_image():
    app = Dispatch("Excel.Application")
    workbook_file_name = r"D:\learn\Programming\Robot\data\Book1.xlsx"
    workbook = app.Workbooks.Open(workbook_file_name)

    app.DisplayAlerts = False

    i = 1
    for sheet in workbook.Worksheets:
        for chartObject in sheet.ChartObjects():
            print(sheet.Name + ':' + chartObject.Name)
            chartObject.Chart.Export(r"D:\learn\Programming\Robot\data\chart" + str(i) + ".png")
            i += 1
        
    workbook.Close(SaveChanges=False, Filename=workbook_file_name)


export_image()