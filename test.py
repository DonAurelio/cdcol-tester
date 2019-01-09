# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Test(object):

    def __init__(self,testfile,driver_path):
        self._driver = webdriver.Chrome(driver_path)
        self._testfile = testfile

    def apply_test_cases(self):
        cases = self._testfile.cases
        for case_name, case_data in cases.items():
            self.apply_test_case(case_data)

    def apply_test_case(self,case):
        self.apply_login(case)
        self.apply_run(case)

    def apply_login(self,case):
        login = case.get('login',{})
        url = login.get('url','')
        actions = login.get('actions',[])

        self._driver.get(url)
        self.apply_actions(actions)

    def apply_run(self,case):
        run = case.get('run',{})
        url = run.get('url','')
        actions = run.get('actions',[])
        finished = run.get('finished','')
        collect = run.get('collect',[])

        self._driver.get(url)
        self.apply_actions(actions)
        

    def apply_actions(self,actions):
        for action in actions:
            self.appy_action(action)

    def appy_action(self,action):
        
        fields = action.split(':')

        if ':' in action:
            # "my_user:text_name=userName"
            data, element_id = action.split(':')
            element, element_value = element_id.split('=')
            element_type, element_attr  = element.split('_')

            set_function = getattr(self,'set_' + element_type)
            set_function(data,element_attr,element_value)

        if ':' not in action:
            element, element_value = action.split('=')
            element_type, element_attr  = element.split('_')
            button = self._driver.find_element(element_attr,element_value)
            button.click()

    def set_text(self,data,attr_name,attr_value):
        box = self._driver.find_element(attr_name,attr_value)
        box.send_keys(data)

    def set_select(self,data,attr_name,attr_value):
        select = self._driver.find_element(attr_name,attr_value)
        select = Select( select )

        if not data:
            select.deselect_all()
        else:
            data = data.split(',')
            for datum in data:
                select.select_by_value(datum)

        
