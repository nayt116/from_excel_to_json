import openpyxl


class Excel_Connection:
    def __init__(self, excel_name:str):
        self.ex_name = excel_name
        self.conn = openpyxl.load_workbook(self.ex_name)