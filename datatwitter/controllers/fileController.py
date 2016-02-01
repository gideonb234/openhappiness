# File Controller to handle csv to json conversion and possibly parsing of json/csv files
import json, io, csv, os

class Dataset:
    def __init__(self, filename, data_type):
        # filename must relate to file path
        self.filename = filename
        self.data_type = data_type
        self.analysed = False

    def return_file_format(self,file):
        fileFormat = os.path._splitext(file)[1]

    def set_analysed(self):
        if self.analysed:
            self.analysed = False
        else:
            self.analysed = True


