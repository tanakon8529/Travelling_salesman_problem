from cmath import pi
from turtle import distance
from utils.text_util import text_controls

from pprint import pprint
import random

class travelling_salesman_problen(object):
    def __init__(self):
        self.txt = text_controls()

    def distance_between_point(self, big_num_x1, big_num_y1, big_num_x2, big_num_y2):
        # d^2 = (x2-x1)^2 + (y2-y1)^2
        distance = ( abs(big_num_x2-big_num_x1)^2 + abs(big_num_y2-big_num_y1)^2 )^2
        return distance

    def compare_two_point(self, point1, point2):
        big_num_x1 = int(point1[0])
        big_num_x2 = int(point2[0])

        big_num_y1 = int(point1[1])
        big_num_y2 = int(point2[1])

        return big_num_x1, big_num_y1, big_num_x2, big_num_y2

    def process_run_multi(self):
        data_pack = self.txt.spilt_data_pack()


        for file_name in data_pack:
            current_distance = None
            path_has_been = []
            while len(path_has_been) < 1000:
                inround_distance = 0
                random_data = random.choices(data_pack[file_name], k=len(data_pack[file_name]))

                if random_data not in path_has_been:
                    path_has_been.append(random_data)

                    for point_loop in random_data:
                        current_point = point_loop
                        next_point = data_pack[file_name].index(point_loop)+1

                        if next_point < len(data_pack[file_name]):
                            big_num_x1, big_num_y1, big_num_x2, big_num_y2 = self.compare_two_point(current_point, data_pack[file_name][next_point])
                            distance = self.distance_between_point(big_num_x1, big_num_y1, big_num_x2, big_num_y2)
                            inround_distance += distance
                            current_point = point_loop
                            if current_distance != None:
                                if inround_distance > current_distance:
                                    break
                    
                    if current_distance == None or inround_distance < current_distance:
                        current_distance = inround_distance
                        
            print("{}, current_distance : {} KM, inround_distance : {} KM, total routed : {}".format(file_name, current_distance, inround_distance, len(path_has_been)))



    def process_run_single(self, file_name):
        data_pack = self.txt.spilt_data_pack()

        current_distance = None
        path_has_been = []

        while True:
            inround_distance = 0
            random_data = random.choices(data_pack[file_name], k=len(data_pack[file_name]))

            if random_data not in path_has_been:
                path_has_been.append(random_data)

                for point_loop in random_data:
                    current_point = point_loop
                    next_point = data_pack[file_name].index(point_loop)+1

                    if next_point < len(data_pack[file_name]):
                        big_num_x1, big_num_y1, big_num_x2, big_num_y2 = self.compare_two_point(current_point, data_pack[file_name][next_point])
                        distance = self.distance_between_point(big_num_x1, big_num_y1, big_num_x2, big_num_y2)
                        inround_distance += distance
                        current_point = point_loop
                        if current_distance != None:
                            if inround_distance > current_distance:
                                break
                
                if current_distance == None or inround_distance < current_distance:
                    current_distance = inround_distance
                print("{}, current_distance : {} KM, inround_distance : {} KM, total routed : {}".format(file_name, current_distance, inround_distance, len(path_has_been)))

            
    def process_run(self, file_name, process):
        if process == "Single":
            self.process_run_single(file_name)
        if process == "Multi":
            self.process_run_multi()