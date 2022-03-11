class text_controls(object):
    def __init__(self):
        self.blabla = ''

    def read_text(self, path):
        txt = open(path, "r")
        txt.close
        return txt
