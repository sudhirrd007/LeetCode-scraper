import time
import sqlite3
from element_existence import element_existence_check
from logs import insert_log


###########################################################################################################
### Fetch metadata of submission ##########################################################################
###########################################################################################################

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
    METADATA["Submission_link"] = tds[1].find_element_by_tag_name("a").get_attribute("href")
    METADATA["Runtime"] = tds[2].text
    METADATA["Memory"] = tds[3].text
    METADATA["Language"] = tds[4].text
    return METADATA


###########################################################################################################
### Fetch python/javascript program text ##################################################################
###########################################################################################################

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
def parse_raw_program(raw_program, METADATA):
    numbers = set(map(str, set(range(10))))
    
    parsed_program_list = []
    for line in raw_program.strip().split("\n"):
        # if first letter is in {numbers} leave it
        if(line[0] not in numbers):
            # for blank line, which contain only a number
            if(line.strip()[0] in numbers):
                parsed_program_list.append("")
            else:
                parsed_program_list.append(line.rstrip())

    # show starting of program
    break_point = 0
    for index, val in enumerate(parsed_program_list):
        # "###" : breakpoint, from below program starts
        if((len(val) > 2) and (val[:3] == "###")):
            break_point = index
            break

    notes = []
    count = 1
    for line in parsed_program_list[:break_point]:
        if((len(line) > 0) and (line[0] == "#")):
            notes.append("{}. {}".format(count, line[2:]))
            count += 1

    METADATA["Notes"] = notes

    parsed_program = "\n".join(parsed_program_list[break_point + 1 : ]) + "\n"
    
    return parsed_program, METADATA


def fetch_program(driver, METADATA):
    raw_program = fetch_raw_program(driver)
    
    # parsed program
    parsed_program, METADATA = parse_raw_program(raw_program, METADATA)
    return parsed_program, METADATA


###########################################################################################################
### Store program as python/javascript file ###############################################################
###########################################################################################################


def create_filename(METADATA):
    problem_number = METADATA["ID"]
    # L : is string
    L = len(problem_number)
    # we need number 4-digit long 
    problem_number = "0"*(4-L) + problem_number
    problem_title = METADATA["Title"]
    problem_title = "_".join(problem_title.split(" "))

    # javascript
    if(METADATA["Language"][:5] == "javas"):
        file_extension = "js"
    # python
    elif(METADATA["Language"][:5] == "pytho"):
        file_extension = "py"
    # other files, get extension from user
    else:
        file_extension = input("\n\nWe haven't recognize file extention\n Enter file extension only >> ")
        file_extension = file_extension.strip()
    
    METADATA["File_name"] = "{}_{}.{}".format(problem_number, problem_title, file_extension)
    return METADATA
    

def problem_metadata_lines(METADATA):
    metadata_lines = ""
    metadata_lines += "# ID : {}\n".format(METADATA["ID"])
    metadata_lines += "# Title : {}\n".format(METADATA["Title"])
    metadata_lines += "# Difficulty : {}\n".format(METADATA["Difficulty"])
    metadata_lines += "# Acceptance_rate : {}\n".format(METADATA["Acceptance_rate"])
    metadata_lines += "# Runtime : {}\n".format(METADATA["Runtime"])
    metadata_lines += "# Memory : {}\n".format(METADATA["Memory"])
    tags = METADATA["Tags"]
    metadata_lines += "# Tags : {}\n".format(" , ".join(tags))
    metadata_lines += "# Language : {}\n".format(METADATA["Language"])
    metadata_lines += "# Problem_link : {}\n".format(METADATA["Problem_link"])
    metadata_lines += "# Premium : {}\n".format(METADATA["Premium"])
    
    notes = METADATA["Notes"]
    if(notes):
        metadata_lines += "# Notes : {}\n".format(notes[0])
        if(len(notes) > 1):
            for note in notes[1:]:
                metadata_lines += "#         {}\n".format(note)
    else:
        metadata_lines += "# Notes : -\n"
    metadata_lines += "###\n\n"
    return metadata_lines


# this function needs to be changes, when "fetch_submission_trs" will change,
# to in store program in more than one language
def store_program_file(program_string, METADATA):
    METADATA = create_filename(METADATA)
    
    file_location = "./data_files/PROGRAMS/{}/{}".format(METADATA["Difficulty"], METADATA["File_name"])
    metadata_lines = problem_metadata_lines(METADATA)

    with open(file_location, "w") as file:
        file.write(metadata_lines)
        file.write(program_string)
    
    insert_log(METADATA["ID"], "Program stored")

    return METADATA


###########################################################################################################
### add metadata of problem into METADATA database #################################################################
###########################################################################################################


def update_METADATA_databse(database_file, METADATA):
    columns = ["ID", "Title", "Difficulty", "Acceptance_rate", "Runtime", "Memory", "Language", "Problem_link", "Premium", "File_name", "Notes"]

    syntax = "INSERT INTO METADATA VALUES ("

    if(METADATA["Notes"]):
        METADATA["Notes"] = ", ".join(METADATA["Notes"])
    else:
        METADATA["Notes"] = "-"

    values = []
    for col in columns:
        val = METADATA[col]
        if(type(val) == int):
            values.append("{}".format(val))
        else:
            values.append("'{}'".format(val))

    syntax += ", ".join(values)
    syntax += ");"
    
    conn = sqlite3.connect(database_file)
    conn.execute(syntax)
    conn.commit()
    conn.close()

    # insert log
    insert_log(METADATA["ID"], "metadata stored")
