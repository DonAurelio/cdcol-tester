# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Test(object):

    def __init__(self,testfile,driver_path):
        self._driver = webdriver.Chrome(driver_path)
        self._testfile = testfile

    def _find_elemet(self,attr,attr_value):
        # getattr can return find_element_by_id or find_element_by_name function.
        lookup = getattr(self._driver,'find_element_by_' + attr)
        element = lookup(attr_value)
        return element

    def _action_type(self,action):
        data, element_id = action.split(':') if ':' in action else None, action
        field, value = element_id.split('=')
        field_type, field_attr  = field.split('_')
        return field_type

    def apply_test_cases(self):
        cases = self._testfile.cases
        for case_name, case_data in cases.items():
            self.apply_test_case(case_data)

    def apply_test_case(self,case):
        self.apply_login(case)

    def apply_login(self,case):
        login = case.get('login',{})
        url = login.get('url','')
        actions = login.get('actions',[])

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
            field, value = element_id.split('=')
            field_type, field_attr  = field.split('_')

            set_function = getattr(self,'set_' + field_type)
            set_function(data,field_attr,value)

        if ':' not in action:
            element, element_value = action.split('=')
            element_type, element_attr  = element.split('_')
            button = self._find_elemet(element_attr,element_value)
            button.click()

    def set_text(self,data,attr_name,attr_value):
        box = self._find_elemet(attr_name,attr_value)
        box.send_keys(data)

    def set_select(self,data,attr_name,attr_value):
        select = self._find_elemet(attr_name,attr_value)
        select = Select( select )
        
