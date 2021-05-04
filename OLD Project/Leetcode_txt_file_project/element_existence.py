import time

def element_existence_check(driver, Xpath=None, tag_name=None, id=None, init_wait = 1, wait = 1, limit=5, exception=True):
    """
    {init_wait} : sleep for given time before element existence check
    {wait} : sleep every time when through except except block
    {exception} : whether to through error{True} or return False{False}
    """
    time.sleep(init_wait)
    while(limit > 0):
        try:
            if(Xpath):
                driver.find_element_by_xpath(Xpath)
            elif(tag_name):
                driver.find_element_by_tag_name(tag_name)
            elif(id):
                driver.find_element_by_id(id)
            return True
        except:
            print(limit, end=" ")
            time.sleep(wait)
            limit -= wait
    if(exception):
        raise Exception("\n\n\n>>> {} not found <<<\n\n\n".format(Xpath))
    else:
        return False