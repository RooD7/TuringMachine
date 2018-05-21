#!/usr/bin/python
import os

class InputFile(object):

	def __init__(self):
		self.param = []

	def inputs(self, patchFile):
		#Realiza a leitura do arquivo
		if os.path.isfile(patchFile):
			# self.param = self.readFile()
			file = open(patchFile,'r')
			# for l in file:
			# 	print(l)
			l = file.readlines()
			print(l)
			file.close()
			
		else:
			self.param = None			

		return self.param