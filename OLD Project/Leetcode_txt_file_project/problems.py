from tqdm import tqdm
from element_existence import element_existence_check
import os


def fetch_problems_trs_from_webpage(driver):
    # tbody of all problems
    Xpath = '//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[1]'
    element_existence_check(driver, Xpath=Xpath)
    tbody = driver.find_element_by_xpath(Xpath)
    problems_trs = tbody.find_elements_by_tag_name("tr")
    return problems_trs


def fetch_saved_problems_from_file(file_name):
    saved_problems = []
    if(not os.path.isfile(file_name)):
        ## initialize file with header row
        first_line = "#;Title;Difficulty;Acceptance Rate;Runtime;Memory;Tags;Language;Problem Link;Premium\n"
        with open(file_name, "w") as file:
            file.write(first_line)
        return saved_problems
    else:
        with open(file_name, "r") as file:
            file.readline()
            for line in file:
                line = line.split(";")
                # line[0] : problem number
                saved_problems.append(line[0])
        return saved_problems


def check_solved(td):
    try:
        td.find_element_by_tag_name("span")
        return True
    except:
        return False


def fetch_unsaved_problems_trs_from_webpage(driver, file_name):
    saved_problems = fetch_saved_problems_from_file(file_name)
    # trs : list of <tr> of problems
    unsaved_problems_trs = []
    problems_trs = fetch_problems_trs_from_webpage(driver)

    for tr in tqdm(problems_trs):
        # tds : list of <td> elements contain metadata of problem
        tds = tr.find_elements_by_tag_name("td")
        # tds[0] : show solved or unsolved
        if(check_solved(tds[0])):
            # tds[1] : problem number
            problem_number = tds[1].text.strip()
            if(problem_number not in saved_problems):
                unsaved_problems_trs.append(tr)
    return unsaved_problems_trs


def check_premium(td):
    try:
        td.find_element_by_tag_name("span")
        return "1"
    except:
        return "0"


def extract_problem_metadata(problem_tr, METADATA):
    # tds : list of <td> elements contain metadata of problem
    tds = problem_tr.find_elements_by_tag_name("td")
    METADATA["number"] = tds[1].text.strip()
    a = tds[2].find_element_by_tag_name("a")
    METADATA["title"] = a.text.strip()
    METADATA["premium"] = check_premium(tds[2])
    METADATA["problem_link"] = a.get_attribute("href")
    METADATA["acceptance_rate"] = tds[4].text.strip()
    span = tds[5].find_element_by_tag_name("span")
    METADATA["difficulty"] = span.text.strip().upper()
    return METADATA

