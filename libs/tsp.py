from utils.text_util import text_controls
import random

class travelling_salesman_problen(object):
    def __init__(self):
        self.txt = text_controls()

    def generate_graph_size(self, x, y):
        print(x, y)

    def process_run(self):
        data_pack = self.txt.get_all_file_name_in_folder()
        for file_name, data in data_pack.items():
            node_coord_section = data["NODE_COORD_SECTION"]
            header = data["header"]
            # print(file_name, header)
            for point, coordinates in node_coord_section.items():
                # print(point, coordinates)
                list_coordinates = list(coordinates)

                # skip list out of range
                try: 
                    res = self.generate_graph_size(list_coordinates[0], list_coordinates[1])
                except Exception as e:
                    pass