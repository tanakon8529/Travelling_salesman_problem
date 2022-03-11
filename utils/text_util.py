class text_controls(object):
    def __init__(self):
        self.blabla = ''

    def read_text(self, path):
        file = open(path, "r")
        text_file = file.read()
        file.close
        return text_file
