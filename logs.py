import os

FILE_LOGS = "./data_files/logs.txt"

def insert_log(section, log):
    if(not os.path.isfile(FILE_LOGS)):
        with open(FILE_LOGS, "w") as file:
            pass
    with open(FILE_LOGS, "a") as file:
        line = "{} >> {}\n".format(section, log)
        file.write(line)

