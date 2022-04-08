# Ramkhamhaeng University
```
CPE4196 Group :
- 6451000977 tanakon kabprapun
- 6151001556 autthasit sanongsat
- 6251001324 porramin patumrat
- 6251000946 piyaphong nakphan
- 6251000573 Sarawut thepniyom
- 6251000912 Tharathorn Matmueang
```

# required
work on python 3.9.6 (Ubuntu 20.04)

# Quick Start
1. pip install -r requirements.txt
 
2. ***main.py***
--- Select file_name.txt --- 
- gC100_01 to 10
- gC200_01 to 10

--- Select you process ----
- Single
- Multi

```
process = "Multi"
filename = "gC200_03.txt"

tsp = travelling_salesman_problen()
data_pack = tsp.process_run(filename, process)
```
 
3.  ```
    python main.py
    ```
    or
    ```
    python3 main.py
    ```
