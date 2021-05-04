# root file of this project

# author : Sudhir Dhameliya
# github : https://github.com/sudhirrd007


from selenium import webdriver
import time
from os import path
from tqdm import tqdm
import os
from login import make_log_in
from tags import fetch_and_store_tag_names, fetch_problem_tags, update_tags_file
from problems import fetch_unsaved_problems_trs_from_webpage, extract_problem_metadata
from submissions import fetch_submission_metadata, fetch_program, store_program_file, update_metadata_file
from logs import insert_log

FILE_TAG_NAMES = "./files/tags_names.txt"
FILE_PROBLEMS_METADATA = "./files/problems_metadata.txt"
FILE_TAGS = "./files/tags.txt"
FILE_LOGS = "./files/logs.txt"


# starting timestamp
start = time.time()


## replace driver path
DRIVER_PATH = "./drivers/chromedriver"
# DRIVER_PATH = "./drivers/geckodriver"
# DRIVER_PATH = "./drivers/operadriver"


## select below according to driver
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver = webdriver.Firefox(executable_path=DRIVER_PATH)
# driver = webdriver.Opera(executable_path=DRIVER_PATH)


driver.get("https://leetcode.com/accounts/login/")

make_log_in(driver)


flag = input("\nYou want to fetch new tags{1} otherwise {ENTER/0} >> ")
if((flag == "1") or (not os.path.isfile(FILE_TAG_NAMES))):
    fetch_and_store_tag_names(driver, FILE_TAG_NAMES)


flag = input("\nAdd one TAB and press <ENTER> >> ")
handles = driver.window_handles
if(len(handles) == 1):
    input("\nWithout the second TAB, we can not proceeds\nAdd one TAB and press <ENTER> >> ")
    handles = driver.window_handles


unsaved_problems_trs = fetch_unsaved_problems_trs_from_webpage(driver, FILE_PROBLEMS_METADATA)

tags_dict = {}

for problem_tr in unsaved_problems_trs:
    driver.switch_to_window(handles[0])
    # because tab focus is changing
    time.sleep(0.5)

    # will store all the metadata of current problem
    METADATA = {}
    METADATA = extract_problem_metadata(problem_tr, METADATA)

    ## change tab because we need to enter into given problem page
    driver.switch_to_window(handles[1])
    time.sleep(0.5)
    driver.get(METADATA["problem_link"])
    time.sleep(2)

    METADATA = fetch_problem_tags(driver, METADATA)

    METADATA = fetch_submission_metadata(driver, METADATA)

    # open "submission" webpage
    driver.get(METADATA["submission_link"])
    time.sleep(2)

    program_string = fetch_program(driver)

    print(">>> program storing process started\n   do not stop the process  <<<\n")

    store_program_file(program_string, METADATA)
    insert_log(FILE_LOGS, METADATA["number"], "Program stored")

    update_metadata_file(FILE_PROBLEMS_METADATA, METADATA)
    insert_log(FILE_LOGS, METADATA["number"], "metadata stored")

    ## to add problems in "tags.txt" file
    for tag in METADATA["tags"]:
        difficulty = METADATA["difficulty"]
        problem_number = METADATA["number"]
        if(tag not in tags_dict):
            tags_dict[tag] = {difficulty: [problem_number]}
        else:
            if(difficulty not in tags_dict[tag]):
                tags_dict[tag][difficulty] = [problem_number]
            else:
                tags_dict[tag][difficulty].append([problem_number])

    update_tags_file(FILE_TAG_NAMES, FILE_TAGS, tags_dict)
    insert_log(FILE_LOGS, METADATA["number"], "tags has been added")

    print(">> storing process ended <<<\n")

driver.quit()

# ending timestamp
end = time.time()
insert_log(FILE_LOGS, round(end-start,2), "total running time\n\n\n")


