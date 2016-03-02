# File Controller to handle csv to json conversion and possibly parsing of json/csv files
import json, io, csv, os
from ..models import Dataset

class FileController:
    def __init__(self):
        return

    def convert_csv_json(self, filepath):
        file_format = self.return_file_format(filepath)
        if file_format == "CSV":
            print("convert to json")
        else:
            print("nah")

    def return_file_format(self,file):
        file_format = os.path.splitext(file)[1]
        return file_format

    def open_file(self, f_id):
        MEDIA_ROOT = '/datatwitter/files'
        f_id = Dataset.objects.get(f_id)
        f = open(os.path.join(f_id.file_path))
        print(f)