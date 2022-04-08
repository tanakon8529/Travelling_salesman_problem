from libs.tsp import travelling_salesman_problen

# process problem
# gC100_01 to 10
# gC200_01 to 10

# Single or Multi Process Select
# - Single
# - Multi

process = "Multi"
filename = "gC200_03.txt"

tsp = travelling_salesman_problen()
data_pack = tsp.process_run(filename, process)