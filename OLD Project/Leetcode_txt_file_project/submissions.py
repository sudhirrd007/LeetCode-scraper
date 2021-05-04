import time
from element_existence import element_existence_check


# for now this only fetch the latest submission
# modify it to fetch all submission later
def fetch_submission_trs(driver):
    Xpath = '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[4]'
    driver.find_element_by_xpath(Xpath).click()
    time.sleep(0.5)

    # first submission Xpath
    Xpath = '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[5]/div/div/div/div/div/div/div/div/div/table/tbody/tr[1]'
    return driver.find_element_by_xpath(Xpath)


# if function "fetch_submission_trs(driver)" will change that this function also need to be changed
def fetch_submission_metadata(driver, METADATA):
    submission_tr = fetch_submission_trs(driver)
    # <td> of metadata elements
    tds = submission_tr.find_elements_by_tag_name("td")
    METADATA["submission_link"] = tds[1].find_element_by_tag_name("a").get_attribute("href")
    METADATA["runtime"] = tds[2].text
    METADATA["memory"] = tds[3].text
    METADATA["language"] = tds[4].text
    return METADATA

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

# fetch "unstructured" program
def fetch_raw_program(driver):
    # "edit code" button
    Xpath = '//*[@id="edit-code-btn"]'
    element_existence_check(driver, Xpath=Xpath, init_wait=0.3)
    driver.find_element_by_xpath(Xpath).click()
    #> after clicking we will redirected to another webpage but will remain in the same window

    # textbox
    Xpath = '//*[@id="app"]/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[6]/div[1]/div/div/div/div[5]'
    element_existence_check(driver, Xpath=Xpath)
    return driver.find_element_by_xpath(Xpath).text


# convert raw program into structured program
def parse_raw_program(raw_program):
    numbers = set(map(str, set(range(10))))
    parsed_program = ""
    for line in raw_program.strip().split("\n"):
        # if first letter is in {numbers} leave it
        if(line[0] not in numbers):
            # for blank line, which contain only a number
            if(line.strip()[0] in numbers):
                parsed_program += "\n"
            else:
                parsed_program += line + "\n"
    return parsed_program


def fetch_program(driver):
    raw_program = fetch_raw_program(driver)
    # return parsed program
    return parse_raw_program(raw_program)


# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

def create_filename(METADATA):
    problem_number = METADATA["number"]
    # L : is string
    L = len(problem_number)
    # we need number 4-digit long 
    problem_number = "0"*(4-L) + problem_number
    problem_title = METADATA["title"]
    problem_title = "_".join(problem_title.split(" "))
    METADATA["file_name"] = "{}_{}".format(problem_number, problem_title)
    return METADATA
    

def problem_metadata_lines(METADATA):
    metadata_lines = ""
    metadata_lines += "# number : {}\n".format(METADATA["number"])
    metadata_lines += "# title : {}\n".format(METADATA["title"])
    metadata_lines += "# difficulty : {}\n".format(METADATA["difficulty"])
    metadata_lines += "# acceptance_rate : {}\n".format(METADATA["acceptance_rate"])
    metadata_lines += "# runtime : {}\n".format(METADATA["runtime"])
    metadata_lines += "# memory : {}\n".format(METADATA["memory"])
    tags = METADATA["tags"]
    metadata_lines += "# tags : {}\n".format(" , ".join(tags))
    metadata_lines += "# language : {}\n".format(METADATA["language"])
    metadata_lines += "# problem_link : {}\n".format(METADATA["problem_link"])
    metadata_lines += "# premium : {}\n".format(METADATA["premium"])
    metadata_lines += "##\n\n"
    return metadata_lines


# this function needs to be changes, when "fetch_submission_trs" will change,
# to in store program in more than one language
def store_program_file(program_string, METADATA):
    METADATA = create_filename(METADATA)

    # javascript
    if(METADATA["language"][:5] == "javas"):
        file_extension = "js"
    # python
    elif(METADATA["language"][:5] == "pytho"):
        file_extension = "py"
    
    file_location = "./PROGRAMS/{}/{}.{}".format(METADATA["difficulty"], METADATA["file_name"], file_extension)
    metadata_lines = problem_metadata_lines(METADATA)

    with open(file_location, "w") as file:
        file.write(metadata_lines)
        file.write(program_string)


# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

def update_metadata_file(file_name, METADATA):
    # #;Title;Difficulty;Acceptance Rate;Runtime;Memory;Tags;Language;Problem Link;Premium
    line = ""
    line += METADATA["number"] + ";"
    line += METADATA["title"] + ";"
    line += METADATA["difficulty"] + ";"
    line += METADATA["acceptance_rate"] + ";"
    line += METADATA["runtime"] + ";"
    line += METADATA["memory"] + ";"
    tags = METADATA["tags"]
    line += " , ".join(tags) + ";"
    line += METADATA["language"] + ";"
    line += METADATA["problem_link"] + ";"
    line += METADATA["premium"] + "\n"

    with open(file_name, "a") as file:
        file.write(line)

