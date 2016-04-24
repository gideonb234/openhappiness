# File Controller to handle csv to json conversion and possibly parsing of json/csv files
import json, io, csv, os
from ..models import Dataset
from django.shortcuts import get_object_or_404
from django.core.validators import ValidationError
from open_happy import settings


class FileController:
    def __init__(self):
        return
    # Return the file format of the file given
    def return_file_format(self,file):
        file_format = os.path.splitext(file)[1]
        return file_format
    # Open file if csv or json
    def open_file(self, file, saved_file):
        ext = self.validate_file_extension(file.name)
        if ext == '.json':
            f_id = get_object_or_404(Dataset, pk=saved_file)
            print(type(f_id.file_path))
            with open(f_id.file_path.path) as f:
                data = json.load(f)
            for j_col in data:
                print(j_col)
            return data
        elif ext == '.csv':
            f_id = get_object_or_404(Dataset, pk=saved_file)
            with open(f_id.file_path.path) as f:
                csvReader = csv.reader(f)
                print(csvReader)
            return csvReader
        else:
            raise ValidationError(u'File not supported')

    # open file based on id (must be json file)
    def open_file_id(self, saved_file):
        f_id = get_object_or_404(Dataset, pk=saved_file)
        print(type(f_id.file_path))
        with open(f_id.file_path.path) as f:
            data = json.load(f)
        for j_col in data:
            print(j_col)
        return data

    # Return true if file is csv/json else return false
    def validate_file_extension(self, file):
        ext = os.path.splitext(file)[1]
        print(ext)
        valid_extensions = ['.csv', '.json']
        if ext not in valid_extensions:
            raise ValidationError(u'File not supported!')
        return ext