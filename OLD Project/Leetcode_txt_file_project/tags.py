

import time
import os
from element_existence import element_existence_check


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
    

# fetch all tags and store it in file
def fetch_and_store_tag_names(driver, file_name):
    if(not driver.current_url == "https://leetcode.com/problemset/all/"):
        raise Exception("\n>>> We are not on homepage <<<")
    tag_names = fetch_tag_names_from_webpage(driver)
    with open(file_name, "w") as file:
        for tag in tag_names:
            line = "{}\n".format(tag)
            file.write(line)

# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

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
        METADATA["tags"] = tags
    ## if not "related topics", then add tag as "Miscellaneous"
    else:
        METADATA["tags"] = ["Miscellaneous"]
    return METADATA


# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

def create_tags_file(FILE_TAG_NAMES, FILE_TAGS):
    with open(FILE_TAG_NAMES, "r") as file:
        tag_names = []
        for line in file:
            tag_names.append(line[:-1])
    with open(FILE_TAGS, "w") as file:
        for tag in tag_names:
            line = "{} : EASY; MEDIUM; HARD\n".format(tag)
            file.write(line)


def fetch_tags_with_problems_from_file(FILE_TAGS, updatable_tag_names):
    saved_tags_dict = {}
    with open(FILE_TAGS, "r") as file:
        for line in file:
            # ex. "Array : EASY, 1, 2; MEDIUM, 3; HARD, 5, 6"
            tag, problems = line[:-1].split(" : ")
            if(tag in updatable_tag_names):
                saved_tags_dict[tag] = {}
                difficulty_blocks = problems.split("; ")
                for difficulty in difficulty_blocks:
                    # ex. "EASY, 1, 2"
                    splits = difficulty.split(", ")
                    difficulty_level = splits[0]
                    # ex. "EASY"
                    if(len(splits) == 1):
                        problem_numbers = []
                    else:
                        problem_numbers = splits[1]
                    saved_tags_dict[tag][difficulty_level] = problem_numbers
            else:
                saved_tags_dict[tag] = line
    return saved_tags_dict


def sort_problem_numbers(numbers):
    numbers = list(map(int, numbers))
    numbers.sort()
    numbers = list(map(str, numbers))
    return numbers


# add new problem to respective tags in "tags.txt" file
def store_new_problems_in_tags_file(file_name, saved_tags_dict, updatable_tag_names):
    tag_names = list(saved_tags_dict.keys())
    tag_names.sort()
    tag_names.remove("Miscellaneous")
    tag_names.append("Miscellaneous")
    difficulty_levels = ["EASY", "MEDIUM", "HARD"]
    with open(file_name, "w") as file:
        for tag in tag_names:
            if(tag in updatable_tag_names):
                line = "{} : ".format(tag)
                
                for level in difficulty_levels:
                    numbers = saved_tags_dict[tag][level]
                    if(numbers):
                        if(level != "HARD"):
                            line += "{}, {}; ".format(level, ", ".join(numbers))
                        else:
                            line += "{}, {}\n".format(level, ", ".join(numbers))
                    else:
                        if(level != "HARD"):
                            line += "{}; ".format(level)
                        else:
                            line += "{}\n".format(level)
            else:
                line = saved_tags_dict[tag]
            file.write(line)


def update_tags_file(FILE_TAG_NAMES, FILE_TAGS, unsaved_tags_dict):
    if(not os.path.isfile(FILE_TAGS)):
        create_tags_file(FILE_TAG_NAMES, FILE_TAGS)

    # we only need to fetch this tags to update related problem numbers in "tags.txt" file
    updatable_tag_names = list(unsaved_tags_dict.keys())
    saved_tags_dict = fetch_tags_with_problems_from_file(FILE_TAGS, updatable_tag_names)

    for tag in updatable_tag_names:
        for difficulty_level in unsaved_tags_dict[tag]:
            ## combine problem numbers from unsaved_tags and saved_tags
            unsaved_problems = unsaved_tags_dict[tag][difficulty_level]
            saved_problems = saved_tags_dict[tag][difficulty_level]
            # combinition of lists
            problems = unsaved_problems + saved_problems

            # store all this problems back to saved_tags_dict
            saved_tags_dict[tag][difficulty_level] = sort_problem_numbers(problems)
            
    store_new_problems_in_tags_file(FILE_TAGS, saved_tags_dict, updatable_tag_names)


