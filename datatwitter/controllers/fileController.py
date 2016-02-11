# File Controller to handle csv to json conversion and possibly parsing of json/csv files
import json, io, csv, os

class FileController:
    def __init__(self, filename, filepath):
        # filename must relate to file path
        self.filename = filename
        self.filepath = filepath
        self.analysed = False

    def return_file_format(self,file):
        file_format = os.path._splitext(file)[1]
        print(file_format)
        return file_format

    def set_analysed(self):
        if self.analysed:
            self.analysed = False
        else:
            self.analysed = True

    def convert_csv_json(self, filepath):
        file_format = self.return_file_format(filepath)
        if file_format == "CSV":
            print("convert to json")
        else:
            print("nah")

    def handle_file_upload(self, file):
        with open('some/file/' + file, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)