# -*- coding: utf-8 -*-

from selenium import webdriver


class Test(object):

    def __init__(self,testfile,driver_path):
        self._driver = webdriver.Chrome(driver_path)
        self._testfile = testfile

    def _find_elemet(self,name,ref):
        # getattr can return find_element_by_id or find_element_by_name function.
        lookup = getattr(self._driver,'find_element_by_' + ref)
        element = lookup(name)
        return element

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

        if len(fields) == 3:
            text, name, ref = fields
            box = self._find_elemet(name,ref)
            box.send_keys(text)

        if len(fields) == 2:
            name, ref = fields
            button = self._find_elemet(name,ref)
            button.click()
