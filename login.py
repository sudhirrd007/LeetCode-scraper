# login file to make login in leetcode
# this program make login to leetcode only and nothing else

import time
from element_existence import element_existence_check


# show all problems on single page
def show_all_problems(driver):
    # drop down menu
    Xpath = '//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span[1]/select/option[4]'
    element_existence_check(driver, Xpath=Xpath)
    show_all = driver.find_element_by_xpath(Xpath)
    show_all.click()


def open_homepage(driver):
    # problem btn on navbar
    Xpath = '//*[@id="navbar-root"]/div/div/div[1]/div[3]/a'
    element_existence_check(driver, Xpath=Xpath)
    problems_btn = driver.find_element_by_xpath(Xpath)
    problems_btn.click()

    show_all_problems(driver)



# check if captcha element is present or not
def captcha_check():
    flag = input("\nIf you see captcha, enter {1) otherwise {ENTER} >> ")
    if(flag == "1"):
        input("\nSolve Captcha and press <ENTER> >> ")
        return True
    else:
        return False


# make automatic login
def automatic_log_in(driver, username, password):
    element_existence_check(driver, id='id_login')
    driver.find_element_by_id('id_login').send_keys(username)
    time.sleep(1)
    driver.find_element_by_id('id_password').send_keys(password)
    time.sleep(1)
    log_in_btn = driver.find_element_by_xpath('//*[@id="signin_btn"]')
    time.sleep(1)
    log_in_btn.click()

    if(captcha_check()):
        log_in_btn.click()


# major function called from main.py
def make_log_in(driver):
    # fetch input from user
    flag = input("\nManual login: {ENTER}\nAutomatic login: {0} >> ")

    if(flag == "0"):
        print("\n>>> Your login info is secured <<<\n")
        username = input("\nEnter your user name >> ").strip()
        password = input("]nEnter your password >> ").strip()
        automatic_log_in(driver, username, password)
    else:
        input("\nPress <ENTER> after successful login >> ")

    open_homepage(driver)
