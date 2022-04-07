from utils.text_util import text_controls

from pprint import pprint
import random

class travelling_salesman_problen(object):
    def __init__(self):
        self.txt = text_controls()

    def distance_between_point(self, point1, point2):
        # d^2 = (x2-x1)^2 + (y2-y1)^2
        distance = ( (point2[0]-point1[0])^2 + (point2[1]-point1[1])^2 )^2
        print(distance)

    def process_run(self):
        data_pack = self.txt.spilt_data_pack()
        for order, data in data_pack.items():
            # print(order, data)
            init_point = random.choice(data)
            for point in data:
                print(point)
            