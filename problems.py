import sqlite3
from tqdm import tqdm
from element_existence import element_existence_check
import os


#############################################################################################################
### Fetch unsaved problems ##################################################################################
#############################################################################################################

def fetch_problems_trs_from_webpage(driver):
    # tbody of all problems
    Xpath = '//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[1]'
    element_existence_check(driver, Xpath=Xpath)
    tbody = driver.find_element_by_xpath(Xpath)
    problems_trs = tbody.find_elements_by_tag_name("tr")
    return problems_trs


def create_METADATA_database(database_file):
    syntax = """
    CREATE TABLE METADATA
    (ID INT PRIMARY KEY NOT NULL,
    Title TEXT NOT NULL,
    Difficulty CHAR(6) NOT NULL,
    Acceptance_rate TEXT NOT NULL,
    Runtime TEXT NOT NULL,
    Memory TEXT NOT NULL,
    Language TEXT NOT NULL,
    Problem_link TEXT NOT NULL,
    Premium INT NOT NULL,
    File_name TEXT NOT NULL,
    Notes TEXT DEFAULT '-' NOT NULL);
    """
    conn = sqlite3.connect(database_file)
    conn.execute(syntax)
    conn.commit()
    conn.close()


def fetch_saved_problems_from_database(database_file):
    saved_problems = []
    if(not os.path.isfile(database_file)):
        create_METADATA_database(database_file)
    else:
        syntax = """SELECT ID FROM METADATA;"""
        conn = sqlite3.connect(database_file)
        cursor = conn.execute(syntax)
        for row in cursor:
            saved_problems.append(row[0])
    return saved_problems
        

def check_solved(td):
    try:
        td.find_element_by_tag_name("span")
        return True
    except:
        return False


def fetch_unsaved_problems_trs_from_webpage(driver, database_file, user_unsaved_problems_list=[]):
    saved_problems = fetch_saved_problems_from_database(database_file)
    unsaved_problems_trs = []

    # trs : list of <tr> of problems
    problems_trs = fetch_problems_trs_from_webpage(driver)

    if(user_unsaved_problems_list):
        problems_trs_TEMP = []
        for problem_number in user_unsaved_problems_list:
            if(problem_number not in saved_problems):
                tr = problems_trs[int(problem_number)-1]
                problems_trs_TEMP.append(tr)
        problems_trs = problems_trs_TEMP

    for tr in tqdm(problems_trs):
        # tds : list of <td> elements contain metadata of problem
        tds = tr.find_elements_by_tag_name("td")
        # tds[0] : show solved or unsolved
        if(check_solved(tds[0])):
            # tds[1] : problem number
            problem_number = int(tds[1].text.strip())
            if(problem_number not in saved_problems):
                unsaved_problems_trs.append(tr) 

    return unsaved_problems_trs


#############################################################################################################
### Fetch Metadata of problems ##################################################################################
#############################################################################################################

def check_premium(td):
    try:
        td.find_element_by_tag_name("span")
        return "1"
    except:
        return "0"


def extract_problem_metadata(problem_tr, METADATA):
    # tds : list of <td> elements contain metadata of problem
    tds = problem_tr.find_elements_by_tag_name("td")
    METADATA["ID"] = tds[1].text.strip()
    a = tds[2].find_element_by_tag_name("a")
    METADATA["Title"] = a.text.strip()
    METADATA["Premium"] = check_premium(tds[2])
    METADATA["Problem_link"] = a.get_attribute("href")
    METADATA["Acceptance_rate"] = tds[4].text.strip()
    span = tds[5].find_element_by_tag_name("span")
    METADATA["Difficulty"] = span.text.strip().upper()
    return METADATA

