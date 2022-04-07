from settings.configs import PATH_RESOURCE_FILE
from os import listdir
from os.path import isfile, join

class text_controls(object):
    def __init__(self):
        self.blabla = ''
        self.folder = PATH_RESOURCE_FILE

    def read_text(self, path):
        file = open(path, "r")
        text_file = file.read()
        file.close
        return text_file

    def convert_txt_to_json(self, name_file):
        txt_file = self.read_text(self.folder+name_file)
        pack_res = txt_file.splitlines()
        line_header_pack = []
        # loop header
        for line in pack_res:
            if " : " in line:
                line_header_pack.append(line.split(" : "))

        # loop NODE_COORD_SECTION
        pack_data = {}
        pack_node = {}
        for line in pack_res:
            if pack_res.index(line) > 5:
                in_line = line.split(" ")
                pack_node[in_line[0]] = {in_line[1], in_line[2]}

        pack_data["NODE_COORD_SECTION"] = pack_node
            
        pack_header = {}
        for item in line_header_pack:
            pack_header[item[0]] = item[1]
            if item[0] == "COMMENT":
                in_item = item[1].split(", ")
                N = in_item[0].split("=")
                seed = in_item[1].split("=")
                pack_header[item[0]] = {"N" : N[1], "seed" : seed[1]}
    
        return pack_header, pack_data

    def get_all_filename_and_data_in_folder(self):
        all_file_name = [f for f in listdir(self.folder) if isfile(join(self.folder, f))]
        data_pack = {}
        for files_name in all_file_name:
            pack_header, pack_data = self.convert_txt_to_json(files_name)
            pack_data["header"] = pack_header
            data_pack[files_name] = pack_data
        return data_pack

    def spilt_data_pack(self):
        data_pack = self.get_all_filename_and_data_in_folder()

        data_pack_spilt = {}
        list_coordinates_pack = []
        for file_name, data in data_pack.items():
            node_coord_section = data["NODE_COORD_SECTION"]
            for order_point, point in node_coord_section.items():
                list_coordinates = list(point)
                list_coordinates_pack.append(list_coordinates)
            data_pack_spilt[file_name] = list_coordinates_pack

        return data_pack_spilt
