# File Controller to handle csv to json conversion and possibly parsing of json/csv files
import json, io, csv

class Dataset:
    def __init__(self, filename, data_type):
        #filename must relate to file path
        self.filename = filename
        self.data_type = data_type
        Dataset.analysed = False

    def isAnalysed(self):
        return Dataset.isAnalysed()