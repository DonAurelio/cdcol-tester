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
        # self.apply_run(case)

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
            
            # Actions with ':' in the middle are set actions, i.e., actions 
            # that set text fields. These actions are parsed as follows:
            
            # Example: text_name=>userName:my_user", in the input type text
            # with attibute name=userName place the text 'myuser'.

            # text_name=>userName (tag_lookup)
            #   text_name (tag_name_attr)
            #       text (tag_name)
            #       name (tag_attr)
            #   userName (tag_attr_value)
            # my_user (data)

            tag_lookup, data = action.split(':')
            tag_name_attr, tag_attr_value = element_id.split('=>')
            tag_name, tag_attr = element.split('_')

            set_function = getattr(self,'set_' + tag_name)
            set_function(tag_attr,tag_attr_value,data)

        if ':' not in action:
            element, element_value = action.split('=>')
            element_type, element_attr  = element.split('_')
            button = self._driver.find_element(element_attr,element_value)
            button.click()

    def set_text(self,attr_name,attr_value,data):
        box = self._driver.find_element(attr_name,attr_value)
        box.send_keys(data)

    def set_select(self,attr_name,attr_value,data):
        select = self._driver.find_element(attr_name,attr_value)
        select = Select( select )

        if not data:
            select.deselect_all()
        else:
            data = data.split(',')
            for datum in data:
                select.select_by_value(datum)

        
