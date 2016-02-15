# File Controller to handle csv to json conversion and possibly parsing of json/csv files
import json, io, csv, os
from ..models import Files

class FileController:
    def __init__(self):
        return

    def convert_csv_json(self, filepath):
        file_format = self.return_file_format(filepath)
        if file_format == "CSV":
            print("convert to json")
        else:
            print("nah")


class File:
    def __init__(self,filename):
        self.filename = filename
        self.filepath = "empty"
        self.analysed = False

    #to fix
    def return_file_format(self,file):
        file_format = os.path._splitext(file)[1]
        print(file_format)
        return file_format

    def set_analysed(self):
        if self.analysed:
            self.analysed = False
        else:
            self.analysed = True

    def set_filename(self, new_name):
        self.filename = new_name
