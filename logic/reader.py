import random
import openpyxl
import csv


# ---------------------------------------------------------------------------- #
#                                    Reader                                    #
# ---------------------------------------------------------------------------- #
class Reader:
    def __init__(self):
        self.list = []
        
        
    def readXlsx(self, xlsx_name: str) -> None:
        # Open the xlsx file
        workbook = openpyxl.load_workbook(filename=xlsx_name, read_only=True, data_only=True)
        sheet = workbook.active
        
        for row in sheet.iter_rows(values_only=True):
            question = str(row[0])
            answer = str(row[1])
            self.list.append((question, answer))
            
            
    def readCSV(self, csv_name: str) -> None:
        # Find the delimiter used in the csv file
        with open(csv_name, 'r', newline='', encoding='utf-8') as csvfile:
            # read the first 1024 bytes to detect the delimiter
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
        custom_delimiter = dialect.delimiter   
        
        # Open the csv file with the detected delimiter
        with open(csv_name, "r", newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=custom_delimiter)
        for row in reader:
            question = row[0]
            answer = row[1]
            self.list.append((question, answer))
        
        
    def cutQuestions(self, begin: int, end: int) -> None:
        self.list = self.list[begin:end]
    
    def shuffle(self) -> None:
        random.shuffle(self.list)
            
    def getQuestion(self, index: int) -> str:
        return self.list[index][0]
    
    def getAnswer(self, index: int) -> str:
        return self.list[index][1]
    
    def getLength(self) -> int:
        return len(self.list)

