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

    def get_all_file_name_in_folder(self):
        return [f for f in listdir(self.folder) if isfile(join(self.folder, f))]

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