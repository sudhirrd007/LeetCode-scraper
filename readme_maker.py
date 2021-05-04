import sqlite3

DATABASE_TAGS = "./data_files/TAGS.db"
DATABASE_METADATA = "./data_files/METADATA.db"
FILE_README = "README.md"
TABLE_TAGS = "TAGS"


# return intro string
def intro():
    string = """
![Language](https://img.shields.io/badge/language-Python%20%2F%20javascript-blue.svg)&nbsp;
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](./LICENSE.md)&nbsp;
![Update](https://img.shields.io/badge/update-weekly-blue.svg)&nbsp;
[![Package Status](https://img.shields.io/pypi/status/pandas.svg)](https://github.com/sudhirrd007/LeetCode_scraper)&nbsp;
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=sudhirrd007.leetcode.solutions)&nbsp;
<br><br>


### Intro
- This whole README.md file is autogenerated
- This python project fetch solved programs on leetcode website and their related data, and store them into sqlite database
- We do not need to store any program file manually or give name to it, because all those things will be done automatically
- Problem names will be grouped by related tag names and sorted by difficulty level in for each those group
- This project is not for one time run only, it will continue from where it was stopped or when all solved problems were fetched
- As you will solve new problems, it fetches those and store and update README.md file

### STEPS
1) Just run from your terminal <br>
2) You have two choice for login <br>
&nbsp;&nbsp;&nbsp;&nbsp; a) automated login : you can give username and password to command line user prompts <br>
&nbsp;&nbsp;&nbsp;&nbsp; b) manual login    : you can directly insert username and password into website <br>
3) then your work will be done
<br><br>

# Index
"""
    return string


# here, fetch tag_names from TAGS.db
def fetch_column_names(conn, table_name, ignore):
    syntax = """PRAGMA table_info({});""".format(table_name)
    cursor = conn.execute(syntax)
    
    columns = []
    for row in cursor:
        columns.append(row[1])

    columns = columns[ignore : ]
    columns.remove('Miscellaneous')
    columns.append('Miscellaneous')
    return columns


# fetch problem numbers(return sorted) for given tag
def fetch_problem_numbers_from_tag(conn, tag_name):
    problem_numbers = []

    # if there is space in tag_name then enclosed that into '' brackets   
    if(" " in tag_name):
        tag_name = "'{}'".format(tag_name)
    syntax = """SELECT ID FROM TAGS WHERE {}=1 ORDER BY Difficulty ASC, ID ASC;""".format(tag_name)

    cursor = conn.execute(syntax)
    for row in cursor:
        problem_numbers.append(row[0])
    return problem_numbers


# fetch metadata of given problems, and see below comments 
def fetch_problems_metadata(conn, problem_numbers):
    problems_dict = {}
    for problem in problem_numbers:
        syntax = """SELECT * FROM METADATA WHERE ID={};""".format(problem)
        cursor = conn.execute(syntax)
        for row in cursor:
            problems_dict[row[0]] = list(row)
    # return dictionary key:problem_number and value:its_metadata
    return problems_dict


# return string for given problem
def create_metadata_string(D):
    # 'ID', 'Title', 'Difficulty', 'Acceptance_rate', 'Runtime', 'Memory', 'Language', 'Problem_link', 'Premium', 'File_name', 'Notes'
    #  0        1          2              3               4         5           6           7             8             9          10
    string = ""
    string += "| {} ".format(D[0])
    file_location = "./data_files/PROGRAMS/{}/{}".format(D[2], D[9])
    string += "| [{}]({}) ".format(D[1], file_location)
    string += "| {} ".format(D[2])
    string += "| [{}]({}) ".format(D[6], file_location)
    string += "| {} ".format(D[4])
    string += "| {} ".format(D[3])
    string += "| [Redirect]({}) ".format(D[7])
    notes = D[10].split(", ")
    notes = " <br> ".join(notes)
    string += "| {} |\n".format(notes)
    return string


# return string representing names of tags
def index(tag_names):
    INDEX_STRING = ""
    # first letter of first tag
    first_letter = tag_names[0][0].lower()

    for tag in tag_names:
        ## when letter of tag name change, add one more line
        ## in simple words, to show tag names alphabet wise
        if(first_letter != tag[0].lower()):
            INDEX_STRING += "\n"
            first_letter = tag[0].lower()
        
        # by which we can jump to that tag portion
        inpage_link_name = "-".join(tag.split(" "))
        # ex. "[Array](#array) <br>"
        INDEX_STRING += "[{}](#{}) <br>\n".format(tag, inpage_link_name.lower())
    return INDEX_STRING


# return portion of given tag
def tag_template(tag_name):
    string = "# {}\n".format(tag_name)
    string += "|  #  | Title  |   Difficulty  |    Language   | Run Time  | Acceptance rate | LeetCode Link | Notes |\n"
    string += "|-----|------- |  ------------ | ------------- | --------- | --------------- | ------------- | ----- |\n"
    return string


# overall run this file only to create README.md file
def update_readme_file():
    conn_metadata = sqlite3.connect(DATABASE_METADATA)
    conn_tags = sqlite3.connect(DATABASE_TAGS)

    tag_names = fetch_column_names(conn_tags, TABLE_TAGS, ignore=2)

    with open(FILE_README, "w") as file:
        FIRST_LINE_STRING = "## Official [LeetCode](https://leetcode.com/problemset/all/) problems with solutions\n\n"
        file.write(FIRST_LINE_STRING)

        intro_string = intro()
        file.write(intro_string)

        INDEX_STRING = index(tag_names)
        file.write(INDEX_STRING)

        file.write("\n<hr>\n\n\n")


        for tag in tag_names:
            # fetch all problem(sorted) from this tag
            problem_numbers = fetch_problem_numbers_from_tag(conn_tags, tag)
            if(problem_numbers):
                tag_string = tag_template(tag)
                file.write(tag_string)
                # DICT : problems_dict, see function return info
                DICT = fetch_problems_metadata(conn_metadata, problem_numbers)
                for problem in problem_numbers:
                    string = create_metadata_string(DICT[problem])
                    file.write(string)
                file.write("\n\n")

update_readme_file()