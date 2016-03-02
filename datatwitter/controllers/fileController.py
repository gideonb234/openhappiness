# File Controller to handle csv to json conversion and possibly parsing of json/csv files
import json, io, csv, os
from ..models import Dataset
from django.shortcuts import get_object_or_404
from django.core.validators import ValidationError
from open_happy import settings


class FileController:
    def __init__(self):
        return

    def convert_csv_json(self, filepath):
        file_format = self.validate_file_extension(filepath)
        if file_format == "CSV":
            print("convert to json")
        else:
            print("nah")

    def return_file_format(self,file):
        file_format = os.path.splitext(file)[1]
        return file_format

    def open_file(self, file):
        ext = self.validate_file_extension(file)
        if ext == '.json':
            self.open_json(file)
        elif ext == '.csv':
            self.open_csv(file)
        else:
            raise ValidationError(u'File not supported')

    def open_json(self, file):
        f_id = get_object_or_404(Dataset, pk=file)
        f = f_id.file_path.open()
        json_obj = json.loads(f)
        for j_col in json_obj:
            print(j_col)

    def open_csv(self, file):
        f_id = get_object_or_404(Dataset, pk=file)
        f = f_id.file_path.open()
        csvReader = csv.reader(f)
        for row in csvReader:
            print(row)
        return f

    def validate_file_extension(self, file):
        ext = os.path.splitext(file)[1]
        print(ext)
        valid_extensions = ['.csv', '.json']
        if ext not in valid_extensions:
            raise ValidationError(u'File not supported!')
        return ext
