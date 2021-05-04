# root file of this project

# author : Sudhir Dhameliya
# github : https://github.com/sudhirrd007

# some notations
# " #NOTCALL " : wouldn't call/import directly into main.py 


import sqlite3
import sys
from selenium import webdriver
import time
from os import path
from tqdm import tqdm
import os
from login import make_log_in
from tags import fetch_and_store_tag_names, fetch_problem_tags, update_TAGS_databse
from problems import fetch_unsaved_problems_trs_from_webpage, extract_problem_metadata
from submissions import fetch_submission_metadata, fetch_program, store_program_file, update_METADATA_databse
from logs import insert_log
from readme_maker import update_readme_file


DATABASE_METADATA = "./data_files/METADATA.db"
DATABASE_TAGS = "./data_files/TAGS.db"


# starting timestamp
start = time.time()

## get problem numbers from user to save time of fetching all problems from webpage
user_unsaved_problems_list = []
string = """\nIf you want to give specific problem number, 
then them with space between them, 
Otherwise press <ENTER> >> """
user_string = input(string)
if(user_string):
    for problem_number in user_string.strip().split(" "):
        try:
            number = int(problem_number.strip())
            user_unsaved_problems_list.append(number)
        except:
            raise Exception("\n??? Terminal Inputs are problematic ???\n")


## add any other browser data when needed
## give driver path
def chrome():
    DRIVER_PATH = "./drivers/chromedriver"
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    return driver
def opera():
    DRIVER_PATH = "./drivers/operadriver"
    driver = webdriver.Opera(executable_path=DRIVER_PATH)
    return driver
def firefox():
    DRIVER_PATH = "./drivers/geckodriver"
    driver = webdriver.Firefox(executable_path=DRIVER_PATH)
    return driver


## comment out all other browser functions
driver = chrome()
# driver = opera()
# driver = firefox()


driver.get("https://leetcode.com/accounts/login/")

# will do login and take us to home page of leetcode website
make_log_in(driver)


flag = input("\nYou want to fetch new tags{1} otherwise {ENTER} >> ")
if(not os.path.isfile(DATABASE_TAGS)):
    fetch_and_store_tag_names(driver, DATABASE_TAGS, first_time=True)
elif(flag == "1"):
    fetch_and_store_tag_names(driver, DATABASE_TAGS, first_time=False)


flag = input("\nAdd one TAB and press <ENTER> >> ")
handles = driver.window_handles
# don't proceed with out second tab
while(len(handles) == 1):
    input("\nWithout the second TAB, we can not proceed\nAdd one TAB and press <ENTER> >> ")
    handles = driver.window_handles


unsaved_problems_trs = fetch_unsaved_problems_trs_from_webpage(driver, DATABASE_METADATA, user_unsaved_problems_list)


for problem_tr in tqdm(unsaved_problems_trs):
    driver.switch_to_window(handles[0])
    # because tab focus is changing
    time.sleep(0.5)

    # will store all the metadata of current problem
    METADATA = {}
    METADATA = extract_problem_metadata(problem_tr, METADATA)

    ## change tab because we need to enter into given problem page
    driver.switch_to_window(handles[1])
    time.sleep(0.5)
    driver.get(METADATA["Problem_link"])
    time.sleep(2)

    METADATA = fetch_problem_tags(driver, METADATA)

    METADATA = fetch_submission_metadata(driver, METADATA)

    # open "submission" webpage
    driver.get(METADATA["Submission_link"])
    time.sleep(2)

    program_string, METADATA = fetch_program(driver, METADATA)

    print(">>> program storing process started\n     do not stop the process.....  <<<\n")

    METADATA = store_program_file(program_string, METADATA)

    update_METADATA_databse(DATABASE_METADATA, METADATA)
    
    update_TAGS_databse(DATABASE_TAGS, METADATA)

    print(">>>>> storing process ended <<<<<\n\n")
    

driver.quit()

# update readme.md file
update_readme_file()


# ending timestamp
end = time.time()
insert_log(round(end-start,2), "total running time\n\n")


