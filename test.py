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

		self._driver.get(url)

		username = login.get('username','')
		text, name, ref = username.split(':')
		username_box = self._find_elemet(name,ref)
		username_box.send_keys(text)

		password = login.get('password','')
		text, name, ref = password.split(':')
		password_box = self._find_elemet(name,ref)
		password_box.send_keys(text)

		password = login.get('submit','')
		name, ref = password.split(':')
		login_button = self._find_elemet(name,ref)
		login_button.click()



