
import sqlite3
import time
import os
from element_existence import element_existence_check
from logs import insert_log


#############################################################################################################
### Fetch tags names from website #################################################################################
#############################################################################################################

# #NOTCALL
def fetch_tag_names_from_webpage(driver):
    # dropdown use to filter tags
    dropdown_Xpath = '//*[@id="question-app"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/button'
    element_existence_check(driver, Xpath=dropdown_Xpath)
    dropdown = driver.find_element_by_xpath(dropdown_Xpath)
    dropdown.click()

    # list of rows
    tag_names_Xpath = '//*[@id="question-app"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]'
    element_existence_check(driver, Xpath=tag_names_Xpath, init_wait=0.3)
    tags_div = driver.find_element_by_xpath(tag_names_Xpath)
    tag_spans = tags_div.find_elements_by_tag_name("span")
    tag_names = [span.text.strip() for span in tag_spans]
    tag_names.sort()
    # Miscellaneous : for some problems, which are not categorized
    tag_names.append("Miscellaneous")

    dropdown.click()
    return tag_names
    

# #NOTCALL
def create_table_syntax(tag_names):
    L = len(tag_names)

    table_syntax = "CREATE TABLE TAGS (ID INT PRIMARY KEY NOT NULL, Difficulty INT NOT NULL, "
    declarations = ["'{}' INT DEFAULT 0 NOT NULL"] * L
    table_syntax += ", ".join(declarations)
    table_syntax += ");"
    table_syntax = table_syntax.format(*tag_names)
    return table_syntax


# #NOTCALL
# add new tags in database_file
def add_columns(tag_names, database_file):
    conn_ = sqlite3.connect(database_file)
    for tag in tag_names:
        styntax = """ALTER TABLE TAGS ADD COLUMN '{}' INT DEFAULT 0;""".format(tag)
        conn_.execute(styntax)
    conn_.commit()
    conn_.close()


# fetch column names(means tag names) from database_file
def fetch_saved_tag_names(database_file):
    conn_ = sqlite3.connect(database_file)
    syntax = """PRAGMA table_info(TAGS);"""
    cursor = conn_.execute(syntax)
    columns = []
    for row in cursor:
        columns.append(row[1])
    conn_.close()
    return columns[2:]


# fetch all tags and store it in file
def fetch_and_store_tag_names(driver, database_file, first_time=True):
    if(not driver.current_url == "https://leetcode.com/problemset/all/"):
        raise Exception("\n>>> We are not on homepage <<<")

    tag_names = fetch_tag_names_from_webpage(driver)

    if(first_time):
        conn = sqlite3.connect(database_file)
        syntax = create_table_syntax(tag_names)
        conn.execute(syntax)
        conn.commit()
        conn.close()
    else:
        saved_tag_names = fetch_saved_tag_names(database_file)
        if(set(saved_tag_names) - set(tag_names)):
            raise Exception("\n>>> Tag names mismatched <<<")
        else:
            latest_tag_names = set(tag_names) - set(saved_tag_names)
            latest_tag_names = list(latest_tag_names)
            latest_tag_names.sort()
            add_columns(latest_tag_names, database_file)


###########################################################################################################
### Fetch Tags of specific problem from specific problem webpage ##########################################
###########################################################################################################

# check the <div> of "related topics" and return Xpath of that
def fetch_related_topics_element_Xpath(driver):             
    for div_number in range(4, 8):
        Xpath = '//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div[{}]'.format(div_number)
        try:
            div = driver.find_element_by_xpath(Xpath)
            element = div.find_element_by_tag_name("div").find_element_by_tag_name("div").find_element_by_tag_name("div")
            string = element.text.strip()
            if(string.lower() == "related topics"):
                return Xpath
        except:
            pass
    # we don't want exception, that is why False
    return False


def fetch_problem_tags(driver, METADATA):
    # to retrive "related topics" Xpath
    Xpath = fetch_related_topics_element_Xpath(driver)
    if(Xpath):
        related_topics_dropdown = driver.find_element_by_xpath(Xpath)
        # open "related topics" dropdown
        related_topics_dropdown.click()
        time.sleep(1)

        Xpath = '{}/div[2]'.format(Xpath)
        div = driver.find_element_by_xpath(Xpath)
        # <a> of problem tags
        as_ = div.find_elements_by_tag_name("a")
        tags = [a.find_element_by_tag_name("span").text.strip() for a in as_]
        METADATA["Tags"] = tags
    ## if not "related topics", then add tag as "Miscellaneous"
    else:
        METADATA["Tags"] = ["Miscellaneous"]
    return METADATA


#############################################################################################################
### add problem into respective tags in TAGS database #######################################################
#############################################################################################################

def tags_mapper(tag):
    mapper = {"EASY": 1, "MEDIUM": 2, "HARD": 3}
    return mapper[tag]


def update_TAGS_databse(database_file, METADATA):
    L = len(METADATA["Tags"])
    conn = sqlite3.connect(database_file)

    syntax = "INSERT INTO TAGS (ID, Difficulty"
    
    values = ", '{}'" * L
    syntax += values.format(*METADATA["Tags"])
    syntax += ") VALUES ({}, {}".format(METADATA["ID"], tags_mapper(METADATA["Difficulty"]))
    syntax += ", 1" * L
    syntax += ");"
    conn.execute(syntax)
    conn.commit()
    conn.close()

    # insert log
    insert_log(METADATA["ID"], "tags has been added")
