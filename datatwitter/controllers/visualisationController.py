#Handle communication between JS library for Visualisation and the view containing data from comparison controller

class VisualisationController:
    def __init__(self):
        self = "o"

    def getData(self,result):
        return "e"

    def remove_strings_twitter(self,result):
        # go through the array and remove strings from the array to make it clean for the visualisation
        cleaned_indivs = []
        for r in result[3]:
            cleaned_indivs.append([r[0],r[1],r[2]])
        cleaned_result = [result[0], result[1], cleaned_indivs]
        print(cleaned_result)
        return cleaned_result
