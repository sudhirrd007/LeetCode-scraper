import os


def insert_log(file_name, section, log):
    if(not os.path.isfile(file_name)):
        with open(file_name, "w") as file:
            pass
    with open(file_name, "a") as file:
        line = "{} >> {}\n".format(section, log)
        file.write(line)

