# -*- coding: utf-8 -*-

import yaml


class TestFile(object):

	@staticmethod
	def _load_from_file(file_path):
		"""Load a file in yaml format."""
		with open(file_path,'r') as file:
			data = yaml.load(file)
			return data

	def __init__(self,file_path):
		self._data = self._load_from_file(file_path)

	@property
	def name(self):
		return self._data.get('name','')

	@property
	def cases(self):
		return self._data.get('cases',{})
